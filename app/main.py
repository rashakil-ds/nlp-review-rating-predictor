#Author @Rashedul Alam
from fastapi import FastAPI
from pydantic import BaseModel
from nlp_pipeline.inference import predict as predict_fn

app = FastAPI(
    title="Review Rating API",
    version="1.0.0"
)

class PredictRequest(BaseModel):
    text: str

class PredictResponse(BaseModel):
    #label_id: int
    #label_name: str
    stars_text: str
    confidence: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    result = predict_fn(req.text)
    return result
