# Sanity Test 리포트

**실행 일자**: 2025-12-16  
**테스트 환경**: Python 3.10.11, pytest 9.0.2

---

## 테스트 결과 요약

| 항목 | 결과 | 상태 |
|------|------|------|
| 단위 테스트 | 18/18 통과 | ✅ |
| 코드 커버리지 (핵심 로직) | 100% | ✅ |
| Import 검증 | 모든 모듈 정상 | ✅ |
| 기본 연산 검증 | 정상 동작 | ✅ |
| CalculatorService 검증 | 정상 동작 | ✅ |

**종합 결과**: ✅ **PASS**

---

## 1. 단위 테스트 실행

### 실행 명령어
```bash
pytest tests/ -v
```

### 결과
```
============================= test session starts =============================
collected 18 items

tests/test_arithmetic.py::TestArithmetic::test_addition_1_plus_10 PASSED
tests/test_arithmetic.py::TestArithmetic::test_addition_0_plus_1 PASSED
tests/test_arithmetic.py::TestArithmetic::test_addition_negative_numbers PASSED
tests/test_arithmetic.py::TestArithmetic::test_subtraction_5_minus_2 PASSED
tests/test_arithmetic.py::TestArithmetic::test_multiplication_negative_numbers PASSED
tests/test_arithmetic.py::TestArithmetic::test_multiplication_by_zero PASSED
tests/test_arithmetic.py::TestArithmetic::test_division_5_by_2_integer PASSED
tests/test_arithmetic.py::TestArithmetic::test_division_5_by_2_quotient PASSED
tests/test_arithmetic.py::TestArithmetic::test_division_negative_by_positive PASSED
tests/test_arithmetic.py::TestArithmetic::test_division_by_zero_exception PASSED
tests/test_arithmetic.py::TestArithmetic::test_division_quotient_by_zero_exception PASSED
tests/test_calculator_service.py::TestCalculatorService::test_add PASSED
tests/test_calculator_service.py::TestCalculatorService::test_subtract PASSED
tests/test_calculator_service.py::TestCalculatorService::test_multiply PASSED
tests/test_calculator_service.py::TestCalculatorService::test_divide PASSED
tests/test_calculator_service.py::TestCalculatorService::test_division_by_zero PASSED
tests/test_calculator_service.py::TestCalculatorService::test_invalid_operator PASSED
tests/test_calculator_service.py::TestCalculatorService::test_is_valid_operator PASSED

============================= 18 passed in 0.03s ==============================
```

**결과**: ✅ **18개 테스트 모두 통과**

---

## 2. 코드 커버리지

### 실행 명령어
```bash
pytest --cov=src --cov-report=term-missing tests/
```

### 결과

| 파일 | Statements | Missing | Coverage |
|------|-----------|---------|----------|
| `src/arithmetic.py` | 20 | 0 | **100%** ✅ |
| `src/calculator_service.py` | 13 | 0 | **100%** ✅ |
| `src/calculator_presenter.py` | 67 | 67 | 0% |
| `src/console_app.py` | 79 | 79 | 0% |
| `src/gui/calculator_window.py` | 56 | 56 | 0% |
| `src/gui/button_factory.py` | 24 | 24 | 0% |
| `src/gui/display_widget.py` | 15 | 15 | 0% |
| **TOTAL** | **274** | **241** | **12%** |

**핵심 로직 커버리지**: ✅ **100%** (arithmetic.py, calculator_service.py)

**참고**: GUI 및 Presenter 코드는 단위 테스트에서 제외 (통합 테스트 필요)

---

## 3. Import 검증

### 검증 항목
- ✅ `from src.arithmetic import Arithmetic`
- ✅ `from src.calculator_service import CalculatorService`
- ✅ `from src.calculator_presenter import CalculatorPresenter`

### 결과
```
✅ All imports successful
```

**결과**: ✅ **모든 모듈 Import 정상**

---

## 4. 기본 연산 검증

### 검증 항목
- ✅ 덧셈: `Arithmetic.add(1, 2) == 3`
- ✅ 뺄셈: `Arithmetic.subtract(5, 2) == 3`
- ✅ 곱셈: `Arithmetic.multiply(2, 3) == 6`
- ✅ 나눗셈: `Arithmetic.divide(6, 2) == 3`

### 결과
```
✅ Basic arithmetic operations working
```

**결과**: ✅ **기본 연산 정상 동작**

---

## 5. CalculatorService 검증

### 검증 항목
- ✅ 덧셈: `CalculatorService.calculate(10, '+', 20) == 30`
- ✅ 뺄셈: `CalculatorService.calculate(10, '-', 5) == 5`
- ✅ 곱셈: `CalculatorService.calculate(3, '*', 4) == 12`
- ✅ 나눗셈: `CalculatorService.calculate(10, '/', 2) == 5.0`

### 결과
```
✅ CalculatorService working
```

**결과**: ✅ **CalculatorService 정상 동작**

---

## 6. 예외 처리 검증

### 검증 항목
- ✅ 0으로 나누기: `ArithmeticError` 발생 확인
- ✅ 잘못된 연산자: `ValueError` 발생 확인

### 결과
- ✅ 모든 예외 처리 정상 동작

---

## Sanity Test 체크리스트

### 필수 항목
- [x] 모든 단위 테스트 통과
- [x] 핵심 로직 커버리지 100%
- [x] 모든 모듈 Import 정상
- [x] 기본 연산 정상 동작
- [x] CalculatorService 정상 동작
- [x] 예외 처리 정상 동작

### 선택 항목
- [ ] GUI 실행 테스트 (수동)
- [ ] 콘솔 앱 실행 테스트 (수동)
- [ ] 통합 테스트

---

## 결론

### ✅ Sanity Test 결과: **PASS**

**모든 필수 항목 통과**

- ✅ 18개 단위 테스트 모두 통과
- ✅ 핵심 로직 (arithmetic, calculator_service) 커버리지 100%
- ✅ 모든 모듈 Import 정상
- ✅ 기본 연산 및 CalculatorService 정상 동작
- ✅ 예외 처리 정상 동작

### 권장 사항

1. **통합 테스트 추가**: GUI 및 Presenter 테스트
2. **수동 테스트**: GUI 및 콘솔 앱 실행 확인
3. **성능 테스트**: 대량 연산 처리 시간 확인

---

**작성일**: 2025-12-16  
**버전**: v1.0

