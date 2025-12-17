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
