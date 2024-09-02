# /auto-manhua-editor/auto-manhua-editor/src/ui/main_window.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto Manhua Editor")
        self.setGeometry(100, 100, 800, 600)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())