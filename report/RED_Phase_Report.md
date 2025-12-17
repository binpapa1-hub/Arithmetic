# RED 단계 작업 리포트

## 프로젝트 정보

- **프로젝트명**: 인사관리 앱 시스템 구축 (정산 시스템)
- **테스트 ID**: TC-CMM-001 / TC-AO-001
- **작성자**: 홍길동
- **승인자**: 박문수
- **작성일**: 2020-09-01
- **버전**: v1.0
- **테스트 범위**: 공통 모듈
- **테스트 조직**: 개발팀
- **작업 단계**: RED (Test-Driven Development)

---

## 작업 일정

| 날짜 | 작업 내용 | 상태 |
|------|----------|------|
| 2020-09-01 | 프로젝트 초기 설정 및 구조 생성 | 완료 |
| 2020-09-01 | 테스트 케이스 작성 | 완료 |
| 2020-09-01 | RED 단계 테스트 실행 및 검증 | 완료 |

---

## 1. 프로젝트 초기 설정

### 1.1 프로젝트 구조 생성

```
Arithmetic/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   └── arithmetic.py
└── tests/
    ├── __init__.py
    └── test_arithmetic.py
```

### 1.2 Git 저장소 설정

- Git 저장소 초기화 완료
- GitHub 원격 저장소 연결: `https://github.com/binpapa1-hub/Arithmetic.git`
- 브랜치 전략:
  - `main`: 메인 브랜치
  - `RED`: RED 단계 작업 브랜치 (현재 작업 중)

### 1.3 의존성 관리

**requirements.txt**
```
pytest>=7.0.0
pytest-cov>=7.0.0
```

---

## 2. 테스트 케이스 작성

### 2.1 테스트 케이스 목록

총 **10개의 테스트 케이스**를 작성했습니다.

#### 덧셈 테스트 (3개)

1. **test_addition_1_plus_10**
   - 입력: `1, 10`
   - 예상값: `11`
   - 중요도: 중요

2. **test_addition_0_plus_1**
   - 입력: `0, 1`
   - 예상값: `1`
   - 중요도: 중요

3. **test_addition_negative_numbers**
   - 입력: `-1, -10`
   - 예상값: `-11`
   - 중요도: 보통

#### 뺄셈 테스트 (1개)

4. **test_subtraction_5_minus_2**
   - 입력: `5, 2`
   - 예상값: `3`
   - 중요도: 중요

#### 곱셈 테스트 (2개)

5. **test_multiplication_negative_numbers**
   - 입력: `-5, -3`
   - 예상값: `15`
   - 중요도: 보통

6. **test_multiplication_by_zero**
   - 입력: `0, 10`
   - 예상값: `0`
   - 중요도: 낮음

#### 나눗셈 테스트 (3개)

7. **test_division_5_by_2_integer**
   - 입력: `5, 2`
   - 예상값: `2` (정수 나눗셈)
   - 중요도: 중요

8. **test_division_5_by_2_quotient**
   - 입력: `5, 2`
   - 예상값: `2.5` (몫, 소수점 포함)
   - 중요도: 보통

9. **test_division_negative_by_positive**
   - 입력: `-10, 2`
   - 예상값: `-5`
   - 중요도: 중요

#### 예외 처리 테스트 (1개)

10. **test_division_by_zero_exception**
    - 입력: `0, 0`
    - 예상값: `ArithmeticError` 예외 발생
    - 중요도: 중요

---

## 3. 구현 코드 상태 (RED 단계)

### 3.1 현재 구현 상태

**src/arithmetic.py**

```python
class Arithmetic:
    """사칙연산을 수행하는 클래스"""
    
    @staticmethod
    def add(a, b):
        """두 수를 더합니다"""
        pass
    
    @staticmethod
    def subtract(a, b):
        """두 수를 뺍니다"""
        pass
    
    @staticmethod
    def multiply(a, b):
        """두 수를 곱합니다"""
        pass
    
    @staticmethod
    def divide(a, b):
        """두 수를 나눕니다 (정수 나눗셈)"""
        pass
    
    @staticmethod
    def divide_quotient(a, b):
        """두 수를 나눕니다 (몫, 소수점 포함)"""
        pass
```

**상태**: 모든 메서드가 `pass`만 포함하여 구현되지 않음 (RED 단계 의도)

---

## 4. 테스트 실행 결과

### 4.1 전체 테스트 실행 결과

```
============================= test session starts =============================
platform win32 -- Python 3.10.11, pytest-9.0.2, pluggy-1.6.0
collected 10 items

tests\test_arithmetic.py FFFFFFFFFF                                      [100%]

================================== FAILURES ===================================
[모든 테스트 실패]
============================= 10 failed in 0.10s ==============================
```

### 4.2 개별 테스트 실패 상세

| 테스트 케이스 | 실패 원인 | 상태 |
|--------------|----------|------|
| test_addition_1_plus_10 | `assert None == 11` | ✅ 예상된 실패 |
| test_addition_0_plus_1 | `assert None == 1` | ✅ 예상된 실패 |
| test_addition_negative_numbers | `assert None == -11` | ✅ 예상된 실패 |
| test_subtraction_5_minus_2 | `assert None == 3` | ✅ 예상된 실패 |
| test_multiplication_negative_numbers | `assert None == 15` | ✅ 예상된 실패 |
| test_multiplication_by_zero | `assert None == 0` | ✅ 예상된 실패 |
| test_division_5_by_2_integer | `assert None == 2` | ✅ 예상된 실패 |
| test_division_5_by_2_quotient | `assert None == 2.5` | ✅ 예상된 실패 |
| test_division_negative_by_positive | `assert None == -5` | ✅ 예상된 실패 |
| test_division_by_zero_exception | `Failed: DID NOT RAISE ArithmeticError` | ✅ 예상된 실패 |

**결론**: 모든 테스트가 예상대로 실패했습니다. RED 단계 목표 달성.

---

## 5. 테스트 커버리지

### 5.1 커버리지 결과

```
Name                Stmts   Miss  Cover   Missing
-------------------------------------------------
src\__init__.py         0      0   100%
src\arithmetic.py      16      0   100%
-------------------------------------------------
TOTAL                  16      0   100%
```

### 5.2 커버리지 분석

- **코드 커버리지**: 100%
  - 모든 함수가 호출되어 `pass` 문이 실행됨
  - 함수 시그니처는 모두 테스트됨

- **구현 상태**: 미구현
  - 모든 함수가 `pass`만 포함
  - 실제 로직이 없어 테스트 실패

---

## 6. RED 단계 완료 확인

### 6.1 완료 항목

- ✅ 프로젝트 구조 생성
- ✅ 테스트 케이스 작성 (10개)
- ✅ 모든 테스트 실행 및 실패 확인
- ✅ 테스트 커버리지 확인 (100%)
- ✅ Git 커밋 및 푸시 완료

### 6.2 RED 단계 목표 달성

**RED 단계의 목표**: 실패하는 테스트를 작성하는 것

- ✅ 모든 테스트 케이스 작성 완료
- ✅ 모든 테스트가 예상대로 실패함
- ✅ 코드는 호출되지만 구현이 없어 실패함

---

## 7. 다음 단계 (GREEN)

### 7.1 GREEN 단계 계획

다음 단계에서는 다음 작업을 수행합니다:

1. **구현 작업**
   - `Arithmetic.add()` 구현
   - `Arithmetic.subtract()` 구현
   - `Arithmetic.multiply()` 구현
   - `Arithmetic.divide()` 구현 (정수 나눗셈)
   - `Arithmetic.divide_quotient()` 구현 (소수점 포함)
   - 예외 처리 구현 (0으로 나누기)

2. **테스트 통과 확인**
   - 모든 테스트가 통과하는지 확인
   - 테스트 커버리지 재확인

3. **커밋 및 푸시**
   - GREEN 브랜치 생성
   - 구현 코드 커밋
   - 원격 저장소에 푸시

---

## 8. 참고 사항

### 8.1 테스트 환경

- **언어**: Python 3.10.11
- **테스트 프레임워크**: pytest 9.0.2
- **커버리지 도구**: pytest-cov 7.0.0
- **운영 체제**: Windows 10

### 8.2 Git 브랜치 전략

- `main`: 메인 브랜치
- `RED`: RED 단계 작업 브랜치 (현재)
- `GREEN`: GREEN 단계 작업 브랜치 (예정)
- `REFACTOR`: REFACTOR 단계 작업 브랜치 (예정)

---

## 9. 결론

RED 단계가 성공적으로 완료되었습니다. 모든 테스트 케이스가 작성되었고, 예상대로 실패하는 것을 확인했습니다. 이제 GREEN 단계로 진행하여 테스트를 통과시키는 최소한의 코드를 구현할 준비가 되었습니다.

---

**작성일**: 2025-12-16  
**작성자**: 개발팀  
**문서 버전**: v1.0

