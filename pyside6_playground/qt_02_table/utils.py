from PySide6.QtGui import QColor


def qcolor_from_hex(color_hex: str) -> QColor:
    """Convert a hex string to a QColor.

    Parameters
    ----------
    color_hex : str
        A hex string representing a colour.

    Returns
    -------
    QColor
        A QColor object.

    Raises
    ------
    ValueError
        If the hex string is invalid.
    """
    color_hex = color_hex.lstrip("#")

    # Validate hex string
    if len(color_hex) != 6 or not all(
        c in "0123456789abcdef" for c in color_hex.lower()
    ):
        raise ValueError(f"Invalid hex string '{color_hex}'")

    # Convert hex string to RGB
    r: int = int(color_hex[0:2], 16)
    g: int = int(color_hex[2:4], 16)
    b: int = int(color_hex[4:6], 16)

    # Create QColor object
    return QColor(r, g, b)
