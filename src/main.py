from fastapi import FastAPI
from routes import predictSales

app = FastAPI()
app.include_router(predictSales.prediction_sales_router)