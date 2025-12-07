#Author @Rashedul Alam
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"

from pathlib import Path
import json
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

BASE_DIR = Path(__file__).resolve().parents[1]   #NLP/MODEL_DIR
MODEL_DIR = BASE_DIR / "ml_training" / "models" / "best_model_distilbert"

print("MODEL_DIR =", MODEL_DIR)
print("Exists =", MODEL_DIR.exists())

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

with open(MODEL_DIR / "label2id.json") as f:
    label2id = json.load(f)

with open(MODEL_DIR / "id2label.json") as f:
    id2label = json.load(f)

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
model.to(DEVICE)
model.eval()

def predict(text: str) -> dict:

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True
    ).to(DEVICE)

    with torch.no_grad():
        logits = model(**inputs).logits
        probs = logits.softmax(dim=-1)
        pred = probs.argmax(dim=-1).item()       

    stars_numeric = pred + 1
    star_symbol = "★"
    stars_text = star_symbol * stars_numeric

    return {
        #"label_id": int(pred),
        #"label_name": id2label[str(pred)],
        "stars_text": f"{stars_numeric} {stars_text}",
        "confidence": float(probs[0][pred])
    }
