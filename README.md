# KBO_Project 사용자 가이드 (User Guide)

## 서비스 소개

KBO 야구 팬 성향분석 및 구단별 관중수 증가 요인분석

---

## 주요 기능

### 승률 - 관중수 상관관계

- 기간, 구단 선택에 따른 승률, 관중수 상관관계 인사이트 제공
- 승률 vs 평균관중수 산점도 차트
- 연도별 승률 & 관중수 트렌드 차트
- 팀별 승률 및 관중수 순위 차트
- 분석 결과 및 해설 제공

### SNS 팔로워 vs 관중수 + 구단 나이 상관 관계

- 기간, 구단 선택에 따른 SNS 팔로워 vs 총관중수 산점도, 구단 나이 상관관계 인사이트 제공
- SNS 팔로워 vs 총관중수 산점도 차트
- 구단 나이 vs 총관중수 산점도 차트
- 연도별 SNS 팔로워 & 관중수 트렌드 차트
- 분석 결과 및 해설 제공

### 야구 경기 일정

- 야구 경기 일정 제공

### 야구 직관 팬 성향 분석

- 다양한 선택지에 따른 팬성향 결과지 도출
- 유저 선택에 따른 구장, 좌석, 맛집 추천

---

## 시작 방법

- 하단 탭 별로 인사이트 분리

1. 승률-관중수 상관관계
2. SNS 팔로워 vs 관중수
3. 야구 경기 일정
4. 야구 직관 팬성향 분석

---

## 사용 환경

- 웹 브라우저, 모바일

---

# 개발자 가이드 (Developer Guide)

## 기술 스택

- **Language**: Python
- **Frontend**: Streamlit
- **Deployment**: git, pandas, requests, selenium, seaborn, python-dotenv

---

## 주요 API 명세 (간단 요약)

| 리소스           | 메서드/엔드포인트                  | 설명             |
| ---------------- | ---------------------------------- | ---------------- |
| Kakao Map search | GET /v2/local/search/keyword.json  | 카카오 장소 검색 |
| Weather          | GET /api.weatherapi.com/v1/current | 날씨 조회        |

---

## 페이지 구조 (탭으로 구분)

<pre>
/pages
  ├── login.js
  ├── main.js
  ├── mypage.js
  ├── record.js
  ├── timer.js </pre>

> **css는 `assets/styles` 폴더에서, 이미지들은 `public` 폴더에 넣고 사용**

---

## 사용한 오픈소스

- Streamlit: ui 개발 및 클라이언트 서버 배포

- Pandas: 데이터 전처리, 로직 개발

- Selenium, Requests : 데이터 크롤링

- seaborn : 시각적인 다양한 차트

- python : 주 사용 언어

- git : 프로젝트 코드 관리 및 협업

---

## 배포 환경

- streamlit 클라이언트 서버

---

## 협업 방식

- **포크(Fork) 기반 협업**: 메인 리포지토리를 포크하여 개발합니다.
- 개발 완료 후, **Pull Request(PR)** 를 생성합니다.
- PR에 대해 **코드 리뷰**가 진행됩니다.
- 리뷰 승인 후, **Main Repository에 Merge** 됩니다.

---

## 커밋 컨벤션

커밋 메시지는 아래 컨벤션을 따릅니다:

- feat: 유저 로그인 기능 추가
- fix: 로그인 시 비밀번호 오류 해결
- docs: 환경설정 가이드 추가
- refactor(api): API 요청 방식 개선
- chore: 패키지 정리 및 의존성 업데이트

---

## 프로젝트 기본 폴더 구조

```
.
├── README.md
├── app
│ ├── \__init_.py
│ ├── components
│ └── *_screen.py
├── apis : 리소스 폴더
├── aseets : 리소스 폴더
├── models : 데이터 모델링
├── data : 데이터 저장소
├── requirements.txt : 사용 라이브러리 명시
├── scraper : 크롤링 로직
├── features : 기능
├── main.py : streamlit 진입점
└── libs : util 함수

```

## 네이밍 규칙

- 파일 네임, 변수, 함수 : snake_case
- 클래스: PascalCase
- 상수: ALL_CAPS

---

## 커밋 메세지 prefix

- feature/ : 새로운 기능 설명
- fix/ : 버그 수정
- refactor/ : 코드 리팩토링 (기능 변화 없음)
- chore/ : 환경 설정, 패키지, 문서 등
- docs/ : 문서 관련 수정
