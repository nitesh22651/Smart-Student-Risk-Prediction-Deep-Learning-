from fastapi import APIRouter, Request, status, HTTPException
from ..schema import PredictDropoutPayload, PredictDropoutResponse
from ..services import CDPPredictionService


prediction_router = APIRouter(prefix="/predict", tags=["CDP Prediction"])


cdp_service = CDPPredictionService()


@prediction_router.post("/dropout", response_model=PredictDropoutResponse)
async def predict_course_dropout(request: Request, payload: PredictDropoutPayload):
    try:
        prediction = await cdp_service.predict_confidense(payload.model_dump())
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail=str(e)
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error! Try again later..."
        )
    
    return PredictDropoutResponse(
        status=status.HTTP_200_OK,
        confidence=prediction
    )