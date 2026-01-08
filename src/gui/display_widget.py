"""
디스플레이 위젯 - 계산 결과 표시
"""
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class DisplayWidget(QLabel):
    """계산기 디스플레이 위젯"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """UI 설정"""
        self.setText("0")
        self.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        
        # 폰트 설정
        font = QFont("Arial", 24, QFont.Weight.Bold)
        self.setFont(font)
        
        # 스타일 설정
        self.setStyleSheet("""
            QLabel {
                background-color: #1e1e1e;
                color: #ffffff;
                border: 2px solid #333;
                border-radius: 5px;
                padding: 10px;
                min-height: 60px;
            }
        """)
    
    def update_display(self, value: str):
        """디스플레이 업데이트"""
        self.setText(value)

