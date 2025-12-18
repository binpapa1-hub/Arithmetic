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

