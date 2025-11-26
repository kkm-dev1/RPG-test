# 🚀 GitHub Pages 배포 가이드

## ⚠️ 중요 사항

**현재 상태로는 소스 코드만 있어서 웹에서 직접 실행할 수 없습니다!**

빌드를 먼저 해야 웹 파일들이 생성됩니다. 아래 방법 중 하나를 선택하세요.

---

## 방법 1: 수동 빌드 후 업로드 (간단)

### 1단계: 로컬에서 빌드

터미널에서 다음 명령어 실행:

```bash
pygbag --build main.py
```

이 명령어가 `build/web/` 폴더에 웹 파일들을 생성합니다.

### 2단계: GitHub 저장소 생성

1. GitHub에 새 저장소 생성 (예: `rpg-game`)
2. 저장소를 로컬에 클론:
   ```bash
   git clone https://github.com/당신의사용자명/rpg-game.git
   cd rpg-game
   ```

### 3단계: 빌드된 파일 복사

`build/web/` 폴더의 **모든 내용**을 저장소의 `docs/` 폴더로 복사:

```bash
# docs 폴더 생성
mkdir docs

# build/web의 모든 내용을 docs로 복사
xcopy /E /I build\web docs
```

또는 수동으로 `build/web/` 안의 모든 파일을 `docs/` 폴더로 복사

### 4단계: GitHub에 업로드

```bash
git add .
git commit -m "웹 게임 배포"
git push origin main
```

### 5단계: GitHub Pages 활성화

1. GitHub 저장소 페이지에서 **Settings** 클릭
2. 왼쪽 메뉴에서 **Pages** 선택
3. **Source** 섹션에서:
   - Branch: `main` (또는 `master`)
   - Folder: `/docs` 선택
4. **Save** 클릭

### 6단계: 접속

몇 분 후 다음 주소로 접속:
```
https://당신의사용자명.github.io/rpg-game/
```

---

## 방법 2: GitHub Actions로 자동 배포 (권장)

코드를 push할 때마다 자동으로 빌드하고 배포됩니다!

### 1단계: GitHub Actions 워크플로우 파일 생성

프로젝트에 `.github/workflows/deploy.yml` 파일을 생성:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Build with pygbag
        run: pygbag --build main.py
      
      - name: Setup Pages
        uses: actions/configure-pages@v3
      
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: './build/web'
      
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

### 2단계: GitHub 저장소 설정

1. 저장소의 **Settings** > **Pages**로 이동
2. **Source**를 "GitHub Actions"로 선택
3. 저장

### 3단계: 코드 Push

```bash
git add .
git commit -m "GitHub Actions 배포 설정"
git push origin main
```

### 4단계: 자동 배포 확인

1. GitHub 저장소의 **Actions** 탭에서 배포 진행 상황 확인
2. 완료되면 `https://당신의사용자명.github.io/저장소명/` 접속

---

## 📁 프로젝트 구조 (방법 1 사용 시)

```
rpg-game/
├── .github/
│   └── workflows/
│       └── deploy.yml          # (방법 2만 사용)
├── docs/                       # 빌드된 웹 파일들 (방법 1)
│   ├── index.html
│   ├── main.py
│   └── ... (기타 웹 파일들)
├── main.py                     # 원본 소스 코드
├── requirements.txt
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## 🔧 .gitignore 파일 생성 (중요!)

빌드 파일과 불필요한 파일들을 제외하려면 `.gitignore` 파일을 생성하세요:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv

# Build files (방법 1 사용 시)
build/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

---

## ✅ 체크리스트

- [ ] `pygbag` 설치됨 (`pip install pygbag`)
- [ ] 빌드 완료 (`pygbag --build main.py`)
- [ ] GitHub 저장소 생성
- [ ] 빌드된 파일 업로드 (방법 1) 또는 Actions 설정 (방법 2)
- [ ] GitHub Pages 활성화
- [ ] 웹 주소로 접속 확인

---

## 🐛 문제 해결

### "빌드 오류가 발생합니다"

```bash
# pygbag 최신 버전으로 업그레이드
pip install --upgrade pygbag

# 캐시 정리 후 재빌드
pygbag --build --no-cache main.py
```

### "GitHub Pages가 동작하지 않습니다"

1. **파일 경로 확인**: `docs/index.html` 파일이 있는지 확인
2. **브랜치 확인**: Settings > Pages에서 올바른 브랜치 선택
3. **대기 시간**: GitHub Pages 활성화 후 5-10분 정도 걸릴 수 있음
4. **브라우저 캐시**: Ctrl+F5로 하드 리프레시

### "404 오류가 발생합니다"

- 저장소 이름과 URL이 일치하는지 확인
- `docs/` 폴더에 `index.html`이 있는지 확인
- GitHub Actions를 사용하는 경우 Actions 탭에서 오류 확인

---

## 💡 추천

**방법 2 (GitHub Actions)**를 추천합니다:
- ✅ 코드 수정 후 push만 하면 자동 배포
- ✅ 빌드 파일을 수동으로 관리할 필요 없음
- ✅ CI/CD 파이프라인 구축 가능

방법 1은 간단하지만, 코드를 수정할 때마다 수동으로 빌드하고 업로드해야 합니다.

---

## 📝 참고

- GitHub Pages는 무료로 제공됩니다
- 저장소를 Public으로 설정해야 무료 사용 가능
- Private 저장소는 GitHub Pro가 필요하지만, GitHub Actions는 무료로 사용 가능

