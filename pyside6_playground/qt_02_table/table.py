from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

from pyside6_playground.qt_02_table.constants import COLOURS
from pyside6_playground.qt_02_table.utils import qcolor_from_hex

from __feature__ import snake_case, true_property  # noqa


class TableWidget(QTableWidget):
    """A table widget."""

    row_count: int
    column_count: int
    horizontal_header_labels: list[str]
    item: list[list[QTableWidgetItem]]

    def __init__(self: "TableWidget") -> None:
        """Initialise the widget."""
        super().__init__()

        self.window_title: str = "Table"

        self.init_table()
        self.insert_colours()

    def init_table(self: "TableWidget") -> None:
        """Initialise the table."""
        self.row_count = len(COLOURS)
        self.column_count = 1 + len(COLOURS[0]) if COLOURS else 0
        self.horizontal_header_labels = ["Name", "Hex Code", "Colour"]

    def insert_colours(self: "TableWidget") -> None:
        """Insert the colours into the table."""
        for i, (name, color_hex) in enumerate(COLOURS):
            item_name: QTableWidgetItem = QTableWidgetItem(name)
            item_hex: QTableWidgetItem = QTableWidgetItem(color_hex)
            item_colour: QTableWidgetItem = QTableWidgetItem()
            item_colour.set_background(qcolor_from_hex(color_hex))

            self.set_item(i, 0, item_name)
            self.set_item(i, 1, item_hex)
            self.set_item(i, 2, item_colour)
