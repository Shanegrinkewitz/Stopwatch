from PyQt6.QtCore import Qt, QTime, QSize
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stopwatch")

        vbox = QVBoxLayout()

        self.resize(QSize(400, 600))

        self.timer_label = QLabel("00:00:00:0")
        self.timer_label.setFont(QFont("Arial", 48))
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.timer_label)

        self.middle_widget = QWidget()
        self.middle_layout = QVBoxLayout()
        self.middle_widget.setLayout(self.middle_layout)
        vbox.addWidget(self.middle_widget)

        self.bottom_widget = QWidget()
        self.bottom_layout = QHBoxLayout()
        self.bottom_widget.setLayout(self.bottom_layout)

        self.bottom_layout.setSpacing(20)

        self.start_stop_button = QPushButton("Start")
        self.start_stop_button.setFixedSize(QSize(100, 50))
        self.bottom_layout.addWidget(self.start_stop_button)

        self.lap_reset_button = QPushButton("Lap")
        self.lap_reset_button.setFixedSize(QSize(100, 50))
        self.bottom_layout.addWidget(self.lap_reset_button)

        vbox.addWidget(self.bottom_widget)

        self.time = QTime(0, 0)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Stopwatch")
    
    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()