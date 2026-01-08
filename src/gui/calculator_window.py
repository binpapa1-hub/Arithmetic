"""
계산기 메인 윈도우
"""
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QGridLayout, QMessageBox
from PyQt6.QtCore import Qt
from src.gui.display_widget import DisplayWidget
from src.gui.button_factory import ButtonFactory
from src.calculator_presenter import CalculatorPresenter


class CalculatorWindow(QMainWindow):
    """계산기 메인 윈도우"""
    
    def __init__(self):
        super().__init__()
        self.presenter = CalculatorPresenter(self)
        self.setup_ui()
    
    def setup_ui(self):
        """UI 초기 설정"""
        self.setWindowTitle("계산기")
        self.setFixedSize(300, 450)  # 나누기 버튼 추가로 높이 증가
        
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
        
        # 버튼 배치 (5x4 그리드)
        buttons = [
            # Row 1
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("×", 0, 3),
            # Row 2
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("-", 1, 3),
            # Row 3
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("+", 2, 3),
            # Row 4
            ("+/-", 3, 0), ("0", 3, 1), (".", 3, 2), ("/", 3, 3),
            # Row 5
            ("=", 4, 0, 1, 2),  # 등호 버튼 (2칸 너비)
        ]
        
        for button_info in buttons:
            # 버튼 정보 파싱 (row, col, rowspan, colspan 지원)
            if len(button_info) == 3:
                text, row, col = button_info
                rowspan, colspan = 1, 1
            elif len(button_info) == 5:
                text, row, col, rowspan, colspan = button_info
            else:
                continue
            
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
            
            layout.addWidget(button, row, col, rowspan, colspan)
        
        # Clear 버튼 추가 (등호 버튼 옆에)
        clear_button = factory.create_function_button("C")
        clear_button.clicked.connect(self.presenter.handle_clear)
        layout.addWidget(clear_button, 4, 2, 1, 2)  # 2칸 너비
    
    def update_display(self, value: str):
        """디스플레이 업데이트 (Presenter에서 호출)"""
        self.display.update_display(value)
    
    def show_error(self, message: str):
        """에러 메시지 표시"""
        QMessageBox.warning(self, "오류", message)

