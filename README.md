# 데이터 분석가 포트폴리오

https://njinkim.github.io/data-analyst-portfolio/
프로젝트 상세 페이지 기능을 포함하여 각 프로젝트의 자세한 내용을 확인할 수 있습니다.

## 📁 파일 구조

```
portfolio/
├── index.html              # 메인 페이지
├── styles.css              # 메인 페이지 스타일
├── script.js               # 메인 페이지 JavaScript
├── project-detail.css      # 프로젝트 상세 페이지 스타일
├── project-detail.js       # 프로젝트 상세 페이지 JavaScript
├── project1.html           
├── project2.html           
├── project3.html           
├── project4.html           
├── project5.html           
├── project6.html           
└── README.md               # 프로젝트 설명서
```


## 🛠️ 사용법

### 로컬에서 실행
1. 모든 파일을 웹 서버에 업로드
2. `index.html` 파일을 브라우저에서 열기
3. 프로젝트 카드를 클릭하여 상세 페이지 확인


### 내용 수정 방법
1. **개인 정보 수정**: `index.html`의 이름, 연락처, 소개 내용 수정
2. **프로젝트 내용 수정**: 각 `project*.html` 파일의 내용 수정
3. **스타일 수정**: `styles.css`와 `project-detail.css`에서 색상, 폰트 등 수정

## 🚀 배포 방법

### GitHub Pages
1. GitHub 저장소 생성
2. 파일 업로드
3. Settings > Pages에서 배포 설정

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

```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
```
