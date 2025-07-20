# 데이터 분석가 포트폴리오

3년 경력의 데이터 분석가를 위한 반응형 웹 포트폴리오입니다. 프로젝트 상세 페이지 기능을 포함하여 각 프로젝트의 자세한 내용을 확인할 수 있습니다.

## 🚀 주요 기능

### 메인 페이지
- **반응형 디자인**: 모바일과 데스크톱에서 최적화된 레이아웃
- **8개 섹션**: 표지부, 소개, 목차, 경력, 프로젝트, 기술, 기타 기술, 교육
- **인터랙티브 네비게이션**: 부드러운 스크롤과 현재 섹션 하이라이트
- **프로젝트 카드 호버 효과**: 마우스 오버 시 상세보기 표시

### 프로젝트 상세 페이지
- **5개 프로젝트 상세 페이지**: 각 프로젝트별 전용 페이지
- **PPT 1-2장 분량**: 스크롤 가능한 상세 내용
- **이미지 첨부 기능**: 프로젝트 관련 이미지 추가 가능
- **홈으로 돌아가기 버튼**: 우측 상단 고정 버튼

## 📁 파일 구조

```
portfolio/
├── index.html              # 메인 페이지
├── styles.css              # 메인 페이지 스타일
├── script.js               # 메인 페이지 JavaScript
├── project-detail.css      # 프로젝트 상세 페이지 스타일
├── project-detail.js       # 프로젝트 상세 페이지 JavaScript
├── project1.html           # 데이터 마트 구성 프로젝트
├── project2.html           # 크롤러 개발 프로젝트
├── project3.html           # Tableau 대시보드 프로젝트
├── project4.html           # 예측 모델 개발 프로젝트
├── project5.html           # 지표 개발 프로젝트
└── README.md               # 프로젝트 설명서
```

## 🎨 프로젝트 예시

### 1. 데이터 마트 구성 및 업데이트 관리
- **기술**: Apache Airflow, Python, PostgreSQL
- **성과**: 데이터 업데이트 시간 87.5% 단축
- **내용**: 대시보드 일일 지표 관리를 위한 데이터 파이프라인 구축

### 2. 크롤러 개발
- **기술**: Python, Selenium, BeautifulSoup
- **성과**: 데이터 수집 시간 93.8% 단축
- **내용**: 네이버 뉴스, 블로그, 카페 수집 및 트렌드 분석

### 3. Tableau 대시보드 구성
- **기술**: Tableau, SQL, Python
- **성과**: 의사결정 시간 75% 단축
- **내용**: 실시간 데이터 시각화 및 의사결정 지원

### 4. 예측 모델 개발
- **기술**: Python, R, TensorFlow, Scikit-learn
- **성과**: 지원수 예측 92% 정확도
- **내용**: Zero-inflated Poisson Regression과 LSTM 활용

### 5. 지표 개발
- **기술**: Python, R, SQL, Tableau
- **성과**: 운영 효율성 15% 개선
- **내용**: 지원자 대 보호자 비율 등 핵심 KPI 개발

## 🛠️ 사용법

### 로컬에서 실행
1. 모든 파일을 웹 서버에 업로드
2. `index.html` 파일을 브라우저에서 열기
3. 프로젝트 카드를 클릭하여 상세 페이지 확인

### 이미지 추가 방법
각 프로젝트 상세 페이지의 이미지 플레이스홀더를 실제 이미지로 교체:

```html
<!-- 이미지 플레이스홀더 -->
<div class="image-placeholder">
    <i class="fas fa-chart-line"></i>
    <p>프로젝트 개요 다이어그램</p>
</div>

<!-- 실제 이미지로 교체 -->
<img src="images/project-overview.png" alt="프로젝트 개요 다이어그램" class="project-image">
```

### 내용 수정 방법
1. **개인 정보 수정**: `index.html`의 이름, 연락처, 소개 내용 수정
2. **프로젝트 내용 수정**: 각 `project*.html` 파일의 내용 수정
3. **스타일 수정**: `styles.css`와 `project-detail.css`에서 색상, 폰트 등 수정

## 🎯 주요 특징

### 반응형 디자인
- 모바일, 태블릿, 데스크톱 최적화
- 터치 디바이스 지원
- 유연한 그리드 레이아웃

### 인터랙티브 기능
- 부드러운 스크롤 애니메이션
- 프로젝트 카드 호버 효과
- 스킬 바 애니메이션
- 모바일 햄버거 메뉴

### 접근성
- 키보드 네비게이션 지원
- 스크린 리더 호환
- 색상 대비 최적화

## 🚀 배포 방법

### GitHub Pages
1. GitHub 저장소 생성
2. 파일 업로드
3. Settings > Pages에서 배포 설정

### Netlify
1. Netlify 계정 생성
2. 파일 드래그 앤 드롭 또는 Git 연결
3. 자동 배포 완료

### Vercel
1. Vercel 계정 생성
2. Git 저장소 연결
3. 자동 배포 설정

## 📱 브라우저 지원

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 🔧 커스터마이징

### 색상 변경
`styles.css`의 CSS 변수 수정:

```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
}
```

### 폰트 변경
Google Fonts 또는 웹 폰트 추가:

```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
```

### 새로운 프로젝트 추가
1. `project6.html` 파일 생성
2. 기존 프로젝트 페이지 구조 복사
3. `index.html`에 프로젝트 카드 추가
4. `script.js`에서 클릭 이벤트 연결

## 📞 문의

포트폴리오 관련 문의사항이 있으시면 언제든 연락주세요.

---

© 2024 데이터 분석가 포트폴리오. All rights reserved. 