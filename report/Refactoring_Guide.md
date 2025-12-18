# 리팩토링 가이드

## 리팩토링이란?

리팩토링(Refactoring)은 **코드의 외부 동작은 변경하지 않고 내부 구조를 개선**하는 작업입니다.

**핵심 원칙:**
- ✅ 기능은 그대로 유지
- ✅ 테스트는 계속 통과해야 함
- ✅ 코드 품질 향상

---

## 현재 프로젝트 리팩토링 상태

### ✅ 완료된 리팩토링

1. **PyQt GUI 리팩토링** (완료)
   - MVP 패턴 적용
   - 비즈니스 로직 분리 (CalculatorService)
   - UI와 로직 분리 (Presenter)

2. **SOLID 원칙 적용** (완료)
   - SRP: 각 클래스 단일 책임
   - OCP: Strategy 패턴으로 확장 가능
   - DIP: 인터페이스 기반 의존성

### ⚠️ 추가 리팩토링 필요 영역

1. **console_app.py** - 아직 리팩토링 필요
2. **코드 품질 개선** - 상수 분리, 타입 힌트 강화
3. **테스트 커버리지** - GUI/Presenter 테스트 추가

---

## 리팩토링 절차 (5단계)

### Step 1: 현재 상태 분석

```bash
# 1. 코드 스멜 확인
pylint src/ --score=y

# 2. 테스트 실행 (기능 정상 확인)
pytest tests/ -v

# 3. 커버리지 확인
pytest --cov=src --cov-report=term-missing tests/
```

**체크리스트:**
- [ ] 현재 기능 정상 동작 확인
- [ ] 테스트 모두 통과
- [ ] 코드 스멜 식별

### Step 2: 리팩토링 목표 설정

**예시 목표:**
- console_app.py 리팩토링
- Magic String 제거
- 에러 처리 개선
- 타입 힌트 추가

### Step 3: 작은 단위로 리팩토링

**원칙:**
- 한 번에 하나씩
- 작은 변경
- 테스트 실행 확인

### Step 4: 테스트 실행

```bash
# 리팩토링 후 반드시 테스트
pytest tests/ -v
```

**체크리스트:**
- [ ] 모든 테스트 통과
- [ ] 기능 정상 동작
- [ ] 성능 저하 없음

### Step 5: 코드 리뷰 및 문서화

- [ ] 변경 사항 문서화
- [ ] 코드 리뷰
- [ ] 커밋 메시지 작성

---

## 리팩토링 예시: console_app.py 개선

### 현재 코드 문제점

```python
# console_app.py (현재)
def main():
    print("입력화면")
    a = int(input("첫번째 정수값>>"))
    operator = input("연산자>>")
    b = int(input("두번째 정수값>"))
    
    if operator == "+":
        result = Arithmetic.add(a, b)
    elif operator == "-":
        result = Arithmetic.subtract(a, b)
    # ... if-elif 체인
```

**문제점:**
- Long Method (하나의 함수에 모든 로직)
- Feature Envy (Arithmetic 직접 호출)
- Magic String (연산자 하드코딩)
- Missing Error Handling (ValueError 미처리)

### 리팩토링 후 코드

```python
# console_app.py (개선)
from src.calculator_service import CalculatorService

def get_input(prompt: str) -> str:
    """사용자 입력 받기"""
    return input(prompt)

def get_integer_input(prompt: str) -> int:
    """정수 입력 받기 (에러 처리 포함)"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("올바른 정수를 입력해주세요.")

def display_result(a: int, operator: str, b: int, result: float):
    """결과 표시"""
    print("결과 뷰 화면")
    print("=" * 30)
    print(f"{a} {operator} {b}을 계산합니다.")
    print("=" * 30)
    print(f"{a}{operator}{b}={result}입니다.")

def main():
    """메인 함수"""
    print("입력화면\n")
    
    a = get_integer_input("첫번째 정수값>> ")
    operator = get_input("연산자>> ")
    b = get_integer_input("두번째 정수값>> ")
    
    try:
        result = CalculatorService.calculate(a, operator, b)
        display_result(a, operator, b, result)
    except (ValueError, ArithmeticError) as e:
        print(f"오류: {e}")
```

**개선 사항:**
- ✅ 함수 분리 (SRP)
- ✅ CalculatorService 사용 (DIP)
- ✅ 에러 처리 추가
- ✅ 타입 힌트 추가

---

## 리팩토링 체크리스트

### 코드 품질 개선

- [ ] **Magic String 제거**
  ```python
  # Before
  if operator == "+":
  
  # After
  class Operators:
      ADD = "+"
  if operator == Operators.ADD:
  ```

- [ ] **타입 힌트 추가**
  ```python
  # Before
  def calculate(a, operator, b):
  
  # After
  def calculate(a: float, operator: str, b: float) -> float:
  ```

- [ ] **상수 분리**
  ```python
  # Before
  print("=" * 30)
  
  # After
  SEPARATOR_LENGTH = 30
  print("=" * SEPARATOR_LENGTH)
  ```

- [ ] **에러 메시지 상수화**
  ```python
  # Before
  print("0으로 나눌 수 없습니다.")
  
  # After
  class ErrorMessages:
      DIVISION_BY_ZERO = "0으로 나눌 수 없습니다."
  print(ErrorMessages.DIVISION_BY_ZERO)
  ```

### 아키텍처 개선

- [ ] **의존성 주입 (Dependency Injection)**
- [ ] **인터페이스 추상화**
- [ ] **팩토리 패턴 적용**

### 테스트 개선

- [ ] **테스트 커버리지 100%**
- [ ] **통합 테스트 추가**
- [ ] **UI 테스트 추가**

---

## 리팩토링 실행 가이드

### 1. console_app.py 리팩토링

**목표:** CalculatorService 사용, 에러 처리 개선

```bash
# 1. 현재 테스트 실행 (베이스라인)
pytest tests/ -v

# 2. console_app.py 수정
# (위의 리팩토링 예시 참고)

# 3. 테스트 재실행
pytest tests/ -v

# 4. 수동 테스트
python src/console_app.py
```

### 2. 코드 품질 개선

```bash
# 1. pylint 실행
pylint src/ --score=y

# 2. 문제점 수정
# (Magic String, 타입 힌트 등)

# 3. 재검사
pylint src/ --score=y
```

### 3. 테스트 커버리지 개선

```bash
# 1. 커버리지 확인
pytest --cov=src --cov-report=html tests/

# 2. 누락된 부분 식별
# (calculator_presenter.py, gui/*.py)

# 3. 테스트 추가
# tests/test_calculator_presenter.py 생성

# 4. 재확인
pytest --cov=src --cov-report=term-missing tests/
```

---

## 리팩토링 시 주의사항

### ✅ DO (해야 할 것)

1. **작은 단위로 리팩토링**
   - 한 번에 하나의 스멜만 해결
   - 테스트 실행 후 다음 단계 진행

2. **테스트 먼저 작성**
   - 리팩토링 전 테스트 작성
   - 리팩토링 후 테스트 통과 확인

3. **기능 유지**
   - 외부 동작 변경 없음
   - 사용자 경험 동일

4. **문서화**
   - 변경 사항 기록
   - 리팩토링 이유 명시

### ❌ DON'T (하지 말아야 할 것)

1. **기능 추가와 동시에 리팩토링**
   - 리팩토링과 기능 추가 분리

2. **대규모 변경**
   - 한 번에 너무 많은 변경

3. **테스트 없이 리팩토링**
   - 테스트 없이는 위험

4. **성능 저하**
   - 리팩토링 후 성능 확인

---

## 리팩토링 우선순위

### 높은 우선순위 (High Priority)

1. **console_app.py 리팩토링**
   - CalculatorService 사용
   - 에러 처리 개선
   - 함수 분리

2. **에러 처리 강화**
   - 모든 입력 검증
   - 명확한 에러 메시지

### 중간 우선순위 (Medium Priority)

3. **코드 품질 개선**
   - Magic String 제거
   - 타입 힌트 추가
   - 상수 분리

4. **테스트 커버리지**
   - Presenter 테스트
   - GUI 테스트 (선택사항)

### 낮은 우선순위 (Low Priority)

5. **성능 최적화**
   - 불필요한 연산 제거
   - 메모리 사용 최적화

6. **문서화 개선**
   - Docstring 보완
   - 사용자 가이드 작성

---

## 리팩토링 실행 스크립트

### refactor_check.bat

```batch
@echo off
echo ========================================
echo 리팩토링 전 체크
echo ========================================
echo.

echo [1/3] 테스트 실행...
pytest tests/ -v
if %errorlevel% neq 0 (
    echo [경고] 테스트 실패 - 리팩토링 전 수정 필요
    pause
    exit /b 1
)

echo [2/3] 코드 품질 확인...
pylint src/ --score=y --disable=import-error

echo [3/3] 커버리지 확인...
pytest --cov=src --cov-report=term-missing tests/

echo.
echo ========================================
echo 리팩토링 준비 완료
echo ========================================
pause
```

---

## 리팩토링 예시 시나리오

### 시나리오 1: console_app.py 리팩토링

**단계:**
1. 현재 코드 분석
2. CalculatorService 사용으로 변경
3. 함수 분리
4. 에러 처리 추가
5. 테스트 실행
6. 수동 테스트

**예상 시간:** 30분

### 시나리오 2: 코드 품질 개선

**단계:**
1. pylint 실행하여 문제점 식별
2. Magic String 상수로 분리
3. 타입 힌트 추가
4. 테스트 실행
5. pylint 재실행

**예상 시간:** 20분

---

## 리팩토링 완료 체크리스트

### 코드 품질
- [ ] pylint 점수 8.0 이상
- [ ] flake8 통과
- [ ] 타입 힌트 명시
- [ ] Magic String 제거

### 아키텍처
- [ ] SOLID 원칙 준수
- [ ] 의존성 분리
- [ ] 패턴 적용 (Strategy, Factory 등)

### 테스트
- [ ] 모든 테스트 통과
- [ ] 커버리지 100% (핵심 로직)
- [ ] 통합 테스트 추가

### 문서화
- [ ] Docstring 완성
- [ ] README 업데이트
- [ ] 변경 사항 기록

---

## 다음 단계

1. **리팩토링 목표 선택**
   - console_app.py 리팩토링 (권장)
   - 코드 품질 개선
   - 테스트 커버리지 개선

2. **리팩토링 실행**
   - 위의 가이드 따라 단계별 실행

3. **검증**
   - 테스트 실행
   - 코드 품질 확인
   - 수동 테스트

---

**작성일**: 2025-12-16  
**버전**: v1.0

