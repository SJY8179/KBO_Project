# KBO_Project

First Mini Project of Python Data Analysis

### 실행 명령어

1. streamlit run app/main.py : streamlit 개발 환경 실행
2. python -m scraper.scraper_ex : 루트 기준으로 해당 스크립트 실행

---

### 네이밍 규칙

1안

- 파일 네임, 변수, 함수, 상수 : snake_case

- 클래스: PascalCase

2안

- 파일 네임 : PascalCase

- 변수, 함수: snake_case

- 클래스: PascalCase

- 상수: ALL_CAPS

---

### 폴더 구조

.
├── README.md
├── app
│ ├── \__init_.py
│ ├── components
│ ├── main.py
│ └── pages
├── aseets : 리소스 폴더
├── models : 데이터 모델링
├── data : 데이터 저장소
├── requirements.txt
├── scraper : 크롤링 로직
├── libs : util 함수
└── test.py
