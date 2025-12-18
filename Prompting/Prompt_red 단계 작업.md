# Test cases report analysis
_Exported on 12/17/2025 at 15:04:03 GMT+9 from Cursor (2.2.20)_

---

**User**

@report/Test_Cases_Report.md 이파일을 분석해서 구현해야할 기능을 기능/비기능 항목으로 구분해서 목록을 알려줘

---

**Cursor**

## 기능/비기능 요구사항 분석

### 기능적 요구사항 (Functional Requirements)

| # | 함수 | 설명 | 입출력 예시 |
|---|------|------|-------------|
| 1 | `add(a, b)` | 두 수의 덧셈 | `add(1, 10)` → `11` |
| 2 | `subtract(a, b)` | 두 수의 뺄셈 | `subtract(5, 2)` → `3` |
| 3 | `multiply(a, b)` | 두 수의 곱셈 | `multiply(-5, -3)` → `15` |
| 4 | `divide(a, b)` | 정수 나눗셈 | `divide(5, 2)` → `2` |
| 5 | `divide_quotient(a, b)` | 소수점 나눗셈 | `divide_quotient(5, 2)` → `2.5` |

### 비기능적 요구사항 (Non-Functional Requirements)

| # | 항목 | 설명 |
|---|------|------|
| 1 | **예외 처리** | 0으로 나눌 때 `ArithmeticError` 발생 |
| 2 | **음수 처리** | 음수 입력값 정상 처리 (덧셈, 곱셈, 나눗셈) |
| 3 | **0 처리** | 0이 포함된 연산 정상 처리 (`0 + 1`, `0 * 10`) |
| 4 | **테스트 커버리지** | 100% 코드 커버리지 유지 |
| 5 | **환경 호환성** | Python 3.10.11, pytest 9.0.2 환경에서 동작 |

---

**User**

구현 우선순위를 readme.md 파일에 green 단계에서 해야할 목록을 추가해줘

---

**Cursor**

```markdown
# Arithmetic Operations - TDD 프로젝트

## 프로젝트 개요

사칙연산(+, -, *, /) 기능의 정확도를 검증하는 단위 테스트 프로젝트입니다.
본 프로젝트는 **RED-GREEN-REFACTOR** 방식의 TDD(Test-Driven Development)를 통해 진행됩니다.

## 프로젝트 정보

- **프로젝트명**: 인사관리 앱 시스템 구축 (정산 시스템)
- **테스트 ID**: TC-CMM-001 / TC-AO-001
- **작성자**: 홍길동
- **승인자**: 박문수
- **작성일**: 2020-09-01
- **버전**: v1.0
- **테스트 범위**: 공통 모듈
- **테스트 조직**: 개발팀

## 테스트 목적

사칙연산의 정확도와 예외 처리를 검증하여 안정적인 수학 연산 모듈을 구축합니다.

## 테스트 환경

- **언어**: Python
- **IDE**: PyCharm
- **운영 체제**: Windows 10

## 테스트 케이스

### 기본 연산 테스트

| 테스트 케이스 | 입력값 | 예상값 | 중요도 | 상태 |
|------------|--------|--------|--------|------|
| 덧셈 | 1 + 10 | 11 | 중요 | 성공 |
| 덧셈 | 0 + 1 | 1 | 중요 | 성공 |
| 덧셈 | -1 + (-10) | -11 | 보통 | 성공 |
| 뺄셈 | 5 - 2 | 3 | 중요 | 성공 |
| 곱셈 | -5 * -3 | 15 | 보통 | 성공 |
| 곱셈 | 0 * 10 | 0 | 낮음 | 성공 |
| 나눗셈 (정수) | 5 / 2 | 2 | 중요 | 성공 |
| 나눗셈 (몫) | 5 ÷ 2 | 2.5 | 보통 | 성공 |
| 나눗셈 | -10 / 2 | -5 | 중요 | 성공 |

### 예외 처리 테스트

| 테스트 케이스 | 입력값 | 예상값 | 중요도 | 상태 |
|------------|--------|--------|--------|------|
| 0으로 나누기 | 0 / 0 | ArithmeticException | 중요 | 성공 |

## TDD 프로세스 (RED-GREEN-REFACTOR)

### 1. RED 단계 --> 진행중 ing~~!!
- 실패하는 테스트 케이스를 먼저 작성합니다.
- 모든 테스트 케이스가 실패하는 것을 확인합니다.

### 2. GREEN 단계
- 테스트를 통과하는 최소한의 코드를 작성합니다.
- 모든 테스트 케이스가 성공하는 것을 확인합니다.

#### 구현 우선순위

| 우선순위 | 함수 | 구현 내용 | 중요도 |
|---------|------|----------|--------|
| 1 | `add(a, b)` | `return a + b` | 중요 |
| 2 | `subtract(a, b)` | `return a - b` | 중요 |
| 3 | `multiply(a, b)` | `return a * b` | 보통 |
| 4 | `divide(a, b)` | 정수 나눗셈 + 0 예외 처리 | 중요 |
| 5 | `divide_quotient(a, b)` | 소수점 나눗셈 + 0 예외 처리 | 보통 |

#### 비기능 요구사항
- [ ] 0으로 나눌 때 `ArithmeticError` 발생
- [ ] 음수 입력값 정상 처리
- [ ] 테스트 커버리지 100% 유지

### 3. REFACTOR 단계
- 코드의 품질을 개선합니다.
- 테스트는 계속 통과해야 합니다.

## 전제 조건

1. 프로그램은 오류 없이 성공적으로 컴파일되어야 합니다.
2. 모든 종속성을 올바르게 설치하고 구성해야 합니다.
3. Python 3.x 버전이 설치되어 있어야 합니다.

## 설치 및 실행

### 1. 프로젝트 클론 또는 다운로드

```bash
cd Arithmetic
```

### 2. 가상 환경 설정 (선택사항)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 테스트 실행

```bash
# pytest를 사용하는 경우
pytest

# unittest를 사용하는 경우
python -m unittest discover
```

## 성공/실패 기준

### 성공 기준
- 모든 테스트 사례가 예상한 결과를 생성합니다.
- 예외 처리가 올바르게 동작합니다.

### 실패 기준
- 테스트 케이스가 예상한 결과를 생성하지 않습니다.
- 예외가 발생하지 않아야 할 경우 예외가 발생합니다.

## 특별 절차

1. 테스트 결과를 기록하고 이에 따라 테스트 사례 문서를 업데이트합니다.
2. 즉각적인 해결을 위해 모든 실패를 개발팀에 전달하세요.

## 프로젝트 구조

```
Arithmetic/
├── README.md
├── requirements.txt
├── src/
│   └── arithmetic.py
└── tests/
    └── test_arithmetic.py
```

## 참고사항

- 다양한 조합(양수, 음수, 0)을 포함한 테스트 케이스를 통해 연산의 정확도와 범위를 검증합니다.
- 정수 나눗셈과 소수점을 포함한 몫 계산을 모두 테스트합니다.
- 예외 처리(0으로 나누기)를 반드시 포함합니다.


```

README.md에 GREEN 단계 구현 목록을 추가했습니다:

**구현 우선순위:**
1. `add(a, b)` - 덧셈 (중요)
2. `subtract(a, b)` - 뺄셈 (중요)
3. `multiply(a, b)` - 곱셈 (보통)
4. `divide(a, b)` - 정수 나눗셈 + 예외 처리 (중요)
5. `divide_quotient(a, b)` - 소수점 나눗셈 + 예외 처리 (보통)

**비기능 요구사항 체크리스트도 추가:**
- 0으로 나눌 때 ArithmeticError 발생
- 음수 입력값 정상 처리
- 테스트 커버리지 100% 유지

---

**User**

@README.md 내용중 @README.md (61-69) 을 최소단위로 구현하려고 하는데 먼저 시나리오를 작성해서 보여주고 승인 받은 후 구현해줘

---

**Cursor**

## GREEN 단계 구현 시나리오

### 구현 순서 (최소 단위)

| 순서 | 함수 | 구현 코드 | 테스트 통과 예상 |
|-----|------|----------|----------------|
| 1 | `add(a, b)` | `return a + b` | TC-ADD-001~003 |
| 2 | `subtract(a, b)` | `return a - b` | TC-SUB-001 |
| 3 | `multiply(a, b)` | `return a * b` | TC-MUL-001~002 |
| 4 | `divide(a, b)` | `if b == 0: raise ArithmeticError`<br>`return a // b` | TC-DIV-001, 003, TC-EXC-001 |
| 5 | `divide_quotient(a, b)` | `if b == 0: raise ArithmeticError`<br>`return a / b` | TC-DIV-002 |

### 구현 계획

```python
class Arithmetic:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ArithmeticError("Cannot divide by zero")
        return a // b

    @staticmethod
    def divide_quotient(a, b):
        if b == 0:
            raise ArithmeticError("Cannot divide by zero")
        return a / b
```

### 예상 결과
- 총 10개 테스트 모두 통과 (RED → GREEN)
- 코드 커버리지 100% 유지

---

**이 시나리오로 진행할까요?**

```python
class Arithmetic:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ArithmeticError("Cannot divide by zero")
        return a // b

    @staticmethod
    def divide_quotient(a, b):
        if b == 0:
            raise ArithmeticError("Cannot divide by zero")
        return a / b
```

---

**User**

네

---

**Cursor**

```python
"""
사칙연산 모듈
TC-CMM-001 / TC-AO-001
"""


class Arithmetic:
    """사칙연산을 수행하는 클래스"""
    
    @staticmethod
    def add(a, b):
        """두 수를 더합니다"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """두 수를 뺍니다"""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """두 수를 곱합니다"""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """두 수를 나눕니다 (정수 나눗셈)"""
        if b == 0:
            raise ArithmeticError("Cannot divide by zero")
        return a // b
    
    @staticmethod
    def divide_quotient(a, b):
        """두 수를 나눕니다 (몫, 소수점 포함)"""
        if b == 0:
            raise ArithmeticError("Cannot divide by zero")
        return a / b


```

✅ **GREEN 단계 완료!**

모든 10개 테스트가 통과했습니다:

| 함수 | 테스트 | 결과 |
|------|--------|------|
| `add` | 3개 | ✅ PASSED |
| `subtract` | 1개 | ✅ PASSED |
| `multiply` | 2개 | ✅ PASSED |
| `divide` | 2개 | ✅ PASSED |
| `divide_quotient` | 1개 | ✅ PASSED |
| 예외 처리 | 1개 | ✅ PASSED |

**RED → GREEN 전환 성공!**

---

**User**

첨부와 같이 실행 했는데, 아무런 것도 안나오는데, 실행 결과 만들수 있을까?

---

**Cursor**

`src/arithmetic.py`에 실행 가능한 메인 코드를 추가하겠습니다.

```python
"""
사칙연산 모듈
TC-CMM-001 / TC-AO-001
"""


class Arithmetic:
    """사칙연산을 수행하는 클래스"""
    
    @staticmethod
    def add(a, b):
        """두 수를 더합니다"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """두 수를 뺍니다"""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """두 수를 곱합니다"""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """두 수를 나눕니다 (정수 나눗셈)"""
        if b == 0:
            raise ArithmeticError("Cannot divide by zero")
        return a // b
    
    @staticmethod
    def divide_quotient(a, b):
        """두 수를 나눕니다 (몫, 소수점 포함)"""
        if b == 0:
            raise ArithmeticError("Cannot divide by zero")
        return a / b


if __name__ == "__main__":
    print("=== 사칙연산 테스트 ===")
    print(f"덧셈: 1 + 10 = {Arithmetic.add(1, 10)}")
    print(f"덧셈: -1 + (-10) = {Arithmetic.add(-1, -10)}")
    print(f"뺄셈: 5 - 2 = {Arithmetic.subtract(5, 2)}")
    print(f"곱셈: -5 * -3 = {Arithmetic.multiply(-5, -3)}")
    print(f"곱셈: 0 * 10 = {Arithmetic.multiply(0, 10)}")
    print(f"나눗셈(정수): 5 // 2 = {Arithmetic.divide(5, 2)}")
    print(f"나눗셈(소수): 5 / 2 = {Arithmetic.divide_quotient(5, 2)}")
    print(f"나눗셈: -10 / 2 = {Arithmetic.divide(-10, 2)}")

```

이제 다시 실행해보세요:

```bash
python src\arithmetic.py
```

실행하면 다음과 같은 결과가 출력됩니다:

```
=== 사칙연산 테스트 ===
덧셈: 1 + 10 = 11
덧셈: -1 + (-10) = -11
뺄셈: 5 - 2 = 3
곱셈: -5 * -3 = 15
곱셈: 0 * 10 = 0
나눗셈(정수): 5 // 2 = 2
나눗셈(소수): 5 / 2 = 2.5
나눗셈: -10 / 2 = -5
```

```shellscript
python src\arithmetic.py
```

```plaintext
=== 사칙연산 테스트 ===
덧셈: 1 + 10 = 11
덧셈: -1 + (-10) = -11
뺄셈: 5 - 2 = 3
곱셈: -5 * -3 = 15
곱셈: 0 * 10 = 0
나눗셈(정수): 5 // 2 = 2
나눗셈(소수): 5 / 2 = 2.5
나눗셈: -10 / 2 = -5
```

---

**User**

@README.md 내용중 @README.md (71-74) 을 최소단위로 구현하라고 하는데 먼저 시나리오를 작성해서 보여주고 승인 받은후 구현해줘

---

**Cursor**

## 비기능 요구사항 구현 시나리오

### 현재 상태 분석

| 요구사항 | 현재 상태 | 비고 |
|---------|----------|------|
| 0으로 나눌 때 `ArithmeticError` 발생 | ✅ 이미 구현됨 | `divide`, `divide_quotient`에 적용 |
| 음수 입력값 정상 처리 | ✅ 이미 구현됨 | 테스트 통과 확인됨 |
| 테스트 커버리지 100% 유지 | ⏳ 확인 필요 | pytest-cov로 검증 |

### 구현 계획

**추가 구현 불필요** - 이미 GREEN 단계에서 모두 구현 완료

### 검증 시나리오

```bash
# 1. 테스트 커버리지 확인
pytest --cov=src --cov-report=term-missing tests/test_arithmetic.py

# 2. 예외 처리 확인 (수동 테스트)
python -c "from src.arithmetic import Arithmetic; Arithmetic.divide(1, 0)"
```

### 예상 결과
- 커버리지 100% 확인
- `ArithmeticError: Cannot divide by zero` 발생 확인

### README 업데이트
- 체크박스를 ✅ 완료 상태로 변경

---

**이 시나리오로 검증 및 README 업데이트를 진행할까요?**

```shellscript
# 1. 테스트 커버리지 확인
pytest --cov=src --cov-report=term-missing tests/test_arithmetic.py

# 2. 예외 처리 확인 (수동 테스트)
python -c "from src.arithmetic import Arithmetic; Arithmetic.divide(1, 0)"
```

---

**User**

네

---

**Cursor**

커버리지가 67%로 나옵니다. `if __name__ == "__main__":` 부분이 테스트에서 실행되지 않아서입니다. 이 부분은 실행 코드이므로 커버리지 제외 처리하겠습니다.

```python
"""
사칙연산 모듈
TC-CMM-001 / TC-AO-001
"""


class Arithmetic:
    """사칙연산을 수행하는 클래스"""
    
    @staticmethod
    def add(a, b):
        """두 수를 더합니다"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """두 수를 뺍니다"""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """두 수를 곱합니다"""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """두 수를 나눕니다 (정수 나눗셈)"""
        if b == 0:
            raise ArithmeticError("Cannot divide by zero")
        return a // b
    
    @staticmethod
    def divide_quotient(a, b):
        """두 수를 나눕니다 (몫, 소수점 포함)"""
        if b == 0:
            raise ArithmeticError("Cannot divide by zero")
        return a / b


if __name__ == "__main__":  # pragma: no cover
    print("=== 사칙연산 테스트 ===")
    print(f"덧셈: 1 + 10 = {Arithmetic.add(1, 10)}")
    print(f"덧셈: -1 + (-10) = {Arithmetic.add(-1, -10)}")
    print(f"뺄셈: 5 - 2 = {Arithmetic.subtract(5, 2)}")
    print(f"곱셈: -5 * -3 = {Arithmetic.multiply(-5, -3)}")
    print(f"곱셈: 0 * 10 = {Arithmetic.multiply(0, 10)}")
    print(f"나눗셈(정수): 5 // 2 = {Arithmetic.divide(5, 2)}")
    print(f"나눗셈(소수): 5 / 2 = {Arithmetic.divide_quotient(5, 2)}")
    print(f"나눗셈: -10 / 2 = {Arithmetic.divide(-10, 2)}")

```

95%입니다. line 36이 누락되었네요 - `divide_quotient`의 0 예외 처리입니다. 테스트에서 `divide_quotient(x, 0)` 케이스가 없습니다. 테스트를 추가하겠습니다.

```python
"""
사칙연산 정확도 테스트
TC-CMM-001 / TC-AO-001
"""
import pytest
from src.arithmetic import Arithmetic


class TestArithmetic:
    """사칙연산 기능 테스트 클래스"""
    
    def test_addition_1_plus_10(self):
        """덧셈 테스트: 1 + 10 = 11"""
        result = Arithmetic.add(1, 10)
        assert result == 11
    
    def test_addition_0_plus_1(self):
        """덧셈 테스트: 0 + 1 = 1"""
        result = Arithmetic.add(0, 1)
        assert result == 1
    
    def test_addition_negative_numbers(self):
        """덧셈 테스트: -1 + (-10) = -11"""
        result = Arithmetic.add(-1, -10)
        assert result == -11
    
    def test_subtraction_5_minus_2(self):
        """뺄셈 테스트: 5 - 2 = 3"""
        result = Arithmetic.subtract(5, 2)
        assert result == 3
    
    def test_multiplication_negative_numbers(self):
        """곱셈 테스트: -5 * -3 = 15"""
        result = Arithmetic.multiply(-5, -3)
        assert result == 15
    
    def test_multiplication_by_zero(self):
        """곱셈 테스트: 0 * 10 = 0"""
        result = Arithmetic.multiply(0, 10)
        assert result == 0
    
    def test_division_5_by_2_integer(self):
        """나눗셈 테스트 (정수): 5 / 2 = 2"""
        result = Arithmetic.divide(5, 2)
        assert result == 2
    
    def test_division_5_by_2_quotient(self):
        """나눗셈 테스트 (몫): 5 ÷ 2 = 2.5"""
        result = Arithmetic.divide_quotient(5, 2)
        assert result == 2.5
    
    def test_division_negative_by_positive(self):
        """나눗셈 테스트: -10 / 2 = -5"""
        result = Arithmetic.divide(-10, 2)
        assert result == -5
    
    def test_division_by_zero_exception(self):
        """예외 처리 테스트: 0 / 0 → ArithmeticException"""
        with pytest.raises(ArithmeticError):
            Arithmetic.divide(0, 0)

    def test_division_quotient_by_zero_exception(self):
        """예외 처리 테스트: divide_quotient(1, 0) → ArithmeticException"""
        with pytest.raises(ArithmeticError):
            Arithmetic.divide_quotient(1, 0)


```

✅ **커버리지 100% 달성!** 이제 README를 업데이트하겠습니다.

```markdown
# Arithmetic Operations - TDD 프로젝트

## 프로젝트 개요

사칙연산(+, -, *, /) 기능의 정확도를 검증하는 단위 테스트 프로젝트입니다.
본 프로젝트는 **RED-GREEN-REFACTOR** 방식의 TDD(Test-Driven Development)를 통해 진행됩니다.

## 프로젝트 정보

- **프로젝트명**: 인사관리 앱 시스템 구축 (정산 시스템)
- **테스트 ID**: TC-CMM-001 / TC-AO-001
- **작성자**: 홍길동
- **승인자**: 박문수
- **작성일**: 2020-09-01
- **버전**: v1.0
- **테스트 범위**: 공통 모듈
- **테스트 조직**: 개발팀

## 테스트 목적

사칙연산의 정확도와 예외 처리를 검증하여 안정적인 수학 연산 모듈을 구축합니다.

## 테스트 환경

- **언어**: Python
- **IDE**: PyCharm
- **운영 체제**: Windows 10

## 테스트 케이스

### 기본 연산 테스트

| 테스트 케이스 | 입력값 | 예상값 | 중요도 | 상태 |
|------------|--------|--------|--------|------|
| 덧셈 | 1 + 10 | 11 | 중요 | 성공 |
| 덧셈 | 0 + 1 | 1 | 중요 | 성공 |
| 덧셈 | -1 + (-10) | -11 | 보통 | 성공 |
| 뺄셈 | 5 - 2 | 3 | 중요 | 성공 |
| 곱셈 | -5 * -3 | 15 | 보통 | 성공 |
| 곱셈 | 0 * 10 | 0 | 낮음 | 성공 |
| 나눗셈 (정수) | 5 / 2 | 2 | 중요 | 성공 |
| 나눗셈 (몫) | 5 ÷ 2 | 2.5 | 보통 | 성공 |
| 나눗셈 | -10 / 2 | -5 | 중요 | 성공 |

### 예외 처리 테스트

| 테스트 케이스 | 입력값 | 예상값 | 중요도 | 상태 |
|------------|--------|--------|--------|------|
| 0으로 나누기 | 0 / 0 | ArithmeticException | 중요 | 성공 |

## TDD 프로세스 (RED-GREEN-REFACTOR)

### 1. RED 단계 --> 진행중 ing~~!!
- 실패하는 테스트 케이스를 먼저 작성합니다.
- 모든 테스트 케이스가 실패하는 것을 확인합니다.

### 2. GREEN 단계
- 테스트를 통과하는 최소한의 코드를 작성합니다.
- 모든 테스트 케이스가 성공하는 것을 확인합니다.

#### 구현 우선순위

| 우선순위 | 함수 | 구현 내용 | 중요도 |
|---------|------|----------|--------|
| 1 | `add(a, b)` | `return a + b` | 중요 |
| 2 | `subtract(a, b)` | `return a - b` | 중요 |
| 3 | `multiply(a, b)` | `return a * b` | 보통 |
| 4 | `divide(a, b)` | 정수 나눗셈 + 0 예외 처리 | 중요 |
| 5 | `divide_quotient(a, b)` | 소수점 나눗셈 + 0 예외 처리 | 보통 |

#### 비기능 요구사항
- [x] 0으로 나눌 때 `ArithmeticError` 발생
- [x] 음수 입력값 정상 처리
- [x] 테스트 커버리지 100% 유지

### 3. REFACTOR 단계
- 코드의 품질을 개선합니다.
- 테스트는 계속 통과해야 합니다.

## 전제 조건

1. 프로그램은 오류 없이 성공적으로 컴파일되어야 합니다.
2. 모든 종속성을 올바르게 설치하고 구성해야 합니다.
3. Python 3.x 버전이 설치되어 있어야 합니다.

## 설치 및 실행

### 1. 프로젝트 클론 또는 다운로드

```bash
cd Arithmetic
```

### 2. 가상 환경 설정 (선택사항)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. 의존성 설치

```bash
pip install -r requirements.txt
```

### 4. 테스트 실행

```bash
# pytest를 사용하는 경우
pytest

# unittest를 사용하는 경우
python -m unittest discover
```

## 성공/실패 기준

### 성공 기준
- 모든 테스트 사례가 예상한 결과를 생성합니다.
- 예외 처리가 올바르게 동작합니다.

### 실패 기준
- 테스트 케이스가 예상한 결과를 생성하지 않습니다.
- 예외가 발생하지 않아야 할 경우 예외가 발생합니다.

## 특별 절차

1. 테스트 결과를 기록하고 이에 따라 테스트 사례 문서를 업데이트합니다.
2. 즉각적인 해결을 위해 모든 실패를 개발팀에 전달하세요.

## 프로젝트 구조

```
Arithmetic/
├── README.md
├── requirements.txt
├── src/
│   └── arithmetic.py
└── tests/
    └── test_arithmetic.py
```

## 참고사항

- 다양한 조합(양수, 음수, 0)을 포함한 테스트 케이스를 통해 연산의 정확도와 범위를 검증합니다.
- 정수 나눗셈과 소수점을 포함한 몫 계산을 모두 테스트합니다.
- 예외 처리(0으로 나누기)를 반드시 포함합니다.


```

✅ **비기능 요구사항 검증 완료!**

| 요구사항 | 상태 | 검증 방법 |
|---------|------|----------|
| 0으로 나눌 때 `ArithmeticError` 발생 | ✅ 완료 | 테스트 2개 통과 |
| 음수 입력값 정상 처리 | ✅ 완료 | 테스트 통과 |
| 테스트 커버리지 100% 유지 | ✅ 완료 | `pytest-cov` 확인 |

**결과:**
- 11개 테스트 통과
- 코드 커버리지 100%
- README 체크박스 업데이트 완료

---

**User**

첨부한 이미지처럼 값을 입력 받아서 처리할수 있는 콘솔프로그램을 만들어줘

---

**Cursor**

```python
"""
사칙연산 콘솔 프로그램
"""
from arithmetic import Arithmetic


def main():
    print("입력화면")
    print()
    
    a = int(input("첫번째 정수값>>"))
    print()
    
    operator = input("연산자>>")
    print()
    
    b = int(input("두번째 정수값>"))
    print()
    
    print("결과 뷰 화면")
    print()
    print("=" * 30)
    print()
    print(f"{a} {operator} {b}을 계산합니다.")
    print()
    print("=" * 30)
    print()
    
    if operator == "+":
        result = Arithmetic.add(a, b)
    elif operator == "-":
        result = Arithmetic.subtract(a, b)
    elif operator == "*":
        result = Arithmetic.multiply(a, b)
    elif operator == "/":
        result = Arithmetic.divide(a, b)
    else:
        print("잘못된 연산자입니다.")
        return
    
    print(f"{a}{operator}{b}={result}입니다.")


if __name__ == "__main__":
    main()

```

완료! 다음 명령어로 실행하세요:

```bash
cd src
python console_app.py
```

실행하면 이미지처럼 값을 입력받아 계산 결과를 출력합니다.

```shellscript
cd src
python console_app.py
```

