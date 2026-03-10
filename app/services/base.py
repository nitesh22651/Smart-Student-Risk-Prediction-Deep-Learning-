from abc import ABC, abstractmethod
import joblib
import numpy as np
from tensorflow.keras.models import load_model


class BaseCDPPredictService(ABC):
    def __init__(self):
        self.preprocessor = joblib.load("artifacts/preprocessor.joblib")
        self.model = load_model("artifacts/checkpoints/resnet_tabular_best.keras") 
        self.numeric_features = [
            "attendance_percentage",
            "assignments_rate",
            "quizzes_score",
            "previous_grades",
            "time_spent_on_study",
            "extracurricular",
            "stress_level",
        ]
        
    @abstractmethod
    async def preprocess_input(self, data:dict) -> np.array:
        pass
    
    @abstractmethod
    async def predict_confidense(self, data:dict) -> float:
        pass
        