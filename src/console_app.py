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

