from pydantic import BaseModel

class SalesPredictionResponse(BaseModel) :
    predicted_sales: int