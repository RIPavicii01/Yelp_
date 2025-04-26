from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
from pathlib import Path
from fastapi.responses import JSONResponse
import traceback
import logging


# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발용이므로 전체 허용, 배포 시에는 도메인 지정
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
try:
    model_path = Path(__file__).parent / "sentiment_model"
    logger.info(f"모델 경로: {model_path} (존재 여부: {model_path.exists()})")
    model = AutoModelForSequenceClassification.from_pretrained(
        str(model_path),
        local_files_only=True
    )
    tokenizer = AutoTokenizer.from_pretrained(
        str(model_path),
        local_files_only=True
    )
    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model=model,
        tokenizer=tokenizer
    )
    logger.info("모델 로딩 성공!")
except Exception as e:
    logger.error(f"모델 로딩 에러: {str(e)}")
    traceback.print_exc()
    sentiment_pipeline = None

class TextIn(BaseModel):
    text: str

@app.get("/")
async def root():
    if sentiment_pipeline is None:
        return {"status": "error", "message": "모델 로딩에 실패했습니다. 서버 로그를 확인하세요."}
    return {"status": "ok", "message": "감정 분석 API가 준비되었습니다."}

@app.post("/predict")
async def predict(item: TextIn):
    try:
        if sentiment_pipeline is None:
            raise Exception("모델이 정상적으로 로드되지 않았습니다. 서버 로그를 확인하세요.")
        result = sentiment_pipeline(item.text)
        return {"result": result}
    except Exception as e:
        error_message = str(e)
        logger.error(f"예측 중 에러 발생: {error_message}")
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={
                "error": error_message,
                "error_type": type(e).__name__,
                "details": traceback.format_exc()
            }
        )

