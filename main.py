from typing import Union

from fastapi import FastAPI

import pandas as pd 
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/predictions")
def prediction(self, PlasmaGlucose, Blood_W_Result_1, BloodPressure, Blood_W_Result_2, Blood_W_Result_3, BMI, Blood_W_Result_4, Age, Insurance):
    result = predict.model(pd.DataFrame([PlasmaGlucose, Blood_W_Result_1, BloodPressure, Blood_W_Result_2, Blood_W_Result_3, BMI, Blood_W_Result_4, Age, Insurance]))
    
    return {
        "PlasmaGlucose": PlasmaGlucose,
        "Blood_W_Result_1": Blood_W_Result_1,
        "BloodPressure": BloodPressure,
        "Blood_W_Result_2": Blood_W_Result_2,
        "Blood_W_Result_3": Blood_W_Result_3,
        "BMI": BMI,
        "Blood_W_Result_4": Blood_W_Result_4,
        "Age": Age,
        "Insurance": Insurance
    }


#PlasmaGlucose  Blood.W.Result-1  BloodPressure Blood.W.Result-2 Blood.W.Result-3  BMI Blood.W.Result-4 Age Insurance  
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

