import sys

from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import *


class Window(QMainWindow):
    """Main Window."""
    filename = ''
    def __init__(self):
        """Initializer."""
        QMainWindow.__init__(self, parent=None)

        #CENTRAL WIDGET
        window = QWidget()
        layout = QGridLayout()

        layout.addWidget(QLabel('Select sequence file'), 0, 0)
        layout.addWidget(QLineEdit(), 1, 0)

        browse_btn = QPushButton('Browse')
        browse_btn.clicked.connect(self._browse_file)
        layout.addWidget(browse_btn, 1, 1)

        layout.addWidget(QLabel('Scan Bar Code'), 2, 0)
        layout.addWidget(QLineEdit(), 3, 0)

        start_btn = QPushButton("START")
        layout.addWidget(start_btn, 4, 0)

        browser = QWebEngineView()
        browser.setUrl(QUrl("http://www.google.com"))

        layout.addWidget(browser, 5, 0)

        window.setLayout(layout)

        #Ustawienia okna
        self.setWindowTitle('PyTestDev')
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(window)
        self._createMenu()
        self._createStatusBar()

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("PyTestDev")
        self.setStatusBar(status)

    def _browse_file(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Python file (*.py);;"
                                                  "All files (*.*)")
        #TODO: teraz uzyc tego pliku i pokazac jego nazwe w odpowiednim EdiLine.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())