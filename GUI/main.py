from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QWidget, QVBoxLayout, QGridLayout, QDialogButtonBox, QLabel, QLineEdit, QComboBox, QPushButton
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
        self.TableSelectBoxList = ['Teachers', 'Students', 'Subjects', 'Time']
        self.ColumnSelectBoxList = ['id', 'FIO', 'Time']
        self.FirstTabLayout = QGridLayout()

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

        self.SubmitButton = QPushButton("Submit")
        self.DBLoadButton = QPushButton("Load DB")
        self.DBSelectTableText = QLabel("Select Table")
        self.DBSelectTable = QComboBox()
        self.DBSelectTable.addItems(self.TableSelectBoxList)

        self.InitializeLayouts()

    def InitializeLayouts(self):
        self.FirstTabLayout.addWidget(self.AddText, 1, 0)
        self.FirstTabLayout.addWidget(self.AddEdit, 1, 1)
        self.FirstTabLayout.addWidget(self.AddColumnText, 1, 2)
        self.FirstTabLayout.addWidget(self.AddColumnSelectBox, 1, 3)

        self.FirstTabLayout.addWidget(self.RemoveText, 2, 0)
        self.FirstTabLayout.addWidget(self.RemoveEdit, 2, 1)
        self.FirstTabLayout.addWidget(self.RemoveLineText, 2, 2)
        self.FirstTabLayout.addWidget(self.RemoveLineSelectBox, 2, 3)
        self.FirstTabLayout.addWidget(self.RemoveLineSelectBox, 2, 4)

        self.FirstTabLayout.addWidget(self.NewColumn, 3, 0)
        self.FirstTabLayout.addWidget(self.NewColumnEdit, 3, 1)

        self.FirstTabLayout.addWidget(self.RemoveColumnText, 4, 0)
        self.FirstTabLayout.addWidget(self.RemoveColumnSelectBox, 4, 1)

        self.FirstTabLayout.addWidget(self.SubmitButton, 6, 0)
        self.FirstTabLayout.addWidget(self.DBLoadButton, 7, 0)
        self.FirstTabLayout.addWidget(self.DBSelectTableText, 7, 1)
        self.FirstTabLayout.addWidget(self.DBSelectTable, 7, 2)

        self.setLayout(self.FirstTabLayout)


class SecondTab(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = MainWindow()
    app.exec()
