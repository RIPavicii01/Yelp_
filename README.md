# distilgpt2-tiny-chatbot

> **장형준 | 2022143032**
>
> FastAPI와 Hugging Face의 경량 챗봇 모델, 그리고 HTML/CSS/JS 프론트엔드로 만든 심플 AI 챗봇 프로젝트

---

## 🛠️ 사용한 언어 & 기술 스택

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/HuggingFace-FFD21F?style=flat&logo=huggingface&logoColor=black"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black"/>
</p>

---

## 📌 프로젝트 소개

- **distilgpt2-tiny-chatbot**은 FastAPI와 Hugging Face의 초경량 챗봇 모델(`ethzanalytics/distilgpt2-tiny-conversational`)을 활용한 간단한 AI 챗봇입니다.
- 프론트엔드는 HTML, CSS, JavaScript만으로 구현되어 누구나 쉽게 실행할 수 있습니다.
- 인삿말, 간단한 영어 대화, 챗봇 데모에 적합합니다.

---

## 🚀 설치 및 실행 방법

### 1. 백엔드(FastAPI) 실행

- 필수 패키지 설치
    pip install fastapi uvicorn transformers torch

- 서버 실행
uvicorn main:app --reload

### 2. 프론트엔드 실행

- `index.html`, `style.css`, `chat.js`를 같은 폴더에 두고,  
  `index.html`을 브라우저에서 더블클릭(또는 Live Server 등으로 실행)

---

## 🗂️ 폴더 구조

├── main.py # FastAPI 백엔드 (챗봇 API)

├── index.html # 프론트엔드 HTML

├── style.css # 프론트엔드 CSS

├── chat.js # 프론트엔드 JS

└── README.md

---

## 💬 주요 기능

- FastAPI 기반 REST 챗봇 API (`/chat/`)
- Hugging Face 경량 챗봇 모델 사용
- HTML/CSS/JS 프론트엔드, 반응형 디자인, 말풍선 UI
- 실시간 채팅, AI 응답 대기 애니메이션, 프로젝트/사용자 정보 표시

---

## 🙋🏻‍♂️ 개발자

- **이름:** 장형준  
- **학번:** 2022143032

---

## 📄 라이선스

- 본 프로젝트는 MIT 라이선스를 따릅니다.

---

## ⭐️ 기타

- 더 자연스러운 챗봇이 필요하다면 모델만 교체해서 사용할 수 있습니다.
- 문의/기여는 Pull Request 또는 Issue로 남겨주세요.
