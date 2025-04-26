from datasets import load_dataset
import json

# Yelp 리뷰 데이터셋 불러오기
dataset = load_dataset("yelp_review_full")

# 학습 데이터 10개, 테스트 데이터 5개 샘플 추출
train_samples = [dataset['train'][i] for i in range(10)]
test_samples = [dataset['test'][i] for i in range(5)]

# 샘플 데이터 구조 확인
print("Train Sample:", train_samples[0])
print("Test Sample:", test_samples[0])

# JSON 파일로 저장
with open("sample_yelp.json", "w", encoding="utf-8") as f:
    json.dump({
        "train": train_samples,
        "test": test_samples
    }, f, ensure_ascii=False, indent=2)

print("샘플 데이터가 sample_yelp.json 파일로 저장되었습니다.")
