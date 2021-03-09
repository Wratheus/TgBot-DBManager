from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QFile
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(796, 567)
        MainWindow.setWindowTitle("DB edit Tool")

        self.Mainlayout = QtWidgets.QWidget(MainWindow)
        self.Mainlayout.setEnabled(True)
        self.Mainlayout.setAutoFillBackground(False)
        self.Mainlayout.setObjectName("Mainlayout")

        self.gridLayoutWidget = QtWidgets.QWidget(self.Mainlayout)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 791, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.GridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.GridLayout.setContentsMargins(0, 0, 0, 0)
        self.GridLayout.setObjectName("GridLayout")

        self.TabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.TabWidget.setObjectName("TabWidget")

        self.Lesson = QtWidgets.QWidget()
        self.Lesson.setObjectName("Lesson")

        self.Enter_Button = QtWidgets.QPushButton(self.Lesson)
        self.Enter_Button.setGeometry(QtCore.QRect(370, 60, 121, 31))
        self.Enter_Button.setObjectName("Enter_Button")

        self.tableWidget = QtWidgets.QTableWidget(self.Lesson)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 761, 341))
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")

        self.Confirm_Button = QtWidgets.QPushButton(self.Lesson)
        self.Confirm_Button.setGeometry(QtCore.QRect(590, 470, 181, 41))
        self.Confirm_Button.setObjectName("Confirm_Button")

        self.Reset_Button = QtWidgets.QPushButton(self.Lesson)
        self.Reset_Button.setGeometry(QtCore.QRect(460, 470, 121, 41))
        self.Reset_Button.setObjectName("Reset_Button")

        self.Select_group_Label = QtWidgets.QLabel(self.Lesson)
        self.Select_group_Label.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.Select_group_Label.setObjectName("Select_group_Label")

        self.SelectSubject_ComboBox = QtWidgets.QComboBox(self.Lesson)
        self.SelectSubject_ComboBox.setGeometry(QtCore.QRect(10, 30, 161, 20))
        self.SelectSubject_ComboBox.setObjectName("SelectSubject_ComboBox")

        self.SelectGroup_ComboBox = QtWidgets.QComboBox(self.Lesson)
        self.SelectGroup_ComboBox.setGeometry(QtCore.QRect(10, 70, 161, 20))
        self.SelectGroup_ComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SelectGroup_ComboBox.setEditable(False)
        self.SelectGroup_ComboBox.setCurrentText("")
        self.SelectGroup_ComboBox.setObjectName("SelectGroup_ComboBox")

        self.SelectStudent_Label = QtWidgets.QLabel(self.Lesson)
        self.SelectStudent_Label.setGeometry(QtCore.QRect(190, 10, 91, 21))
        self.SelectStudent_Label.setObjectName("SelectStudent_Label")

        self.SelectStudent_ComboBox = QtWidgets.QComboBox(self.Lesson)
        self.SelectStudent_ComboBox.setGeometry(QtCore.QRect(190, 30, 161, 20))
        self.SelectStudent_ComboBox.setObjectName("SelectStudent_ComboBox")

        self.SelectSubject_Label = QtWidgets.QLabel(self.Lesson)
        self.SelectSubject_Label.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.SelectSubject_Label.setObjectName("SelectSubject_Label")

        self.SetAttendance_ComboBox = QtWidgets.QComboBox(self.Lesson)
        self.SetAttendance_ComboBox.setGeometry(QtCore.QRect(190, 70, 161, 20))
        self.SetAttendance_ComboBox.setObjectName("SetAttendance_ComboBox")

        self.SetMark_ComboBox = QtWidgets.QComboBox(self.Lesson)
        self.SetMark_ComboBox.setGeometry(QtCore.QRect(370, 30, 121, 20))
        self.SetMark_ComboBox.setObjectName("SetMark_ComboBox")

        self.SetAttendance_Label = QtWidgets.QLabel(self.Lesson)
        self.SetAttendance_Label.setGeometry(QtCore.QRect(190, 50, 91, 21))
        self.SetAttendance_Label.setObjectName("SetAttendance_Label")

        self.SetMark_Label = QtWidgets.QLabel(self.Lesson)
        self.SetMark_Label.setGeometry(QtCore.QRect(370, 10, 61, 21))
        self.SetMark_Label.setObjectName("SetMark_Label")

        self.CurrentAttendanceTable_Label = QtWidgets.QLabel(self.Lesson)
        self.CurrentAttendanceTable_Label.setGeometry(QtCore.QRect(10, 100, 131, 20))
        self.CurrentAttendanceTable_Label.setObjectName("CurrentAttendanceTable_Label")

        self.TabWidget.addTab(self.Lesson, "")
        self.DB_viewer = QtWidgets.QWidget()
        self.DB_viewer.setObjectName("DB_viewer")

        self.DBManagement_TableWidget = QtWidgets.QTableWidget(self.DB_viewer)
        self.DBManagement_TableWidget.setGeometry(QtCore.QRect(10, 61, 761, 411))
        self.DBManagement_TableWidget.setRowCount(20)
        self.DBManagement_TableWidget.setColumnCount(15)
        self.DBManagement_TableWidget.setObjectName("DBManagement_TableWidget")

        self.SelectTable_ComboBox = QtWidgets.QComboBox(self.DB_viewer)
        self.SelectTable_ComboBox.setGeometry(QtCore.QRect(10, 30, 161, 20))
        self.SelectTable_ComboBox.setObjectName("SelectTable_ComboBox")

        self.SelectTable_Label = QtWidgets.QLabel(self.DB_viewer)
        self.SelectTable_Label.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.SelectTable_Label.setObjectName("SelectTable_Label")

        self.SearchInThisTable_Line = QtWidgets.QLineEdit(self.DB_viewer)
        self.SearchInThisTable_Line.setGeometry(QtCore.QRect(180, 30, 113, 20))
        self.SearchInThisTable_Line.setObjectName("SearchInThisTable_Line")

        self.SearchInThisTableLabel = QtWidgets.QLabel(self.DB_viewer)
        self.SearchInThisTableLabel.setGeometry(QtCore.QRect(180, 10, 101, 21))
        self.SearchInThisTableLabel.setObjectName("SearchInThisTableLabel")

        self.CancelChanges_button = QtWidgets.QPushButton(self.DB_viewer)
        self.CancelChanges_button.setGeometry(QtCore.QRect(540, 482, 111, 31))
        self.CancelChanges_button.setObjectName("CancelChanges_button")

        self.Apply_Button = QtWidgets.QPushButton(self.DB_viewer)
        self.Apply_Button.setGeometry(QtCore.QRect(660, 482, 111, 31))
        self.Apply_Button.setObjectName("Apply_Button")

        self.TabWidget.addTab(self.DB_viewer, "DB management")
        self.GridLayout.addWidget(self.TabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.Mainlayout)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName("menubar")

        self.File = QtWidgets.QMenu(self.menubar)
        self.File.setObjectName("File")
        MainWindow.setMenuBar(self.menubar)

        self.actionOpen_database_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_database_file.setObjectName("actionOpen_database_file")
        self.actionCreate_new_database_file = QtWidgets.QAction(MainWindow)
        self.actionCreate_new_database_file.setObjectName("actionCreate_new_database_file")
        self.File.addAction(self.actionOpen_database_file)
        self.File.addAction(self.actionCreate_new_database_file)
        self.menubar.addAction(self.File.menuAction())

        self.retranslateUi(MainWindow)
        self.TabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.Enter_Button.setText(_translate("MainWindow", "Confirm"))
        self.Confirm_Button.setText(_translate("MainWindow", "Submit"))
        self.Reset_Button.setText(_translate("MainWindow", "RESET"))
        self.Select_group_Label.setText(_translate("MainWindow", "Select group"))
        self.SelectStudent_Label.setText(_translate("MainWindow", "Select student"))
        self.SelectSubject_Label.setText(_translate("MainWindow", "Select subject"))
        self.SetAttendance_Label.setText(_translate("MainWindow", "Set attendance"))
        self.SetMark_Label.setText(_translate("MainWindow", "Select mark"))
        self.CurrentAttendanceTable_Label.setText(_translate("MainWindow", "Current attendance table"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.Lesson), _translate("MainWindow", "Lesson management"))
        self.SelectTable_Label.setText(_translate("MainWindow", "Select table"))
        self.SearchInThisTableLabel.setText(_translate("MainWindow", "Search in this table"))
        self.CancelChanges_button.setText(_translate("MainWindow", "Cancel changes"))
        self.Apply_Button.setText(_translate("MainWindow", "Apply"))
        self.File.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_database_file.setText(_translate("MainWindow", "Open database file"))
        self.actionCreate_new_database_file.setText(_translate("MainWindow", "Create new database file"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())