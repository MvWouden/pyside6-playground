from PySide6 import QtCore
from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout

from __feature__ import snake_case, true_property  # noqa


class DialogWidget(QDialog):
    """A dialog widget."""

    def __init__(self: "DialogWidget") -> None:
        """Initialise the widget."""
        super().__init__()

        self.window_title: str = "Dialog"

        # Create widgets
        self.edit: QLineEdit = QLineEdit("John Doe")
        self.button: QPushButton = QPushButton("Greet")

        # Create layout
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.layout.add_widget(self.edit)
        self.layout.add_widget(self.button)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.greet)

    @QtCore.Slot()
    def greet(self: "DialogWidget") -> None:
        """Greet the user."""
        print(f"Hello, {self.edit.text}!")
