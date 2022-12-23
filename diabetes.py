from pydantic import  BaseModel
# create class which describes diabetes measurement
class Diabetes(BaseModel):
    Pregnancies: int
    Glucose:int
    BloodPressure: int
    SkinThickness: int
    Insulin:int
    Bmi:float
    DiabetesPedigreeFunction:float
    Age:int




