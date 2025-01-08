from pydantic import BaseModel

class SalesPredictionRequest(BaseModel):
    id_produit: str              # Product ID
    date: str                    # Date
    categorie: str               # Category
    marque: str                  # Brand
    prix_unitaire: float         # Unit price
    promotion: bool              # Promotion status
    stock_disponible: float      # Stock available
    condition_meteo: str         # Weather condition
    region: str                  # Region
    moment_journee: str          # Time of day
    forecast_period:int
