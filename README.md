# 감정 분석 API 프로젝트

**이름:** 장형준  
**학번:** 2022143032

---

## 프로젝트 개요

이 프로젝트는 FastAPI와 HuggingFace Transformers를 활용한 감정 분석 REST API와  
HTML/JS 기반의 간단한 프론트엔드를 제공합니다.

- 사용자는 웹페이지에서 텍스트(리뷰 등)를 입력하면
- FastAPI 서버가 감정 분석 모델로 예측을 수행해
- 별점(1~5점) 및 신뢰도를 반환합니다.

---

## 주요 기술 스택

- **Backend:** FastAPI, Transformers, PyTorch
- **Frontend:** HTML, CSS, JavaScript (fetch API)
- **모델:** 사전학습 BERT 기반 감정 분석 모델

---

## 폴더 구조


<pre>      ├── app/
      │   ├── main.py # FastAPI 서버 및 감정 분석 API 
      │   └── sentiment_model/ # 저장된 모델 파일 (config.json, pytorch_model.bin, tokenizer 등) 
      ├── index.html # 프론트엔드 (HTML/JS) 
      ├── requirements.txt 
      └── README.md </pre>





---

## 실행 방법

### 1. 패키지 설치

pip install -r requirements.txt


### 2. FastAPI 서버 실행

uvicorn app.main:app --reload --host 127.0.0.1 --port 8001


### 3. 프론트엔드 실행

- `index.html` 파일을 브라우저에서 직접 열기 (더블클릭)
- 또는 간단한 로컬 서버에서 실행

---

## API 사용 예시

### 엔드포인트

- **POST** `/predict`

### 요청 예시

{
"text": "The food was delicious and the staff was friendly"
}


### 응답 예시

[
{
"label": "LABEL_4",
"score": 0.4660353362560272
}
]


---

## 프론트엔드 예시 화면

- 이름: 장형준
- 학번: 2022143032
- 텍스트 입력 → "분석하기" 클릭 → 분석 결과(별점/신뢰도) 표시

---

## CORS 설정

FastAPI 코드에 아래와 같이 CORS 미들웨어가 추가되어 있습니다.



from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
CORSMiddleware,
allow_origins=[""], # 개발용 전체 허용, 배포 시에는 도메인 지정
allow_credentials=True,
allow_methods=[""],
allow_headers=["*"],
)



---

## 참고

- 모델은 반드시 `app/sentiment_model` 폴더에 있어야 하며,  
  내부에 `config.json`, `pytorch_model.bin`, `tokenizer.json` 등이 포함되어야 합니다.
- 서버와 프론트엔드의 포트가 다르면 fetch 주소(`http://127.0.0.1:8001/predict`)를 맞춰주세요.

---

## 라이선스

MIT License

