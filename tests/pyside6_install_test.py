def test_pyside6_install() -> None:
    """Test the installation of PySide6.

    Ensures the PySide6 version is correct.
    Ensures the Qt compile version matches PySide6 version.
    """
    import PySide6.QtCore

    assert PySide6.__version__ == "6.5.2"
    assert PySide6.__version__ == PySide6.QtCore.__version__
