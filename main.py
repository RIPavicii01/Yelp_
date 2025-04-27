from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_name = "ethzanalytics/distilgpt2-tiny-conversational"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# pad_token 설정 (없으면 eos_token으로 대체)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(model_name).to("cuda" if torch.cuda.is_available() else "cpu")

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat/")
def chat(req: ChatRequest):
    inputs = tokenizer(
        req.prompt,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=128
    )
    input_ids = inputs["input_ids"].to(model.device)
    attention_mask = inputs["attention_mask"].to(model.device)
    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_new_tokens=50,
        pad_token_id=tokenizer.pad_token_id
    )
    result = tokenizer.decode(output[0], skip_special_tokens=True)
    return {"response": result}
