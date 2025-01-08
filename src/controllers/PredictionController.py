from .BaseController import BaseController
from dataModels import SalesPredictionRequest, SalesPredictionResponse
from datetime import datetime
import pickle
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
from numpy import floor

class PredictionController(BaseController):
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Paths relative to the base directory
        self.models_paths = [os.path.join(base_dir, 'models', 'xgb_model.pkl')]
        self.encoder_path = os.path.join(base_dir, 'encoder')

    def upload_models(self):
        models = []
        for model_path in self.models_paths:
            with open(model_path, "rb") as model_file:
                models.append(pickle.load(model_file))
        return models
    
    def upload_encoders(self):
        encoders = {}
        
        # Ensure the encoder path exists and contains files
        if not os.path.exists(self.encoder_path):
            raise FileNotFoundError(f"Encoder path not found: {self.encoder_path}")
        
        # Loop through all files in the encoder directory
        for file_name in os.listdir(self.encoder_path):
            # Only process files that match the naming pattern "label_encoders_{col}.pkl"
            if file_name.startswith('label_encoders_') and file_name.endswith('.pkl'):
                # Extract the column name from the file name
                column_name = file_name.replace('label_encoders_', '').replace('.pkl', '')
                file_path = os.path.join(self.encoder_path, file_name)
                
                # Load the encoder and add it to the dictionary
                with open(file_path, 'rb') as file:
                    encoders[column_name] = pickle.load(file)
        
        return encoders

    def voting_ensemble(self, predictions_list):
        return sum(predictions_list) / len(predictions_list)  
    
    def getDateFeature(self, df):
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['day'] = df['date'].dt.day
        df['weekday'] = df['date'].dt.weekday
        df['week'] = df['date'].dt.isocalendar().week
        df.drop('date',axis=1)
        return df
    
    def encode_cat_col(self, df):
        label_encoders = self.upload_encoders()
        for col, encoder in label_encoders.items():
            if col in df.columns:
                print(f"Encoding column {col}")
                try:
                    df[col] = encoder.transform(df[col]).astype(int)
                except ValueError as e:
                    raise ValueError(
                        f"Error encoding column {col}. "
                        f"Ensure all categories in the column exist in the training data. Error: {e}"
                    )
        return df
    
    def target_encode(self,df):
        file_path = os.path.join(self.encoder_path, 'target_encoder.pkl')
        with open(file_path, 'rb') as file:
            mean_encoded = pickle.load(file)
        # Apply target encoding to the test set
        df['id_produit_encoded'] = df['id_produit'].map(mean_encoded)
        return df
                

    
    def preprocess_features(self, request: SalesPredictionRequest):

        
        # Now prepare the data to send in the request
        data = {
            'id_produit': [request.id_produit],
            'date': [request.date],
            'categorie': [request.categorie],
            'marque': [request.marque],
            'prix_unitaire': [request.prix_unitaire],
            'promotion': [request.promotion],
            'stock_disponible': [request.stock_disponible],
            'condition_meteo': [request.condition_meteo],
            'region': [request.region],
            'moment_journee': [request.moment_journee],
        }



        df = pd.DataFrame(data)

        # Convert 'date' column to datetime
        df['date'] = pd.to_datetime(df['date'])
        df['jour_ferie'] = (df['date'].dt.weekday >= 5).astype(int)

        df['weekend'] = df['date'].dt.month.apply(lambda x: 1 if x == 12 else 0)


        # Add date features

        # Encode categorical columns
        df = self.encode_cat_col(df)
        df = self.target_encode(df)

        return df

    def predict_sales(self, request: SalesPredictionRequest):
        models = self.upload_models()
        
        # Preprocess the input features
        features = self.preprocess_features(request)
        features1 = features.drop(['id_produit'], axis=1)
        

        
        predictions = []
        
        # Loop through the next 'forecast_period' days to predict sales
        for i in range(request.forecast_period):
            # Shift the date for each prediction (assuming daily data)
            future_date = features['date'].iloc[0] + pd.Timedelta(days=i+1)
            features1['date'] = future_date
            
            features1 = self.getDateFeature(features1)
            feature_order = ['categorie', 'marque', 'prix_unitaire', 'promotion', 'jour_ferie', 'weekend', 
                        'stock_disponible', 'condition_meteo', 'region', 'moment_journee', 'year', 
                        'month', 'day', 'weekday', 'week', 'id_produit_encoded']

            # Reorder columns in features1 according to feature_order
            features1 = features1[feature_order]
            
            
            # Predict using each model
            all_models_predicted_sales = []
            for model in models:
                predicted_sales = floor(model.predict(features1))
                all_models_predicted_sales.append(predicted_sales[0])
            
            # Perform voting ensemble
            final_prediction = self.voting_ensemble(all_models_predicted_sales)
            print((future_date,final_prediction))
            predictions.append(final_prediction)
        
        return SalesPredictionResponse(predicted_sales=predictions)
