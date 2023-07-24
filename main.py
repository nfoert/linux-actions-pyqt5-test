from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Hello, Linux!\nThanks for packaging this, GitHub actions.\nAnd another...")
label.show()
app.exec()