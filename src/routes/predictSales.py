from fastapi import APIRouter, Depends
from controllers import PredictionController
from dataModels import SalesPredictionResponse, SalesPredictionRequest


prediction_sales_router = APIRouter(
    prefix="/api/v1/ml",
    tags=['api_v1','ml']
)

@prediction_sales_router.post('/predict_sales',response_model=SalesPredictionResponse)
async def prediction_sales_endpoint(request: SalesPredictionRequest):
    print(request.dict())
    predictionController = PredictionController()
    models_path = []
    #models = predictionController.upload_models(models_path)
    predicted_sales = predictionController.predict_sales(
        request
    )
    return predicted_sales

@prediction_sales_router.post('/welcome')
async def prediction_sales_endpoint():
    return "hi"