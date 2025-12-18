"""
계산기 서비스 - 비즈니스 로직 담당
SOLID 원칙: SRP (단일 책임), DIP (의존성 역전)
"""
from typing import Dict, Callable
from src.arithmetic import Arithmetic


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

