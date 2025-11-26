# RPG 게임 - Web 배포 가이드

이 프로젝트는 pygbag을 사용하여 PC와 모바일 기기에서 모두 실행 가능한 웹 게임입니다.

## 📋 사전 요구사항

- Python 3.8 이상
- pip (Python 패키지 관리자)

## 🚀 설치 방법

### 1. 필요한 패키지 설치

터미널에서 다음 명령어를 실행하여 필요한 패키지를 설치합니다:

```bash
pip install -r requirements.txt
```

또는 개별적으로 설치:

```bash
pip install arcade pygbag
```

## 🎮 실행 방법

### PC에서 로컬 테스트

#### 방법 1: pygbag으로 웹 서버 실행

프로젝트 디렉토리에서 다음 명령어를 실행합니다:

```bash
pygbag main.py
```

이 명령어를 실행하면:
- 웹 브라우저가 자동으로 열립니다
- 로컬 웹 서버가 시작됩니다 (기본 포트: 8000)
- 브라우저에서 게임을 플레이할 수 있습니다

#### 방법 2: 일반 Python 실행 (개발용)

웹 변환 없이 직접 실행하려면:

```bash
python main.py
```

### 모바일에서 실행

#### 방법 1: 같은 네트워크에서 접속

1. PC에서 `pygbag main.py` 실행
2. PC의 IP 주소 확인:
   - Windows: `ipconfig` 명령어 실행 후 IPv4 주소 확인
   - 예: `192.168.0.100:8000`
3. 모바일 기기에서 같은 Wi-Fi 네트워크에 연결
4. 모바일 브라우저에서 `http://PC의IP주소:8000` 접속
   - 예: `http://192.168.0.100:8000`

#### 방법 2: 웹 호스팅 서비스 사용

생성된 파일을 웹 호스팅 서비스에 업로드:

1. **빌드 파일 생성**:
   ```bash
   pygbag --build main.py
   ```

2. **생성된 파일 업로드**:
   - `build/web/` 폴더의 내용을 다음 서비스 중 하나에 업로드:
     - GitHub Pages
     - Netlify
     - Vercel
     - Firebase Hosting

3. **모바일에서 접속**:
   - 업로드된 URL을 모바일 브라우저에서 열기

## 🎯 게임 조작 방법

- **PC**: 방향키 (↑ ↓ ← →)로 플레이어 이동
- **모바일**: 화면 터치로 이동 (추가 구현 필요) 또는 가상 키보드 사용

## 📁 프로젝트 구조

```
RPG/
├── main.py              # 메인 게임 코드
├── requirements.txt     # 필요한 패키지 목록
├── pyproject.toml        # pygbag 설정 파일
└── README.md           # 이 파일
```

## 🔧 문제 해결

### 포트가 이미 사용 중인 경우

다른 포트를 사용하려면:

```bash
pygbag --port 8080 main.py
```

### 빌드 오류가 발생하는 경우

1. Python 버전 확인 (3.8 이상 필요):
   ```bash
   python --version
   ```

2. 패키지 재설치:
   ```bash
   pip install --upgrade arcade pygbag
   ```

3. 캐시 정리:
   ```bash
   pip cache purge
   ```

### 모바일에서 접속이 안 되는 경우

1. PC 방화벽 설정 확인
2. PC와 모바일이 같은 Wi-Fi 네트워크에 연결되어 있는지 확인
3. PC의 IP 주소가 올바른지 확인

## 📝 참고 사항

- pygbag은 Python 코드를 WebAssembly로 변환하여 브라우저에서 실행합니다
- 첫 로딩 시 약간의 시간이 걸릴 수 있습니다
- 모바일에서는 성능이 PC보다 낮을 수 있으므로 최적화가 필요할 수 있습니다
- 일부 브라우저에서는 WebAssembly 지원이 제한적일 수 있습니다 (최신 브라우저 권장)

## 🌐 브라우저 호환성

- Chrome/Edge (권장)
- Firefox
- Safari (iOS 포함)
- 모바일 브라우저 (Chrome, Safari 등)

## 📚 추가 리소스

- [pygbag 공식 문서](https://pygbag.readthedocs.io/)
- [arcade 라이브러리 문서](https://api.arcade.academy/)

