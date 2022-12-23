import uvicorn
from fastapi import  FastAPI
from diabetes import Diabetes

import  numpy as np
import pickle
import  pandas as pd

# create the app object
app = FastAPI()
pickle_in = open("modelsvm.pkl","rb")
classifier = pickle.load(pickle_in)
# model_dir = "model.h5"
# classifier = load_model(model_dir)


@app.get('/')
def index():
    return {'massage':'Hello,Dahal'}

@app.get('/name')
def get_name(name:str):
    return {"royal dahal":f'{name}'}

#3. expose the prediction functaionality
@app.post('/predict')
def predict_banknote(data:Diabetes):
    data=data.dict()
    Pregnancies = data['Pregnancies']
    Glucose = data['Glucose']
    BloodPressure = data['BloodPressure']
    SkinThickness = data['SkinThickness']
    Insulin = data['Insulin']
    Bmi = data['Bmi']
    DiabetesPedigreeFunction = data['DiabetesPedigreeFunction']
    Age = data['Age']
#taking inputs for prediction
    prediction=classifier.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,Bmi,DiabetesPedigreeFunction,Age]])

    if (prediction[0]>0.5):
        prediction="The person has diabetes"
    else:
        prediction = "The person is healthy"
    return {
        prediction
    }





#5.run the api with uvicorn
# if __name__ =='__main__':
#     uvicorn.run(app,host='127.0.0.1',port=8001)
if __name__ =='__main__':
    app.run(host='0.0.0.0',port=8080)

