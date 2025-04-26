from datasets import load_dataset

def download_and_save():
    dataset = load_dataset("yelp_review_full")
    # 예시로 1만개만 추출해서 저장
    small_train = dataset['train'].shuffle(seed=42).select(range(10000))
    small_train.to_csv("data/yelp_small_train.csv")

if __name__ == "__main__":
    download_and_save()
