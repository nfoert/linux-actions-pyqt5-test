from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Hello, Linux!\nThanks for packaging this, GitHub actions.\nAnd another.......") # There's got to be a faster way to test this...
label.show()
app.exec()