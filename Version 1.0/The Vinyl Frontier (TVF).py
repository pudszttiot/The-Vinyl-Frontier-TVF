import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

def open_webview():
    """
    Function to open a web view of the Discogs website and handle file downloads.
    """
    app = QApplication(sys.argv)
    window = QMainWindow()
    central_widget = QWidget()
    layout = QVBoxLayout(central_widget)
    webview = QWebEngineView()
    loading_label = QLabel("Loading, please wait...")  # Create a loading label

    # Apply a zoom factor to make the text smaller (0.8 means 80% of the original size)
    webview.setZoomFactor(0.8)

    # Function to hide the loading label when the page is fully loaded
    def hide_loading_label():
        loading_label.hide()

    # Create a custom download handler
    def download_requested(download):
        # Prompt the user to choose the download path
        save_path, _ = QFileDialog.getSaveFileName(window, "Save File", os.path.expanduser("~"), "All Files (*.*)")
        if save_path:
            download.setPath(save_path)
            download.accept()

    # Set the custom download handler for the web view
    profile = QWebEngineProfile.defaultProfile()
    profile.downloadRequested.connect(download_requested)

    webview.loadFinished.connect(hide_loading_label)  # Connect the hide_loading_label function to the loadFinished signal

    webview.load(QUrl('https://www.discogs.com/'))

    layout.addWidget(webview)
    layout.addWidget(loading_label)  # Add the loading label to the layout

    window.setCentralWidget(central_widget)
    window.setWindowTitle('The Vinyl Frontier (TVF)')
    window.setGeometry(100, 100, 890, 450)

    # Set the window icon
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'G:\Software\py\Python Creations\Completed\Projects\The Vinyl Frontier (TVF)\Images\TVF.ico')
    window.setWindowIcon(QIcon(icon_path))

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    button = QPushButton('Click for The Vinyl Frontier (TVF)')
    button.clicked.connect(open_webview)
    layout = QVBoxLayout()
    layout.addWidget(button)
    central_widget = QWidget()
    central_widget.setLayout(layout)
    window = QMainWindow()
    window.setCentralWidget(central_widget)
    window.setWindowTitle('The Vinyl Frontier (TVF)')
    window.setGeometry(100, 100, 300, 100)

    # Set the window icon
    icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'G:\Software\py\Python Creations\Completed\Projects\The Vinyl Frontier (TVF)\Images\TVF.ico')
    window.setWindowIcon(QIcon(icon_path))

    window.show()
