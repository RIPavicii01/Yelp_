from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
import numpy as np
from sklearn.metrics import accuracy_score
import torch

# 1. 데이터셋 불러오기
raw_datasets = load_dataset("yelp_review_full")

# 2. 토크나이저 및 모델 불러오기
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=5)

# 3. 토큰화 함수 정의
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

# 4. 데이터셋 토큰화
encoded_datasets = raw_datasets.map(tokenize_function, batched=True)

# 5. 평가 지표 함수 정의
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return {"accuracy": accuracy_score(labels, predictions)}

# 6. 훈련 인자 설정
training_args = TrainingArguments(
    output_dir="../app/results",
    eval_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=1,
    weight_decay=0.01,
    save_strategy="epoch"
)

# 7. Trainer 객체 생성
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=encoded_datasets["train"].shuffle(seed=42).select(range(10000)),
    eval_dataset=encoded_datasets["test"].shuffle(seed=42).select(range(2000)),
    compute_metrics=compute_metrics
)

# 8. 모델 학습
trainer.train()

# 9. 평가
metrics = trainer.evaluate()
print(metrics)

# 모델 저장
trainer.save_model("./sentiment_model")
tokenizer.save_pretrained("./sentiment_model")

