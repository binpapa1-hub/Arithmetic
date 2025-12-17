# 테스트 케이스 작업 리포트

## 프로젝트 정보

| 항목 | 내용 |
|------|------|
| 프로젝트명 | 인사관리 앱 시스템 구축 |
| 대상 시스템 | 정산 시스템 |
| 단계 | 단위 테스트 |
| 작성자 | 홍길동 |
| 승인자 | 박문수 |
| 문서 상태 | 최초 작성 |
| 작성일 | 2020-09-01 |
| 버전 | v1.0 |
| 테스트 범위 | 공통 모듈 |
| 테스트 조직 | 개발팀 |

---

## 테스트 ID

- **TC-CMM-001** (Common Module / Core Mathematical Module)
- **TC-AO-001** (Arithmetic Operations)

---

## 테스트 목적

사칙연산(+, -, *, /) 기능의 정확도를 검증합니다.

---

## 테스트 환경

| 항목 | 내용 |
|------|------|
| 언어 | Python 3.10.11 |
| IDE | PyCharm / Cursor |
| 운영 체제 | Windows 10 |
| 테스트 프레임워크 | pytest 9.0.2 |
| 커버리지 도구 | pytest-cov 7.0.0 |

---

## 테스트 케이스 목록

### 1. 덧셈 테스트 (Addition)

| 테스트 ID | 테스트 함수 | 입력값 | 예상값 | 중요도 | 결과 |
|----------|------------|--------|--------|--------|------|
| TC-ADD-001 | test_addition_1_plus_10 | 1, 10 | 11 | 중요 | 실패 (RED) |
| TC-ADD-002 | test_addition_0_plus_1 | 0, 1 | 1 | 중요 | 실패 (RED) |
| TC-ADD-003 | test_addition_negative_numbers | -1, -10 | -11 | 보통 | 실패 (RED) |

#### 테스트 코드

```python
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
```

---

### 2. 뺄셈 테스트 (Subtraction)

| 테스트 ID | 테스트 함수 | 입력값 | 예상값 | 중요도 | 결과 |
|----------|------------|--------|--------|--------|------|
| TC-SUB-001 | test_subtraction_5_minus_2 | 5, 2 | 3 | 중요 | 실패 (RED) |

#### 테스트 코드

```python
def test_subtraction_5_minus_2(self):
    """뺄셈 테스트: 5 - 2 = 3"""
    result = Arithmetic.subtract(5, 2)
    assert result == 3
```

---

### 3. 곱셈 테스트 (Multiplication)

| 테스트 ID | 테스트 함수 | 입력값 | 예상값 | 중요도 | 결과 |
|----------|------------|--------|--------|--------|------|
| TC-MUL-001 | test_multiplication_negative_numbers | -5, -3 | 15 | 보통 | 실패 (RED) |
| TC-MUL-002 | test_multiplication_by_zero | 0, 10 | 0 | 낮음 | 실패 (RED) |

#### 테스트 코드

```python
def test_multiplication_negative_numbers(self):
    """곱셈 테스트: -5 * -3 = 15"""
    result = Arithmetic.multiply(-5, -3)
    assert result == 15

def test_multiplication_by_zero(self):
    """곱셈 테스트: 0 * 10 = 0"""
    result = Arithmetic.multiply(0, 10)
    assert result == 0
```

---

### 4. 나눗셈 테스트 (Division)

| 테스트 ID | 테스트 함수 | 입력값 | 예상값 | 중요도 | 결과 |
|----------|------------|--------|--------|--------|------|
| TC-DIV-001 | test_division_5_by_2_integer | 5, 2 | 2 (정수) | 중요 | 실패 (RED) |
| TC-DIV-002 | test_division_5_by_2_quotient | 5, 2 | 2.5 (몫) | 보통 | 실패 (RED) |
| TC-DIV-003 | test_division_negative_by_positive | -10, 2 | -5 | 중요 | 실패 (RED) |

#### 테스트 코드

```python
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
```

---

### 5. 예외 처리 테스트 (Exception)

| 테스트 ID | 테스트 함수 | 입력값 | 예상값 | 중요도 | 결과 |
|----------|------------|--------|--------|--------|------|
| TC-EXC-001 | test_division_by_zero_exception | 0, 0 | ArithmeticError | 중요 | 실패 (RED) |

#### 테스트 코드

```python
def test_division_by_zero_exception(self):
    """예외 처리 테스트: 0 / 0 → ArithmeticException"""
    with pytest.raises(ArithmeticError):
        Arithmetic.divide(0, 0)
```

---

## 테스트 실행 결과 요약

### 실행 명령어

```bash
pytest tests/test_arithmetic.py -v
pytest --cov=src --cov-report=term-missing tests/test_arithmetic.py
```

### 결과 요약

| 항목 | 값 |
|------|-----|
| 총 테스트 수 | 10개 |
| 성공 | 0개 |
| 실패 | 10개 |
| 코드 커버리지 | 100% |
| 단계 | RED (예상된 실패) |

### 상세 결과

| # | 테스트 함수 | 실패 원인 | 상태 |
|---|------------|----------|------|
| 1 | test_addition_1_plus_10 | `assert None == 11` | ✅ 예상된 실패 |
| 2 | test_addition_0_plus_1 | `assert None == 1` | ✅ 예상된 실패 |
| 3 | test_addition_negative_numbers | `assert None == -11` | ✅ 예상된 실패 |
| 4 | test_subtraction_5_minus_2 | `assert None == 3` | ✅ 예상된 실패 |
| 5 | test_multiplication_negative_numbers | `assert None == 15` | ✅ 예상된 실패 |
| 6 | test_multiplication_by_zero | `assert None == 0` | ✅ 예상된 실패 |
| 7 | test_division_5_by_2_integer | `assert None == 2` | ✅ 예상된 실패 |
| 8 | test_division_5_by_2_quotient | `assert None == 2.5` | ✅ 예상된 실패 |
| 9 | test_division_negative_by_positive | `assert None == -5` | ✅ 예상된 실패 |
| 10 | test_division_by_zero_exception | `DID NOT RAISE ArithmeticError` | ✅ 예상된 실패 |

---

## 테스트 커버리지

```
Name                Stmts   Miss  Cover   Missing
-------------------------------------------------
src\__init__.py         0      0   100%
src\arithmetic.py      16      0   100%
-------------------------------------------------
TOTAL                  16      0   100%
```

---

## 전제 조건

1. 프로그램은 오류 없이 성공적으로 컴파일되어야 합니다.
2. 모든 종속성을 올바르게 설치하고 구성해야 합니다.
3. Python 3.x 버전이 설치되어 있어야 합니다.

---

## 성공/실패 기준

### 성공 기준
- 모든 테스트 사례가 예상한 결과를 생성합니다.
- 예외 처리가 올바르게 동작합니다.

### 실패 기준
- 테스트 케이스가 예상한 결과를 생성하지 않습니다.
- 예외가 발생하지 않아야 할 경우 예외가 발생합니다.

---

## 특별 절차

1. 테스트 결과를 기록하고 이에 따라 테스트 사례 문서를 업데이트합니다.
2. 즉각적인 해결을 위해 모든 실패를 개발팀에 전달하세요.

---

## 다음 단계

### GREEN 단계 (구현)

| 함수 | 구현 내용 |
|------|---------|
| `add(a, b)` | `return a + b` |
| `subtract(a, b)` | `return a - b` |
| `multiply(a, b)` | `return a * b` |
| `divide(a, b)` | 정수 나눗셈 + 예외 처리 |
| `divide_quotient(a, b)` | 소수점 나눗셈 + 예외 처리 |

---

**작성일**: 2025-12-16  
**작성자**: 개발팀  
**문서 버전**: v1.0

