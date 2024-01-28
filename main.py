from PyQt5.QtWidgets import QApplication

from mains.mainconnector import MainConnector


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    connector = MainConnector()
    sys.exit(app.exec_())