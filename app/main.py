from fastapi import FastAPI
from pydantic import BaseModel
import COPD


class InputData(BaseModel):
    pass


app = FastAPI()
model = COPD.model()


@app.post("/predict")
def predict(data: InputData):
    result = model.predict(data)
    output = round(float(result), 3)
    return output
