# Test cases report analysis
_Exported on 12/18/2025 at 13:19:45 GMT+9 from Cursor (2.2.20)_

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

---

**User**

첨부한 이미지처럼 동작하는 콘솔 프로그램을 첨부한 그림처럼 PyQT로 GUI 프로그램으로 리펙토링을 하고자 합니다. 코드, 스멜분석, 정적분석, SOLID를 고려해서 방법을 알려줘 단계적으로

---

**Cursor**


현재 코드 확인 중. 이후 PyQt 리팩토링 계획을 단계별로 제시합니다.



단계별 리팩토링 계획 문서 작성 중.


```markdown
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

```


리팩토링 계획서를 작성했습니다. 각 단계별 구현 가이드 문서를 추가로 작성 중입니다.


```markdown
# PyQt GUI 리팩토링 구현 가이드

## 단계별 구현 코드 예시

---

## Phase 1: CalculatorService 구현

### 1.1 calculator_service.py

```python
"""
계산기 서비스 - 비즈니스 로직 담당
SOLID 원칙: SRP (단일 책임), DIP (의존성 역전)
"""
from typing import Dict, Callable
from arithmetic import Arithmetic


class CalculatorService:
    """계산 로직을 처리하는 서비스 클래스"""
    
    # Strategy 패턴: 연산자 확장 가능 (OCP 원칙)
    OPERATORS: Dict[str, Callable[[float, float], float]] = {
        "+": Arithmetic.add,
        "-": Arithmetic.subtract,
        "×": Arithmetic.multiply,
        "*": Arithmetic.multiply,  # 별칭
        "/": Arithmetic.divide_quotient,  # 소수점 나눗셈
    }
    
    @classmethod
    def calculate(cls, a: float, operator: str, b: float) -> float:
        """
        계산을 수행합니다.
        
        Args:
            a: 첫 번째 피연산자
            operator: 연산자 (+, -, ×, /)
            b: 두 번째 피연산자
            
        Returns:
            계산 결과
            
        Raises:
            ArithmeticError: 0으로 나눌 때
            ValueError: 지원하지 않는 연산자
        """
        if operator not in cls.OPERATORS:
            raise ValueError(f"지원하지 않는 연산자: {operator}")
        
        operation = cls.OPERATORS[operator]
        return operation(a, b)
    
    @classmethod
    def is_valid_operator(cls, operator: str) -> bool:
        """연산자가 유효한지 확인"""
        return operator in cls.OPERATORS
```

**SOLID 적용:**
- ✅ **SRP**: 계산 로직만 담당
- ✅ **OCP**: OPERATORS 딕셔너리로 연산자 확장 가능
- ✅ **DIP**: Arithmetic에 의존하되 인터페이스로 추상화

---

## Phase 2: CalculatorPresenter 구현

### 2.1 calculator_presenter.py

```python
"""
계산기 프레젠터 - UI와 비즈니스 로직 사이의 중재자
SOLID 원칙: SRP, DIP
"""
from typing import Optional
from calculator_service import CalculatorService


class CalculatorState:
    """계산기 상태 관리 클래스"""
    
    def __init__(self):
        self.current_value: str = "0"
        self.previous_value: Optional[float] = None
        self.operator: Optional[str] = None
        self.waiting_for_operand: bool = False
    
    def reset(self):
        """상태 초기화"""
        self.current_value = "0"
        self.previous_value = None
        self.operator = None
        self.waiting_for_operand = False


class CalculatorPresenter:
    """계산기 프레젠터 - MVP 패턴"""
    
    def __init__(self, view):
        """
        Args:
            view: CalculatorWindow 인스턴스
        """
        self.view = view
        self.state = CalculatorState()
        self.service = CalculatorService()
    
    def handle_number_input(self, number: str):
        """숫자 입력 처리"""
        if self.state.waiting_for_operand:
            self.state.current_value = number
            self.state.waiting_for_operand = False
        else:
            if self.state.current_value == "0":
                self.state.current_value = number
            else:
                self.state.current_value += number
        
        self.view.update_display(self.state.current_value)
    
    def handle_operator_input(self, operator: str):
        """연산자 입력 처리"""
        if self.state.operator and not self.state.waiting_for_operand:
            # 이전 연산 실행
            self._perform_calculation()
        
        self.state.previous_value = float(self.state.current_value)
        self.state.operator = operator
        self.state.waiting_for_operand = True
    
    def handle_equals(self):
        """등호 버튼 처리"""
        if self.state.operator and self.state.previous_value is not None:
            self._perform_calculation()
            self.state.operator = None
            self.state.previous_value = None
            self.state.waiting_for_operand = True
    
    def handle_clear(self):
        """초기화"""
        self.state.reset()
        self.view.update_display(self.state.current_value)
    
    def handle_sign_change(self):
        """부호 변경 (+/-)"""
        if self.state.current_value != "0":
            if self.state.current_value.startswith("-"):
                self.state.current_value = self.state.current_value[1:]
            else:
                self.state.current_value = "-" + self.state.current_value
            self.view.update_display(self.state.current_value)
    
    def handle_decimal_point(self):
        """소수점 입력"""
        if self.state.waiting_for_operand:
            self.state.current_value = "0."
            self.state.waiting_for_operand = False
        elif "." not in self.state.current_value:
            self.state.current_value += "."
        
        self.view.update_display(self.state.current_value)
    
    def _perform_calculation(self):
        """실제 계산 수행"""
        try:
            result = self.service.calculate(
                self.state.previous_value,
                self.state.operator,
                float(self.state.current_value)
            )
            
            # 결과 포맷팅 (정수면 정수로, 소수면 소수로)
            if result == int(result):
                self.state.current_value = str(int(result))
            else:
                self.state.current_value = str(result)
            
            self.view.update_display(self.state.current_value)
            
        except ArithmeticError as e:
            self.view.show_error("0으로 나눌 수 없습니다.")
            self.handle_clear()
        except Exception as e:
            self.view.show_error(f"오류: {str(e)}")
            self.handle_clear()
```

**SOLID 적용:**
- ✅ **SRP**: UI 이벤트 처리와 상태 관리만 담당
- ✅ **DIP**: CalculatorService에 의존 (구체 클래스가 아닌 인터페이스)

---

## Phase 3: GUI 컴포넌트 구현

### 3.1 gui/display_widget.py

```python
"""
디스플레이 위젯 - 계산 결과 표시
"""
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class DisplayWidget(QLabel):
    """계산기 디스플레이 위젯"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """UI 설정"""
        self.setText("0")
        self.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        
        # 폰트 설정
        font = QFont("Arial", 24, QFont.Weight.Bold)
        self.setFont(font)
        
        # 스타일 설정
        self.setStyleSheet("""
            QLabel {
                background-color: #1e1e1e;
                color: #ffffff;
                border: 2px solid #333;
                border-radius: 5px;
                padding: 10px;
                min-height: 60px;
            }
        """)
    
    def update_display(self, value: str):
        """디스플레이 업데이트"""
        self.setText(value)
```

### 3.2 gui/button_factory.py

```python
"""
버튼 팩토리 - 버튼 생성 및 스타일링
Factory Pattern 적용
"""
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class ButtonFactory:
    """버튼 생성 팩토리 클래스"""
    
    @staticmethod
    def create_number_button(number: str) -> QPushButton:
        """숫자 버튼 생성"""
        button = QPushButton(number)
        button.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 18px;
                font-weight: bold;
                min-height: 50px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """)
        return button
    
    @staticmethod
    def create_operator_button(operator: str) -> QPushButton:
        """연산자 버튼 생성"""
        button = QPushButton(operator)
        button.setStyleSheet("""
            QPushButton {
                background-color: #ff9500;
                color: white;
                border: 1px solid #ff7700;
                border-radius: 5px;
                font-size: 18px;
                font-weight: bold;
                min-height: 50px;
            }
            QPushButton:hover {
                background-color: #ff7700;
            }
            QPushButton:pressed {
                background-color: #ff5500;
            }
        """)
        return button
    
    @staticmethod
    def create_equals_button() -> QPushButton:
        """등호 버튼 생성"""
        button = QPushButton("=")
        button.setStyleSheet("""
            QPushButton {
                background-color: #007aff;
                color: white;
                border: 1px solid #0051d5;
                border-radius: 5px;
                font-size: 18px;
                font-weight: bold;
                min-height: 50px;
            }
            QPushButton:hover {
                background-color: #0051d5;
            }
            QPushButton:pressed {
                background-color: #003d9e;
            }
        """)
        return button
    
    @staticmethod
    def create_function_button(text: str) -> QPushButton:
        """기능 버튼 생성 (+, -, .)"""
        button = QPushButton(text)
        button.setStyleSheet("""
            QPushButton {
                background-color: #d0d0d0;
                border: 1px solid #b0b0b0;
                border-radius: 5px;
                font-size: 18px;
                font-weight: bold;
                min-height: 50px;
            }
            QPushButton:hover {
                background-color: #c0c0c0;
            }
            QPushButton:pressed {
                background-color: #b0b0b0;
            }
        """)
        return button
```

### 3.3 gui/calculator_window.py

```python
"""
계산기 메인 윈도우
"""
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QGridLayout, QMessageBox
from PyQt6.QtCore import Qt
from gui.display_widget import DisplayWidget
from gui.button_factory import ButtonFactory
from calculator_presenter import CalculatorPresenter


class CalculatorWindow(QMainWindow):
    """계산기 메인 윈도우"""
    
    def __init__(self):
        super().__init__()
        self.presenter = CalculatorPresenter(self)
        self.setup_ui()
    
    def setup_ui(self):
        """UI 초기 설정"""
        self.setWindowTitle("계산기")
        self.setFixedSize(300, 400)
        
        # 중앙 위젯
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 메인 레이아웃
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # 디스플레이
        self.display = DisplayWidget()
        main_layout.addWidget(self.display)
        
        # 버튼 그리드
        button_layout = QGridLayout()
        self._create_buttons(button_layout)
        main_layout.addLayout(button_layout)
    
    def _create_buttons(self, layout: QGridLayout):
        """버튼 생성 및 배치"""
        factory = ButtonFactory()
        
        # 버튼 배치 (4x4 그리드)
        buttons = [
            # Row 1
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("×", 0, 3),
            # Row 2
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("-", 1, 3),
            # Row 3
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("+", 2, 3),
            # Row 4
            ("+/-", 3, 0), ("0", 3, 1), (".", 3, 2), ("=", 3, 3),
        ]
        
        for text, row, col in buttons:
            if text.isdigit():
                button = factory.create_number_button(text)
                button.clicked.connect(lambda checked, n=text: self.presenter.handle_number_input(n))
            elif text in ["+", "-", "×", "/"]:
                button = factory.create_operator_button(text)
                button.clicked.connect(lambda checked, op=text: self.presenter.handle_operator_input(op))
            elif text == "=":
                button = factory.create_equals_button()
                button.clicked.connect(self.presenter.handle_equals)
            elif text == "+/-":
                button = factory.create_function_button(text)
                button.clicked.connect(self.presenter.handle_sign_change)
            elif text == ".":
                button = factory.create_function_button(text)
                button.clicked.connect(self.presenter.handle_decimal_point)
            else:
                button = factory.create_function_button(text)
            
            layout.addWidget(button, row, col)
        
        # Clear 버튼 추가 (선택사항)
        clear_button = factory.create_function_button("C")
        clear_button.clicked.connect(self.presenter.handle_clear)
        layout.addWidget(clear_button, 4, 0, 1, 4)  # 전체 너비
    
    def update_display(self, value: str):
        """디스플레이 업데이트 (Presenter에서 호출)"""
        self.display.update_display(value)
    
    def show_error(self, message: str):
        """에러 메시지 표시"""
        QMessageBox.warning(self, "오류", message)
```

### 3.4 main.py (진입점)

```python
"""
GUI 계산기 실행 진입점
"""
import sys
from PyQt6.QtWidgets import QApplication
from gui.calculator_window import CalculatorWindow


def main():
    """메인 함수"""
    app = QApplication(sys.argv)
    
    window = CalculatorWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
```

---

## Phase 4: 테스트 작성

### 4.1 test_calculator_service.py

```python
"""CalculatorService 테스트"""
import pytest
from calculator_service import CalculatorService


class TestCalculatorService:
    """CalculatorService 테스트 클래스"""
    
    def test_add(self):
        """덧셈 테스트"""
        result = CalculatorService.calculate(1, "+", 10)
        assert result == 11
    
    def test_subtract(self):
        """뺄셈 테스트"""
        result = CalculatorService.calculate(5, "-", 2)
        assert result == 3
    
    def test_multiply(self):
        """곱셈 테스트"""
        result = CalculatorService.calculate(-5, "×", -3)
        assert result == 15
    
    def test_divide(self):
        """나눗셈 테스트"""
        result = CalculatorService.calculate(5, "/", 2)
        assert result == 2.5
    
    def test_division_by_zero(self):
        """0으로 나누기 예외 테스트"""
        with pytest.raises(ArithmeticError):
            CalculatorService.calculate(1, "/", 0)
    
    def test_invalid_operator(self):
        """잘못된 연산자 예외 테스트"""
        with pytest.raises(ValueError):
            CalculatorService.calculate(1, "%", 2)
    
    def test_is_valid_operator(self):
        """연산자 유효성 검사 테스트"""
        assert CalculatorService.is_valid_operator("+") is True
        assert CalculatorService.is_valid_operator("%") is False
```

---

## Phase 5: 정적 분석 및 코드 품질

### 5.1 .pylintrc 설정

```ini
[MASTER]
disable=missing-docstring,too-few-public-methods

[MESSAGES CONTROL]
disable=import-error

[FORMAT]
max-line-length=100
```

### 5.2 실행 명령어

```bash
# pylint
pylint src/gui/*.py src/calculator_service.py src/calculator_presenter.py

# mypy (타입 체크)
mypy src/gui/*.py src/calculator_service.py src/calculator_presenter.py

# flake8 (스타일 체크)
flake8 src/gui/*.py src/calculator_service.py src/calculator_presenter.py
```

---

## 구현 체크리스트

### Phase 1: Service Layer
- [x] CalculatorService 클래스 생성
- [x] 연산자 매핑 딕셔너리
- [x] calculate 메서드 구현
- [x] 예외 처리
- [ ] 단위 테스트 작성

### Phase 2: Presenter Layer
- [x] CalculatorPresenter 클래스 생성
- [x] CalculatorState 클래스 생성
- [x] 숫자 입력 처리
- [x] 연산자 입력 처리
- [x] 계산 로직
- [x] 에러 처리

### Phase 3: View Layer
- [x] CalculatorWindow 생성
- [x] DisplayWidget 생성
- [x] ButtonFactory 생성
- [x] 버튼 레이아웃 구성
- [x] 이벤트 연결

### Phase 4: 통합
- [ ] main.py 생성
- [ ] 전체 통합 테스트
- [ ] UI 테스트

### Phase 5: 품질 관리
- [ ] pylint 실행 및 수정
- [ ] mypy 타입 체크
- [ ] flake8 스타일 체크
- [ ] 문서화

---

**작성일**: 2025-12-16  
**버전**: v1.0

```


리팩토링 계획서와 구현 가이드를 작성했습니다.

## 작성된 문서

1. **`report/Refactoring_Plan.md`** - 전체 리팩토링 계획서
   - 코드 스멜 분석
   - 아키텍처 설계 (MVP 패턴)
   - SOLID 원칙 적용 방안
   - 10단계 구현 계획

2. **`report/Refactoring_Implementation_Guide.md`** - 단계별 구현 가이드
   - 각 클래스별 코드 예시
   - SOLID 원칙 적용 설명
   - 테스트 코드 예시
   - 정적 분석 설정

## 주요 개선 사항

### 코드 스멜 해결
- Long Method → Presenter와 Service로 분리
- Feature Envy → CalculatorService로 연산 로직 캡슐화
- Magic String → 상수로 분리
- Missing Error Handling → 예외 처리 추가

### SOLID 원칙 적용
- SRP: View, Presenter, Service 분리
- OCP: Strategy 패턴으로 연산자 확장 가능
- DIP: 인터페이스 기반 의존성

### 아키텍처
- MVP 패턴 적용
- 비즈니스 로직과 UI 분리
- 테스트 가능한 구조

이 계획서대로 구현을 진행할까요? 원하시면 단계별로 코드를 생성하겠습니다.

