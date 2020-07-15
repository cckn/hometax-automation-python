import sys
from PyQt5.QtWidgets import *
from src import main, web_config


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.worker = main.Worker()
        self.worker.start()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        self.checkBox1 = QCheckBox("메세지박스 ON/OFF", self)
        self.checkBox1.stateChanged.connect(self.checkBoxState)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def checkBoxState(self):
        msg = ""
        if self.checkBox1.isChecked() == True:
            web_config.config.wanna_alert_kill = True

        self.statusBar.showMessage(msg)


def init():
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()


if __name__ == "__main__":
    init()
