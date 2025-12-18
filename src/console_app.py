"""
사칙연산 콘솔 프로그램
리팩토링: 함수 분리, CalculatorService 사용, 에러 처리 추가
"""
import sys
from pathlib import Path

# 프로젝트 루트를 sys.path에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from typing import Optional
from src.calculator_service import CalculatorService


class Constants:
    """상수 정의 클래스"""
    SEPARATOR_LENGTH = 30
    SEPARATOR_CHAR = "="


def get_integer_input(prompt: str) -> Optional[int]:
    """
    정수 입력을 받습니다 (에러 처리 포함)
    
    Args:
        prompt: 입력 프롬프트 메시지
        
    Returns:
        입력된 정수값, 실패 시 None
    """
    while True:
        try:
            value = input(prompt)
            return int(value)
        except ValueError:
            print("❌ 올바른 정수를 입력해주세요.")
            retry = input("다시 시도하시겠습니까? (y/n): ").strip().lower()
            if retry != 'y':
                return None
        except KeyboardInterrupt:
            print("\n\n프로그램이 중단되었습니다.")
            return None


def get_operator_input() -> Optional[str]:
    """
    연산자 입력을 받습니다
    
    Returns:
        입력된 연산자, 실패 시 None
    """
    try:
        operator = input("연산자>> ").strip()
        if CalculatorService.is_valid_operator(operator):
            return operator
        else:
            print(f"❌ 지원하지 않는 연산자입니다: {operator}")
            print(f"지원 연산자: +, -, ×, *, /")
            return None
    except KeyboardInterrupt:
        print("\n\n프로그램이 중단되었습니다.")
        return None


def display_input_screen() -> None:
    """입력 화면을 표시합니다"""
    print("입력화면")
    print()


def display_result_screen(a: int, operator: str, b: int, result: float) -> None:
    """
    결과 화면을 표시합니다
    
    Args:
        a: 첫 번째 피연산자
        operator: 연산자
        b: 두 번째 피연산자
        result: 계산 결과
    """
    print("결과 뷰 화면")
    print()
    separator = Constants.SEPARATOR_CHAR * Constants.SEPARATOR_LENGTH
    print(separator)
    print()
    print(f"{a} {operator} {b}을 계산합니다.")
    print()
    print(separator)
    print()
    print(f"{a}{operator}{b}={result}입니다.")


def perform_calculation(a: int, operator: str, b: int) -> Optional[float]:
    """
    계산을 수행합니다
    
    Args:
        a: 첫 번째 피연산자
        operator: 연산자
        b: 두 번째 피연산자
        
    Returns:
        계산 결과, 실패 시 None
    """
    try:
        return CalculatorService.calculate(a, operator, b)
    except ArithmeticError as e:
        print(f"❌ 계산 오류: {e}")
        return None
    except ValueError as e:
        print(f"❌ 입력 오류: {e}")
        return None
    except Exception as e:
        print(f"❌ 예상치 못한 오류: {e}")
        return None


def main() -> None:
    """메인 함수"""
    display_input_screen()
    
    # 첫 번째 정수 입력
    a = get_integer_input("첫번째 정수값>> ")
    if a is None:
        return
    print()
    
    # 연산자 입력
    operator = get_operator_input()
    if operator is None:
        return
    print()
    
    # 두 번째 정수 입력
    b = get_integer_input("두번째 정수값>> ")
    if b is None:
        return
    print()
    
    # 계산 수행
    result = perform_calculation(a, operator, b)
    if result is None:
        return
    
    # 결과 표시
    display_result_screen(a, operator, b, result)


if __name__ == "__main__":
    main()
