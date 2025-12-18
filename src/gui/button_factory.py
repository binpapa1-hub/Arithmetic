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

