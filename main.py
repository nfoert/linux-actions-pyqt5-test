from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Hello, Linux!\nThanks for packaging this, GitHub actions.\nIt didn't seem to have my changes so here's another commit for ya!")
label.show()
app.exec()