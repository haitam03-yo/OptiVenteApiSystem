from fastapi import FastAPI
from routes import predictSales
from fastapi.middleware.cors import CORSMiddleware

# Create the FastAPI instance
app = FastAPI()

# CORS configuration
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://localhost:5173",  # Include the frontend port here if using Vite or similar
]

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include your router for prediction sales
app.include_router(predictSales.prediction_sales_router)


