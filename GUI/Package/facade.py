from Package.interface import Ui_MainWindow
from Package.database_functional import ConnectionFunctions


class Facade:
    def add(Ui_MainWindow: Ui_MainWindow):
        ConnectionFunctions.clicked_add(Ui_MainWindow)

    def delete(Ui_MainWindow: Ui_MainWindow):
        ConnectionFunctions.clicked_delete(Ui_MainWindow)

    def update(Ui_MainWindow: Ui_MainWindow):
        ConnectionFunctions.clicked_update(Ui_MainWindow)

    def search(Ui_MainWindow: Ui_MainWindow):
        ConnectionFunctions.clicked_search(Ui_MainWindow)
