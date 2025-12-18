# 코드 스멜 분석 리포트

**분석 일자**: 2025-12-16  
**분석 대상**: 전체 프로젝트 코드  
**분석 기준**: Martin Fowler의 리팩토링 카탈로그

---

## 전체 요약

| 파일 | 스멜 개수 | 심각도 | 우선순위 |
|------|----------|--------|----------|
| `console_app.py` | 5개 | 높음 | 높음 |
| `arithmetic.py` | 2개 | 낮음 | 낮음 |
| `calculator_service.py` | 1개 | 낮음 | 낮음 |
| `calculator_presenter.py` | 3개 | 중간 | 중간 |
| `calculator_window.py` | 4개 | 중간 | 중간 |
| `button_factory.py` | 2개 | 낮음 | 낮음 |
| `display_widget.py` | 1개 | 낮음 | 낮음 |

**총 스멜**: 18개

---

## 1. console_app.py 분석

### 🔴 심각도: 높음 | 우선순위: 높음

#### 스멜 1: Long Method
**위치**: `main()` 함수 (전체 47줄 중 35줄)  
**문제점**: 입력, 출력, 계산 로직이 모두 한 함수에 집중  
**영향도**: 높음

```python
def main():
    print("입력화면")
    print()
    a = int(input("첫번째 정수값>>"))
    # ... 30줄 이상의 코드
```

**개선 방안**: 함수 분리
- `get_user_input()` - 입력 처리
- `display_result()` - 결과 표시
- `perform_calculation()` - 계산 수행

---

#### 스멜 2: Feature Envy
**위치**: Line 29-36  
**문제점**: `Arithmetic` 클래스의 메서드를 직접 호출하는 if-elif 체인  
**영향도**: 중간

```python
if operator == "+":
    result = Arithmetic.add(a, b)
elif operator == "-":
    result = Arithmetic.subtract(a, b)
# ...
```

**개선 방안**: `CalculatorService` 사용
```python
result = CalculatorService.calculate(a, operator, b)
```

---

#### 스멜 3: Magic String
**위치**: Line 22, 29-36  
**문제점**: 연산자 문자열 하드코딩  
**영향도**: 낮음

```python
print("=" * 30)  # Magic Number
if operator == "+":  # Magic String
```

**개선 방안**: 상수 분리
```python
class Constants:
    SEPARATOR_LENGTH = 30
    OPERATOR_ADD = "+"
```

---

#### 스멜 4: Missing Error Handling
**위치**: Line 11, 17  
**문제점**: `int()` 변환 시 `ValueError` 미처리  
**영향도**: 높음

```python
a = int(input("첫번째 정수값>>"))  # ValueError 가능
```

**개선 방안**: try-except 추가
```python
try:
    a = int(input("첫번째 정수값>>"))
except ValueError:
    print("올바른 정수를 입력해주세요.")
    return
```

---

#### 스멜 5: Missing Type Hints
**위치**: `main()` 함수  
**문제점**: 타입 힌트 없음  
**영향도**: 낮음

```python
def main():  # 타입 힌트 없음
```

**개선 방안**: 타입 힌트 추가
```python
def main() -> None:
```

---

## 2. arithmetic.py 분석

### 🟡 심각도: 낮음 | 우선순위: 낮음

#### 스멜 1: Missing Type Hints
**위치**: 모든 메서드  
**문제점**: 타입 힌트 없음  
**영향도**: 낮음

```python
@staticmethod
def add(a, b):  # 타입 힌트 없음
    return a + b
```

**개선 방안**: 타입 힌트 추가
```python
@staticmethod
def add(a: float, b: float) -> float:
    return a + b
```

---

#### 스멜 2: Duplicate Code
**위치**: `divide()`와 `divide_quotient()`  
**문제점**: 0으로 나누기 체크 중복  
**영향도**: 낮음

```python
def divide(a, b):
    if b == 0:
        raise ArithmeticError("Cannot divide by zero")
    return a // b

def divide_quotient(a, b):
    if b == 0:  # 중복
        raise ArithmeticError("Cannot divide by zero")
    return a / b
```

**개선 방안**: 헬퍼 메서드 추출
```python
@staticmethod
def _check_division_by_zero(b: float) -> None:
    if b == 0:
        raise ArithmeticError("Cannot divide by zero")
```

---

## 3. calculator_service.py 분석

### 🟢 심각도: 낮음 | 우선순위: 낮음

#### 스멜 1: Magic String (약간)
**위치**: Line 13-19  
**문제점**: 연산자 문자열 하드코딩 (다만 Strategy 패턴으로 개선됨)  
**영향도**: 낮음

**현재 상태**: 이미 Strategy 패턴으로 개선되어 있으나, 상수로 분리 가능

**개선 방안** (선택사항):
```python
class Operators:
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "×"
    DIVIDE = "/"
```

---

## 4. calculator_presenter.py 분석

### 🟡 심각도: 중간 | 우선순위: 중간

#### 스멜 1: Missing Type Hints
**위치**: `__init__()` 메서드  
**문제점**: `view` 파라미터 타입 힌트 없음  
**영향도**: 중간

```python
def __init__(self, view):  # 타입 힌트 없음
```

**개선 방안**: 타입 힌트 추가
```python
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.gui.calculator_window import CalculatorWindow

def __init__(self, view: 'CalculatorWindow'):
```

---

#### 스멜 2: Magic String
**위치**: Line 77, 111  
**문제점**: 에러 메시지 하드코딩  
**영향도**: 낮음

```python
if self.state.current_value.startswith("-"):
    # ...
self.view.show_error("0으로 나눌 수 없습니다.")
```

**개선 방안**: 상수 분리
```python
class ErrorMessages:
    DIVISION_BY_ZERO = "0으로 나눌 수 없습니다."
```

---

#### 스멜 3: Long Method (약간)
**위치**: `_perform_calculation()` 메서드  
**문제점**: 메서드가 약간 길지만 기능적으로는 적절  
**영향도**: 낮음

**현재 상태**: 크게 문제되지 않으나, 포맷팅 로직 분리 가능

---

## 5. calculator_window.py 분석

### 🟡 심각도: 중간 | 우선순위: 중간

#### 스멜 1: Long Method
**위치**: `_create_buttons()` 메서드  
**문제점**: 버튼 생성 로직이 길고 복잡  
**영향도**: 중간

**개선 방안**: 버튼 타입별 메서드 분리
```python
def _create_number_button(self, text: str, row: int, col: int):
    # ...

def _create_operator_button(self, text: str, row: int, col: int):
    # ...
```

---

#### 스멜 2: Magic String
**위치**: Line 22, 46-57, 72  
**문제점**: 윈도우 크기, 버튼 텍스트 하드코딩  
**영향도**: 낮음

```python
self.setFixedSize(300, 450)  # Magic Number
("7", 0, 0), ("8", 0, 1), ...  # Magic String
```

**개선 방안**: 상수 분리
```python
class WindowConstants:
    WIDTH = 300
    HEIGHT = 450
```

---

#### 스멜 3: Complex Conditional
**위치**: Line 69-85  
**문제점**: if-elif 체인이 복잡  
**영향도**: 낮음

**개선 방안**: Strategy 패턴 또는 딕셔너리 매핑
```python
BUTTON_HANDLERS = {
    'number': lambda text: self.presenter.handle_number_input(text),
    'operator': lambda text: self.presenter.handle_operator_input(text),
    # ...
}
```

---

#### 스멜 4: Magic Number
**위치**: Line 22, 92  
**문제점**: 윈도우 크기, 버튼 위치 하드코딩  
**영향도**: 낮음

```python
self.setFixedSize(300, 450)
layout.addWidget(clear_button, 4, 2, 1, 2)
```

**개선 방안**: 상수 분리

---

## 6. button_factory.py 분석

### 🟢 심각도: 낮음 | 우선순위: 낮음

#### 스멜 1: Duplicate Code
**위치**: 모든 메서드  
**문제점**: 스타일시트 코드 중복  
**영향도**: 낮음

**개선 방안**: 공통 스타일 메서드 추출
```python
@staticmethod
def _apply_base_style(button: QPushButton, bg_color: str, hover_color: str):
    button.setStyleSheet(f"""
        QPushButton {{
            background-color: {bg_color};
            ...
        }}
    """)
```

---

#### 스멜 2: Magic String (CSS)
**위치**: 모든 스타일시트  
**문제점**: 색상 코드 하드코딩  
**영향도**: 낮음

**개선 방안**: 색상 상수 분리
```python
class Colors:
    NUMBER_BG = "#f0f0f0"
    OPERATOR_BG = "#ff9500"
    # ...
```

---

## 7. display_widget.py 분석

### 🟢 심각도: 낮음 | 우선순위: 낮음

#### 스멜 1: Magic String (CSS)
**위치**: Line 26-35  
**문제점**: 스타일시트 하드코딩  
**영향도**: 낮음

**개선 방안**: 스타일 상수 분리 (선택사항)

---

## 우선순위별 리팩토링 계획

### 🔴 높은 우선순위 (High Priority)

1. **console_app.py 리팩토링**
   - [ ] 함수 분리 (Long Method 해결)
   - [ ] CalculatorService 사용 (Feature Envy 해결)
   - [ ] 에러 처리 추가 (Missing Error Handling 해결)
   - **예상 시간**: 30분

### 🟡 중간 우선순위 (Medium Priority)

2. **타입 힌트 추가**
   - [ ] arithmetic.py
   - [ ] calculator_presenter.py
   - [ ] calculator_window.py
   - **예상 시간**: 20분

3. **Magic String/Number 제거**
   - [ ] 상수 클래스 생성
   - [ ] 하드코딩된 값 상수로 변경
   - **예상 시간**: 30분

4. **calculator_window.py 개선**
   - [ ] 버튼 생성 메서드 분리
   - [ ] 복잡한 조건문 단순화
   - **예상 시간**: 20분

### 🟢 낮은 우선순위 (Low Priority)

5. **중복 코드 제거**
   - [ ] arithmetic.py의 0 체크 로직
   - [ ] button_factory.py의 스타일 중복
   - **예상 시간**: 15분

6. **CSS 상수 분리**
   - [ ] 색상 상수
   - [ ] 스타일 상수
   - **예상 시간**: 15분

---

## SOLID 원칙 위반 분석

### ✅ 잘 지켜진 부분

- **SRP**: 대부분의 클래스가 단일 책임을 가짐
- **OCP**: CalculatorService의 Strategy 패턴
- **DIP**: 인터페이스 기반 의존성

### ⚠️ 개선 필요 부분

- **console_app.py**: SRP 위반 (여러 책임)
- **타입 힌트**: 일부 메서드에 타입 힌트 부족

---

## 코드 품질 메트릭

| 메트릭 | 현재 값 | 목표 값 | 상태 |
|--------|---------|---------|------|
| 테스트 커버리지 | 15% (핵심 로직 100%) | 100% (핵심 로직) | ✅ |
| 타입 힌트 비율 | 약 40% | 100% | ⚠️ |
| 코드 중복 | 낮음 | 낮음 | ✅ |
| 순환 복잡도 | 낮음 | 낮음 | ✅ |
| 평균 메서드 길이 | 적절 | 적절 | ✅ |

---

## 리팩토링 실행 가이드

### 1단계: console_app.py 리팩토링 (최우선)

```bash
# 1. 현재 테스트 실행
pytest tests/ -v

# 2. console_app.py 수정
# (함수 분리, CalculatorService 사용, 에러 처리)

# 3. 테스트 재실행
pytest tests/ -v

# 4. 수동 테스트
python src/console_app.py
```

### 2단계: 타입 힌트 추가

```bash
# mypy로 타입 체크
mypy src/ --ignore-missing-imports

# 타입 힌트 추가 후 재확인
mypy src/ --ignore-missing-imports
```

### 3단계: Magic String/Number 제거

```bash
# pylint로 확인
pylint src/ --score=y

# 상수 분리 후 재확인
pylint src/ --score=y
```

---

## 결론

### 전체 평가

- **코드 품질**: 양호 (7/10)
- **리팩토링 필요도**: 중간
- **우선순위**: console_app.py 리팩토링

### 권장 사항

1. **즉시 실행**: console_app.py 리팩토링
2. **단기**: 타입 힌트 추가
3. **중기**: Magic String/Number 제거
4. **장기**: 테스트 커버리지 개선

---

**작성일**: 2025-12-16  
**버전**: v1.0

