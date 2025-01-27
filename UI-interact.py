import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

def on_button_click():
    label.setText("Clickou!")

app = QApplication(sys.argv)

# Main Window
window = QWidget()
window.setWindowTitle("PyQt5 UI")

# Widgets
label = QLabel("Ola mundo!")
button = QPushButton("Click")
button.clicked.connect(on_button_click)

# Layout
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)

window.show()
sys.exit(app.exec_())


