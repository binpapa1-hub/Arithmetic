# 콘솔 → PyQt GUI 리팩토링 계획서

## 1단계: 현재 코드 분석 및 스멜 식별

### 1.1 코드 스멜 분석

#### console_app.py의 문제점

| 스멜 유형 | 위치 | 문제점 | 영향도 |
|----------|------|--------|--------|
| **Long Method** | `main()` 함수 | 입력/출력/계산 로직이 모두 한 함수에 집중 | 높음 |
| **Feature Envy** | 연산자 처리 | `Arithmetic` 클래스의 메서드를 직접 호출하는 if-elif 체인 | 중간 |
| **Magic String** | 연산자 비교 | `"+", "-", "*", "/"` 하드코딩 | 낮음 |
| **Missing Error Handling** | 입력 처리 | `int()` 변환 시 ValueError 미처리 | 높음 |
| **Tight Coupling** | 전체 | UI와 비즈니스 로직이 강하게 결합 | 높음 |

#### SOLID 원칙 위반 사항

1. **SRP (Single Responsibility Principle) 위반**
   - `main()` 함수가 입력, 출력, 계산 로직을 모두 담당

2. **OCP (Open/Closed Principle) 위반**
   - 새로운 연산자 추가 시 `main()` 함수 수정 필요

3. **DIP (Dependency Inversion Principle) 위반**
   - 구체적인 `Arithmetic` 클래스에 직접 의존

---

## 2단계: 아키텍처 설계

### 2.1 설계 패턴: MVP (Model-View-Presenter)

```
┌─────────────────────────────────────────┐
│           View (PyQt GUI)               │
│  - CalculatorWindow (QMainWindow)      │
│  - DisplayWidget (QLabel)              │
│  - ButtonGrid (QGridLayout)             │
└──────────────┬──────────────────────────┘
               │ 이벤트 전달
               ▼
┌─────────────────────────────────────────┐
│         Presenter (Controller)          │
│  - CalculatorPresenter                  │
│  - 버튼 클릭 처리                        │
│  - 계산 로직 호출                        │
└──────────────┬──────────────────────────┘
               │ 계산 요청
               ▼
┌─────────────────────────────────────────┐
│         Model (Business Logic)          │
│  - CalculatorService                    │
│  - Arithmetic (기존)                    │
└─────────────────────────────────────────┘
```

### 2.2 클래스 구조

```
src/
├── arithmetic.py          # 기존 (변경 없음)
├── calculator_service.py  # 새로 생성 (비즈니스 로직)
├── calculator_presenter.py # 새로 생성 (프레젠터)
└── gui/
    ├── __init__.py
    ├── calculator_window.py  # 메인 윈도우
    ├── display_widget.py     # 결과 표시 위젯
    └── button_factory.py     # 버튼 생성 팩토리
```

---

## 3단계: 비즈니스 로직 분리 (CalculatorService)

### 3.1 CalculatorService 설계

**책임:**
- 연산자 문자열을 Arithmetic 메서드로 매핑
- 계산 실행 및 예외 처리
- 계산 이력 관리 (선택사항)

**SOLID 적용:**
- **SRP**: 계산 로직만 담당
- **OCP**: Strategy 패턴으로 연산자 확장 가능
- **DIP**: Arithmetic에 의존하되 인터페이스로 추상화

---

## 4단계: PyQt GUI 구현

### 4.1 UI 구성 요소

1. **CalculatorWindow (QMainWindow)**
   - 메인 윈도우
   - 레이아웃 관리

2. **DisplayWidget (QLabel)**
   - 입력값 및 결과 표시
   - 폰트 스타일링

3. **ButtonGrid (QGridLayout)**
   - 4x4 그리드 레이아웃
   - 숫자 버튼 (0-9)
   - 연산자 버튼 (+, -, ×, /)
   - 기능 버튼 (+, -, ., =)

### 4.2 이벤트 처리 흐름

```
사용자 버튼 클릭
    ↓
CalculatorWindow.button_clicked()
    ↓
CalculatorPresenter.handle_input()
    ↓
CalculatorService.calculate()
    ↓
Arithmetic 메서드 호출
    ↓
결과 반환
    ↓
DisplayWidget.update()
```

---

## 5단계: 구현 단계별 작업

### Phase 1: CalculatorService 구현
- [ ] `calculator_service.py` 생성
- [ ] 연산자 매핑 딕셔너리
- [ ] 계산 메서드 구현
- [ ] 예외 처리 추가
- [ ] 단위 테스트 작성

### Phase 2: Presenter 구현
- [ ] `calculator_presenter.py` 생성
- [ ] 상태 관리 (현재 입력값, 연산자, 이전 값)
- [ ] 버튼 입력 처리 로직
- [ ] 계산 트리거 로직

### Phase 3: GUI 컴포넌트 구현
- [ ] `calculator_window.py` - 메인 윈도우
- [ ] `display_widget.py` - 디스플레이
- [ ] `button_factory.py` - 버튼 생성
- [ ] 레이아웃 구성

### Phase 4: 통합 및 테스트
- [ ] 전체 통합 테스트
- [ ] UI 테스트 (선택사항)
- [ ] 사용자 시나리오 테스트

---

## 6단계: 코드 품질 개선

### 6.1 정적 분석 도구

```bash
# pylint 사용
pylint src/gui/*.py

# mypy 타입 체크
mypy src/gui/*.py

# flake8 스타일 체크
flake8 src/gui/*.py
```

### 6.2 개선 사항

1. **타입 힌트 추가**
   ```python
   def calculate(self, a: float, operator: str, b: float) -> float:
   ```

2. **상수 분리**
   ```python
   class Operators:
       ADD = "+"
       SUBTRACT = "-"
       MULTIPLY = "×"
       DIVIDE = "/"
   ```

3. **에러 메시지 상수화**
   ```python
   class ErrorMessages:
       DIVISION_BY_ZERO = "0으로 나눌 수 없습니다."
   ```

---

## 7단계: 의존성 관리

### requirements.txt 업데이트

```
pytest>=7.0.0
pytest-cov>=7.0.0
PyQt6>=6.6.0
pylint>=3.0.0
mypy>=1.7.0
flake8>=6.1.0
```

---

## 8단계: 테스트 전략

### 8.1 단위 테스트
- CalculatorService 테스트
- CalculatorPresenter 테스트
- Arithmetic 테스트 (기존 유지)

### 8.2 통합 테스트
- 전체 계산 플로우 테스트
- 예외 처리 테스트

### 8.3 UI 테스트 (선택사항)
- QTest를 사용한 버튼 클릭 시뮬레이션

---

## 9단계: 문서화

### 9.1 코드 문서화
- Docstring 추가
- 타입 힌트 명시

### 9.2 사용자 가이드
- GUI 사용법 문서
- 스크린샷 포함

---

## 10단계: 배포 준비

### 10.1 실행 파일 생성 (선택사항)
- PyInstaller로 .exe 생성
- 또는 Python 스크립트로 실행

### 10.2 README 업데이트
- GUI 실행 방법 추가
- 스크린샷 추가

---

## 예상 결과물

### 파일 구조
```
src/
├── arithmetic.py              # 기존 (변경 없음)
├── calculator_service.py      # 새로 생성
├── calculator_presenter.py    # 새로 생성
├── console_app.py             # 기존 (유지)
└── gui/
    ├── __init__.py
    ├── calculator_window.py
    ├── display_widget.py
    └── button_factory.py

tests/
├── test_arithmetic.py         # 기존
├── test_calculator_service.py # 새로 생성
└── test_calculator_presenter.py # 새로 생성

main.py                        # GUI 실행 진입점
```

### 실행 방법
```bash
# GUI 실행
python main.py

# 콘솔 실행 (기존 유지)
python src/console_app.py
```

---

## SOLID 원칙 적용 요약

| 원칙 | 적용 방법 |
|------|----------|
| **SRP** | 각 클래스가 단일 책임만 가짐 (View, Presenter, Service 분리) |
| **OCP** | Strategy 패턴으로 연산자 확장 가능 |
| **LSP** | 인터페이스 일관성 유지 |
| **ISP** | 필요한 메서드만 노출 |
| **DIP** | 구체 클래스가 아닌 추상화에 의존 |

---

**작성일**: 2025-12-16  
**버전**: v1.0

