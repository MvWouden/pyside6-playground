from PySide6 import QtCore
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget

from __feature__ import snake_case, true_property  # noqa


class HelloWorldWidget(QWidget):
    """A Hello World widget with a button to toggle language."""

    def __init__(self: "HelloWorldWidget") -> None:
        """Initialise the widget."""
        super().__init__()
        self.layout: QVBoxLayout = QVBoxLayout(self)

        # Create button to cycle language
        self.button: QPushButton = QPushButton("Click me!")
        self.button.clicked.connect(self.magic)

        # Create display text
        self.hello: list[str] = [
            "Hello, World!",
            "Hallo, Wereld!",
            "Hallo, Welt!",
            "Bonjour, le monde!",
        ]
        self.text: QLabel = QLabel(
            text=self.hello[0], alignment=QtCore.Qt.AlignCenter
        )

        self.layout.add_widget(self.text)
        self.layout.add_widget(self.button)

    @QtCore.Slot()
    def magic(self: "HelloWorldWidget") -> None:
        """Cycle through language."""
        try:
            cur_idx: int = self.hello.index(str(self.text.text))
            next_idx: int = (cur_idx + 1) % len(self.hello)
        except ValueError:
            next_idx: int = 0

        self.text.text = self.hello[next_idx]
