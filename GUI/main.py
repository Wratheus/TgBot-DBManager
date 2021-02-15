from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QWidget, QVBoxLayout, QGridLayout, QDialogButtonBox, QLabel, QLineEdit, QComboBox
import sys


class MainWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.tab_instance = QTabWidget()  # tabs instance
        self.vbox_lay = QVBoxLayout()  # vbox instance
        self.InitializeUI()

    def InitializeUI(self):
        self.setWindowTitle('DataBase Edit Tool')
        self.setGeometry(250, 320, 350, 250)

        self.tab_instance.addTab(FirstTab(), "Manage DB")
        self.tab_instance.addTab(SecondTab(), "Edit")
        self.tab_instance.addTab(SecondTab(), "Console")

        self.vbox_lay.addWidget(self.tab_instance)
        self.setLayout(self.vbox_lay)

        self.show()


class FirstTab(QWidget):
    def __init__(self):
        super().__init__()
        self.ColumnSelectBoxList = ['Teachers', 'Students', 'Subjects', 'Time']
        self.first_tab_layout = QGridLayout()

        self.AddText = QLabel("Add new line")
        self.AddEdit = QLineEdit()
        self.AddColumnText = QLabel("To")
        self.AddColumnSelectBox = QComboBox()
        self.AddColumnSelectBox.addItems(self.ColumnSelectBoxList)

        self.RemoveText = QLabel("Remove line")
        self.RemoveEdit = QLineEdit()
        self.RemoveLineText = QLabel("from")
        self.RemoveLineSelectBox = QComboBox()
        self.RemoveLineSelectBox.addItems(self.ColumnSelectBoxList)

        self.NewColumn = QLabel("Create new column")
        self.NewColumnEdit = QLineEdit()

        self.RemoveColumnText = QLabel("Remove Column")
        self.RemoveColumnSelectBox = QComboBox()
        self.RemoveColumnSelectBox.addItems(self.ColumnSelectBoxList)

        self.InitializeUI()

    def InitializeUI(self):
        self.first_tab_layout.addWidget(self.AddText, 1, 0)
        self.first_tab_layout.addWidget(self.AddEdit, 1, 1)
        self.first_tab_layout.addWidget(self.AddColumnText, 1, 2)
        self.first_tab_layout.addWidget(self.AddColumnSelectBox, 1, 3)

        self.first_tab_layout.addWidget(self.RemoveText, 2, 0)
        self.first_tab_layout.addWidget(self.RemoveEdit, 2, 1)
        self.first_tab_layout.addWidget(self.RemoveLineText, 2, 2)
        self.first_tab_layout.addWidget(self.RemoveLineSelectBox, 2, 3)
        self.first_tab_layout.addWidget(self.RemoveLineSelectBox, 2, 4)

        self.first_tab_layout.addWidget(self.NewColumn, 3, 0)
        self.first_tab_layout.addWidget(self.NewColumnEdit, 3, 1)

        self.first_tab_layout.addWidget(self.RemoveColumnText, 4, 0)
        self.first_tab_layout.addWidget(self.RemoveColumnSelectBox, 4, 1)

        self.setLayout(self.first_tab_layout)


class SecondTab(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = MainWindow()
    app.exec()
