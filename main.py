from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Hello, Linux!\nThanks for packaging this, GitHub actions.\nI put it in the wrong spot so here's *ANOTHER* commit!")
label.show()
app.exec()