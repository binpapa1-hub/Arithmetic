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

