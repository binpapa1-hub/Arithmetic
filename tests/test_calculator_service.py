"""CalculatorService 테스트"""
import pytest
from src.calculator_service import CalculatorService


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

