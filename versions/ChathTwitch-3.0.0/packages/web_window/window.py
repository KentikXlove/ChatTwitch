from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon


class WebWindow(QMainWindow):
    """
    Окно с встроенным браузером на QtWebEngine.
    """
    def __init__(self, url: str, title: str = "Simple Web Window",
                 width: int = 800, height: int = 600,
                 icon_path: str = None, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.resize(width, height)
        if icon_path:
            self.setWindowIcon(QIcon(icon_path))

        self.webview = QWebEngineView()
        self.webview.setUrl(QUrl(url))
        self.setCentralWidget(self.webview)


def run_window(url: str, title: str = "Simple Web Window",
               width: int = 800, height: int = 600,
               icon_path: str = None, parent=None) -> int:
    app = QApplication.instance()
    if app is None:
        app = QApplication([])

    window = WebWindow(url, title, width, height, icon_path, parent)   # <-- исправлено
    window.show()
    return app.exec_()