import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "meta-llama/Meta-Llama-Guard-2-8B"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to("cuda" if torch.cuda.is_available() else "cpu")

input_text = "안녕하세요! 무엇을 도와드릴까요?"
input_ids = tokenizer.encode(input_text, return_tensors="pt").to(model.device)
output = model.generate(input_ids, max_new_tokens=50)
result = tokenizer.decode(output[0], skip_special_tokens=True)
print(result)
