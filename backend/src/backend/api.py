from fastapi import FastAPI
from backend.data_processing import df

app = FastAPI() # Create an instance of the FastAPI application

@app.get("/solar-data/csv") # Get solar data in CSV format and add endpoint to the FastAPI app
async def show_data(): # Define an asynchronous function to handle the API request
    return df.to_dict(orient="records") # Convert the DataFrame to a dictionary with records orientation and return it as the response