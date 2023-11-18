from PySide6.QtUiTools import QUiLoader


ui_file = QFile("UI.ui")
ui_file.open(QFile.ReadOnly)

loader = QUiLoader()
window = loader.load(ui_file)
window.show()