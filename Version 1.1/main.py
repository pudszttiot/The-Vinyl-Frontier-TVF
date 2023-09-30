import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("The Vinyl Frontier (TVF)")
        self.setFixedSize(900, 600)
        self.setGeometry(200, 100, 900, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.browser = QWebEngineView()
        self.layout.addWidget(self.browser)

        # Open the URL when the application starts
        url = QUrl("https://www.discogs.com/search/advanced?ev=em_as")
        self.browser.setUrl(url)

        # Zoom out to 80%
        self.browser.setZoomFactor(0.8)  # 80% zoom

def main():
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebBrowser()
    window.show()
    sys.exit(app.exec_())
