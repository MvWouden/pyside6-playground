from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem

from pyside6_playground.qt_03_tree.constants import FILES

from __feature__ import snake_case, true_property  # noqa


class TreeWidget(QTreeWidget):
    """A tree widget."""

    column_count: int
    header_labels: list[str]

    def __init__(self: "TreeWidget") -> None:
        """Initialise the widget."""
        super().__init__()

        self.window_title: str = "Tree"

        self.init_tree()
        self.insert_structure()

    def init_tree(self: "TreeWidget") -> None:
        """Initialise the tree."""
        self.column_count = 2
        self.set_header_labels(["Name", "Type"])

    def insert_structure(self: "TreeWidget") -> None:
        """Parse the structure and insert it into the tree."""
        for directory, files in FILES.items():
            item_directory: QTreeWidgetItem = QTreeWidgetItem(
                [directory, "Directory"]
            )
            self.add_top_level_item(item_directory)

            for file in files:
                item_file: QTreeWidgetItem = QTreeWidgetItem([file, "File"])
                item_directory.add_child(item_file)
