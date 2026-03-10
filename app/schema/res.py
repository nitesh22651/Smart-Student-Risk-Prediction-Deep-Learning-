from pydantic import BaseModel


class PredictDropoutResponse(BaseModel):
    status: int
    confidence: float