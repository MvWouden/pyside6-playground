import sys

from PySide6.QtWidgets import QApplication

from pyside6_playground.qt_02_table.table import TableWidget

if __name__ == "__main__":
    # Create the Qt Application
    app: QApplication = QApplication(sys.argv)

    # Create and show the main window
    widget: TableWidget = TableWidget()
    widget.resize(800, 600)
    widget.show()

    # Run the main Qt loop
    sys.exit(app.exec())
