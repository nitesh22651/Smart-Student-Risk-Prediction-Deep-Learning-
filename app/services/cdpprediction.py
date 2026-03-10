import numpy as np
import pandas as pd
from .base import BaseCDPPredictService


class CDPPredictionService(BaseCDPPredictService):
    def __init__(self):
        super().__init__()
        
    async def preprocess_input(self, data:dict) -> np.array:
        """
        Convert input dict to a row for the sklearn preprocessor.
        """
        missing = [feat for feat in self.numeric_features if feat not in data]
        if missing:
            raise ValueError(f"Missing required features: {missing}")
        
        row_df = pd.DataFrame(
            [{feat: float(data[feat]) for feat in self.numeric_features}],
            columns=self.numeric_features,
        )
        X_processed = self.preprocessor.transform(row_df)  # returns numpy array
        return np.asarray(X_processed, dtype=np.float32)
    
    async def predict_confidense(self, data:dict) -> float:
        """
        Predict dropout confidence using sklearn preprocessor + .keras model.
        """
        x = await self.preprocess_input(data)
        y_pred = self.model.predict(x, verbose=0)
        return float(y_pred[0][0])