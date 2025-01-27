import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget


# Subclass QMainWindow to customize application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        # Windows Title
        self.setWindowTitle("My App")
        
        # Button
        button = QPushButton("Press me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)
        
        # Windows Size and Button Position
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked

        print(self.button_is_checked)
app = QApplication(sys.argv)

# Create Window with the programm
window = MainWindow()
# Windows are hidden by default
window.show()


# Start the event loop
app.exec()



# https://www.pythonguis.com/tutorials/pyqt6-signals-slots-events/ Learning Website