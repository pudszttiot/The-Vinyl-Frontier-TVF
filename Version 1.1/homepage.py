import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QAction, QMenu, QMenuBar, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from main import WebBrowser

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Vinyl Frontier (TVF)")
        self.setFixedSize(800, 600)  # Increased window size
        self.setGeometry(300, 100, 800, 600)
        self.setWindowIcon(QIcon(r"..\Images\TVF.ico"))

        # Set background image for the main window
        background_label = QLabel(self)
        background_label.setGeometry(0, 0, 800, 600)  # Set the size to cover the entire window
        background_pixmap = QPixmap(r"..\Images\TVFBackground.png")  # Provide the path to your background image
        background_label.setPixmap(background_pixmap)

        # Create a QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setGeometry(150, 30, 500, 470)  # Adjust the position and size as needed

        # Load the image
        pixmap = QPixmap(r"..\Images\The Vinyl Frontier 3.png")  # Provide the path to your image file

        # Set custom width and height for the image
        width = 500  # Set your desired width
        height = 470  # Set your desired height
        scaled_pixmap = pixmap.scaled(width, height)
        self.image_label.setPixmap(scaled_pixmap)

        # Create a button to open the content page
        self.open_button = QPushButton("Open The Vinyl Frontier (TVF)", self)
        self.open_button.setGeometry(285, 525, 250, 50)
        self.open_button.clicked.connect(self.open_content_page)

        # Apply custom style to the button (same as before)
        self.open_button.setStyleSheet(
            """
            QPushButton {
                background-color: #4b46b8;
                color: #ffffff;
                border: 2px solid #ffffff;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #e30b96;
                color: #000000;
                border: 2px solid #000000;
                border-radius: 5px;
            }
            """
        )

        # Create a menu bar
        menubar = self.menuBar()

        # Create a "File" menu
        file_menu = menubar.addMenu("File")

        # Create an "Exit" action
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Create a "Help" menu
        help_menu = menubar.addMenu("Help")

        # Create a "How to Use" action
        how_to_use_action = QAction("How to Use", self)
        how_to_use_action.triggered.connect(self.show_how_to_use)
        help_menu.addAction(how_to_use_action)

    def open_content_page(self):
        # Open the content page frame (imported from your existing code)
        self.content_page = WebBrowser()
        self.content_page.show()

        # Close the home page
        self.close()

    def show_how_to_use(self):
        # Create an HTML-formatted message for the "How to Use" instructions
        how_to_use_text = """
        <html>
        <body>
        <h2 style="color: #e30b96;">How to Use</h2>
        <p>Welcome to The Vinyl Frontier (TVF) application!</p>
        <ol>
            <li>Click the <span style="font-weight: bold;">'Open The Vinyl Frontier (TVF)'</span> button to open the content page.</li>
            <li>Use the content page to explore The Vinyl Frontier (TVF).</li>
        </ol>
        <p>Enjoy your vinyl journey!</p>
        </body>
        </html>
        """

        QMessageBox.information(self, "Help", how_to_use_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    homepage = HomePage()
    homepage.show()
    sys.exit(app.exec_())
