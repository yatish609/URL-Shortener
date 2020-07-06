from PyQt5 import QtCore, QtGui, QtWidgets
import core

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(786, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shortenButton = QtWidgets.QPushButton(self.centralwidget)
        self.shortenButton.setGeometry(QtCore.QRect(660, 130, 111, 51))
        self.shortenButton.setObjectName("shortenButton")
        self.linkLabel = QtWidgets.QLabel(self.centralwidget)
        self.linkLabel.setGeometry(QtCore.QRect(20, 140, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.linkLabel.setFont(font)
        self.linkLabel.setObjectName("linkLabel")
        self.inputURL = QtWidgets.QLineEdit(self.centralwidget)
        self.inputURL.setGeometry(QtCore.QRect(90, 150, 531, 22))
        self.inputURL.setObjectName("inputURL")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 30, 491, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/yatis/Pictures/url-shortener.png"))
        self.label.setObjectName("label")
        self.shortenedLinkLabel = QtWidgets.QLabel(self.centralwidget)
        self.shortenedLinkLabel.setGeometry(QtCore.QRect(20, 200, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.shortenedLinkLabel.setFont(font)
        self.shortenedLinkLabel.setObjectName("shortenedLinkLabel")
        self.shortenedURL = QtWidgets.QLineEdit(self.centralwidget)
        self.shortenedURL.setGeometry(QtCore.QRect(190, 210, 431, 22))
        self.shortenedURL.setObjectName("shortenedURL")
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(230, 260, 321, 21))
        font = QtGui.QFont()
        font.setFamily("HoloLens MDL2 Assets")
        font.setPointSize(10)
        self.resultLabel.setFont(font)
        self.resultLabel.setText("")
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setObjectName("resultLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.shortenButton.clicked.connect(self.shortenURL)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "URL Shortener"))
        self.shortenButton.setText(_translate("MainWindow", "Shorten"))
        self.linkLabel.setText(_translate("MainWindow", "Link:"))
        self.shortenedLinkLabel.setText(_translate("MainWindow", "Shortened URL:"))

    def shortenURL(self):
        originalURL = self.inputURL.text().strip()
        if(core.checkURL(originalURL)):
            self.inputURL.setText(originalURL)
            shortURL = core.createURL(originalURL)
            self.shortenedURL.setText(shortURL)
            self.resultLabel.setText('Successfully shortened URL!')
        else:
            self.resultLabel.setText('Invalid URL!')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
