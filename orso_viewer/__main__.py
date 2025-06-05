import sys

from orso_viewer.main_window import MainWindow

from PySide6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    if len(sys.argv) > 1:
        window.read_file(sys.argv[1])

    sys.exit(app.exec())


if __name__ == "__main__":
    main()