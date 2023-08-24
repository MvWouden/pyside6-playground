import sys

from PySide6.QtWidgets import QApplication

from pyside6_playground.qt_hello_world.hello_world import HelloWorldWidget

if __name__ == "__main__":
    app: QApplication = QApplication([])

    widget: HelloWorldWidget = HelloWorldWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
