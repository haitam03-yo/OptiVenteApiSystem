from pydantic import BaseModel
from typing import List

class SalesPredictionResponse(BaseModel) :
    predicted_sales: List[int]