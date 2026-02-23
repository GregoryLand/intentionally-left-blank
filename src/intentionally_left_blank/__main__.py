import sys
from PySide6.QtCore import Qt
from PySide6 import QtGui
from PySide6 import QtWidgets
from typing import Final

DEFAULT_TOOL_TIP_TEXT: Final[str] = "Intentionally Left Blank"
DEFAULT_APP_NAME: Final[str] = "intentionally-left-blank"
#DEFAULT_APP_ORGANIZATION : Final[str] = "None"
DEFAULT_OPACITY: Final[float] = 0.5

def main() -> int:
    app = QtWidgets.QApplication(sys.argv)
#    app.setOrganizationName(DEFAULT_APP_ORGANIZATION)
    app.setApplicationName(DEFAULT_APP_NAME)
    app.setDesktopFileName(DEFAULT_APP_NAME)
    app.setPalette(QtGui.QColor.fromRgb(0,0,0))

    mainWindow = QtWidgets.QMainWindow()
    mainWindow.setToolTip(DEFAULT_TOOL_TIP_TEXT)
    mainWindow.setWindowOpacity(DEFAULT_OPACITY)
    mainWindow.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
