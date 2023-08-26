import sys

from PySide6.QtWidgets import QApplication

from pyside6_playground.qt_01_dialog.dialog import DialogWidget

if __name__ == "__main__":
    # Create the Qt Application
    app: QApplication = QApplication(sys.argv)

    # Create and show the main window
    widget: DialogWidget = DialogWidget()
    widget.show()

    # Run the main Qt loop
    sys.exit(app.exec())
