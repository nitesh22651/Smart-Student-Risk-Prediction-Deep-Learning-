from fastapi import FastAPI
from .apis import prediction_router


app = FastAPI(title="Course Dropout Prediction AI Backend")


app.include_router(prediction_router)

