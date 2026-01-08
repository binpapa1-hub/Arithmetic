"""
계산기 프레젠터 - UI와 비즈니스 로직 사이의 중재자
SOLID 원칙: SRP, DIP
"""
from typing import Optional
from src.calculator_service import CalculatorService


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

