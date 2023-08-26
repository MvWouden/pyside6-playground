import sys

from PySide6.QtWidgets import QApplication

from pyside6_playground.qt_00_hello_world.hello_world import HelloWorldWidget

if __name__ == "__main__":
    # Create the Qt Application
    app: QApplication = QApplication([])

    # Create and show the main window
    widget: HelloWorldWidget = HelloWorldWidget()
    widget.resize(800, 600)
    widget.show()

    # Run the main Qt loop
    sys.exit(app.exec())
