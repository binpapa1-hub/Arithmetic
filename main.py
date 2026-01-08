"""
GUI 계산기 실행 진입점
"""
import sys
from PyQt6.QtWidgets import QApplication
from src.gui.calculator_window import CalculatorWindow


def main():
    """메인 함수"""
    app = QApplication(sys.argv)
    
    window = CalculatorWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

