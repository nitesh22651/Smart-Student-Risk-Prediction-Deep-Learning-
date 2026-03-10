from pydantic import BaseModel


class PredictDropoutPayload(BaseModel):
    attendance_percentage: float	
    assignments_rate: float	
    quizzes_score: float	
    previous_grades: float	
    time_spent_on_study: float
    extracurricular: float
    stress_level: float