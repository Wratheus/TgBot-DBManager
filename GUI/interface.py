<<<<<<< HEAD
from PyQt5 import QtCore, QtWidgets
import db_functions
=======
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sqlite3
from pprint import pprint
>>>>>>> dev


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(829, 527)
        MainWindow.setMinimumSize(829, 527)
        MainWindow.setMaximumSize(829, 527)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle("DB edit Tool")
        self.Mainlayout = QtWidgets.QWidget(MainWindow)
        self.Mainlayout.setEnabled(True)
        self.Mainlayout.setAutoFillBackground(False)
        self.Mainlayout.setStyleSheet("")
        self.Mainlayout.setObjectName("Mainlayout")
        self.TabWidget_3 = QtWidgets.QTabWidget(self.Mainlayout)
        self.TabWidget_3.setGeometry(QtCore.QRect(0, 0, 821, 501))
        self.TabWidget_3.setObjectName("TabWidget_3")
        self.Lesson_3 = QtWidgets.QWidget()
        self.Lesson_3.setObjectName("Lesson_3")
        self.deleteButton = QtWidgets.QPushButton(self.Lesson_3)
        self.deleteButton.setGeometry(QtCore.QRect(610, 420, 191, 31))
        self.deleteButton.setObjectName("deleteButton")
        self.updateButton = QtWidgets.QPushButton(self.Lesson_3)
        self.updateButton.setGeometry(QtCore.QRect(711, 380, 90, 31))
        self.updateButton.setObjectName("updateButton")
        self.addButton = QtWidgets.QPushButton(self.Lesson_3)
        self.addButton.setGeometry(QtCore.QRect(610, 380, 91, 31))
        self.addButton.setObjectName("addButton")
        self.groupBox = QtWidgets.QGroupBox(self.Lesson_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 191, 91))
        self.groupBox.setObjectName("groupBox")
        self.groups_id = QtWidgets.QLineEdit(self.groupBox)
        self.groups_id.setGeometry(QtCore.QRect(70, 28, 113, 23))
        self.groups_id.setObjectName("groups_id")
        self.groups_name = QtWidgets.QLineEdit(self.groupBox)
        self.groups_name.setGeometry(QtCore.QRect(70, 58, 113, 23))
        self.groups_name.setObjectName("groups_name")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 57, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 57, 15))
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Lesson_3)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 10, 191, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.students_id = QtWidgets.QLineEdit(self.groupBox_2)
        self.students_id.setGeometry(QtCore.QRect(70, 28, 113, 23))
        self.students_id.setObjectName("students_id")
        self.students_ = QtWidgets.QLineEdit(self.groupBox_2)
        self.students_.setGeometry(QtCore.QRect(70, 58, 113, 23))
        self.students_.setObjectName("students_")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 57, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 57, 15))
        self.label_4.setObjectName("label_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.Lesson_3)
        self.groupBox_3.setGeometry(QtCore.QRect(410, 10, 191, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.subject_id = QtWidgets.QLineEdit(self.groupBox_3)
        self.subject_id.setGeometry(QtCore.QRect(70, 28, 113, 23))
        self.subject_id.setObjectName("subject_id")
        self.subject_subject = QtWidgets.QLineEdit(self.groupBox_3)
        self.subject_subject.setGeometry(QtCore.QRect(70, 58, 113, 23))
        self.subject_subject.setObjectName("subject_subject")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 57, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 57, 15))
        self.label_6.setObjectName("label_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.Lesson_3)
        self.groupBox_4.setGeometry(QtCore.QRect(610, 10, 191, 121))
        self.groupBox_4.setObjectName("groupBox_4")
        self.teacher_id = QtWidgets.QLineEdit(self.groupBox_4)
        self.teacher_id.setGeometry(QtCore.QRect(70, 28, 113, 23))
        self.teacher_id.setObjectName("teacher_id")
        self.teacher_name = QtWidgets.QLineEdit(self.groupBox_4)
        self.teacher_name.setGeometry(QtCore.QRect(70, 58, 113, 23))
        self.teacher_name.setObjectName("teacher_name")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 57, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 57, 15))
        self.label_8.setObjectName("label_8")
        self.teacher_subject = QtWidgets.QLineEdit(self.groupBox_4)
        self.teacher_subject.setGeometry(QtCore.QRect(70, 88, 113, 23))
        self.teacher_subject.setObjectName("teacher_subject")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(10, 90, 57, 15))
        self.label_11.setObjectName("label_11")
        self.journal_day = QtWidgets.QGroupBox(self.Lesson_3)
        self.journal_day.setGeometry(QtCore.QRect(610, 140, 191, 80))
        self.journal_day.setObjectName("journal_day")
        self.journal_group = QtWidgets.QLineEdit(self.journal_day)
        self.journal_group.setGeometry(QtCore.QRect(70, 45, 113, 23))
        self.journal_group.setObjectName("journal_group")
        self.label_10 = QtWidgets.QLabel(self.journal_day)
        self.label_10.setGeometry(QtCore.QRect(10, 45, 57, 15))
        self.label_10.setObjectName("label_10")
        self.journal_subject = QtWidgets.QLineEdit(self.journal_day)
        self.journal_subject.setGeometry(QtCore.QRect(70, 15, 113, 23))
        self.journal_subject.setObjectName("journal_subject")
        self.label_12 = QtWidgets.QLabel(self.journal_day)
        self.label_12.setGeometry(QtCore.QRect(10, 18, 57, 15))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.journal_day)
        self.label_13.setGeometry(QtCore.QRect(10, 122, 57, 15))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.journal_day)
        self.label_14.setGeometry(QtCore.QRect(10, 152, 57, 15))
        self.label_14.setObjectName("label_14")
        self.list = QtWidgets.QTableWidget(self.Lesson_3)
        self.list.setGeometry(QtCore.QRect(10, 140, 591, 311))
        self.list.setObjectName("list")
        self.search = QtWidgets.QLineEdit(self.Lesson_3)
        self.search.setGeometry(QtCore.QRect(80, 110, 351, 23))
        self.search.setObjectName("search")
        self.searchButton = QtWidgets.QPushButton(self.Lesson_3)
        self.searchButton.setGeometry(QtCore.QRect(450, 110, 151, 23))
        self.searchButton.setObjectName("searchButton")
        self.tablesSelect = QtWidgets.QComboBox(self.Lesson_3)
        self.tablesSelect.setGeometry(QtCore.QRect(610, 350, 191, 23))
        self.tablesSelect.setObjectName("tablesSelect")
        self.tablesSelect.addItem("")
        self.tablesSelect.addItem("")
        self.tablesSelect.addItem("")
        self.tablesSelect.addItem("")
        self.tablesSelect.addItem("")
        self.label_15 = QtWidgets.QLabel(self.Lesson_3)
        self.label_15.setGeometry(QtCore.QRect(10, 110, 57, 21))
        self.label_15.setObjectName("label_15")
        self.TabWidget_3.addTab(self.Lesson_3, "")
        self.DB_viewer_3 = QtWidgets.QWidget()
        self.DB_viewer_3.setObjectName("DB_viewer_3")
        self.DBManagement_TableWidget_3 = QtWidgets.QTableWidget(self.DB_viewer_3)
        self.DBManagement_TableWidget_3.setGeometry(QtCore.QRect(10, 61, 761, 401))
        self.DBManagement_TableWidget_3.setRowCount(20)
        self.DBManagement_TableWidget_3.setColumnCount(15)
        self.DBManagement_TableWidget_3.setObjectName("DBManagement_TableWidget_3")
        self.SelectTable_ComboBox_3 = QtWidgets.QComboBox(self.DB_viewer_3)
        self.SelectTable_ComboBox_3.setGeometry(QtCore.QRect(10, 30, 161, 20))
        self.SelectTable_ComboBox_3.setObjectName("SelectTable_ComboBox_3")
        self.SelectTable_Label_3 = QtWidgets.QLabel(self.DB_viewer_3)
        self.SelectTable_Label_3.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.SelectTable_Label_3.setObjectName("SelectTable_Label_3")
        self.SearchInThisTable_Line_3 = QtWidgets.QLineEdit(self.DB_viewer_3)
        self.SearchInThisTable_Line_3.setGeometry(QtCore.QRect(180, 30, 113, 20))
        self.SearchInThisTable_Line_3.setObjectName("SearchInThisTable_Line_3")
        self.SearchInThisTableLabel_3 = QtWidgets.QLabel(self.DB_viewer_3)
        self.SearchInThisTableLabel_3.setGeometry(QtCore.QRect(180, 10, 101, 21))
        self.SearchInThisTableLabel_3.setObjectName("SearchInThisTableLabel_3")
        self.CancelChanges_button_3 = QtWidgets.QPushButton(self.DB_viewer_3)
        self.CancelChanges_button_3.setGeometry(QtCore.QRect(540, 482, 111, 31))
        self.CancelChanges_button_3.setObjectName("CancelChanges_button_3")
        self.Apply_Button_3 = QtWidgets.QPushButton(self.DB_viewer_3)
        self.Apply_Button_3.setGeometry(QtCore.QRect(660, 482, 111, 31))
        self.Apply_Button_3.setObjectName("Apply_Button_3")
        self.TabWidget_3.addTab(self.DB_viewer_3, "DB management")
        MainWindow.setCentralWidget(self.Mainlayout)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 20))
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
        self.TabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.ids = ["id", "student_id", "subject_id", "teacher_id", "day_id"]
        self.tables = [["student_id", "student_name"],
                       ["subject_id", "subject_name"],
                       ["teacher_id", "teacher_name", "subject_id"],
                       ["journal_id", "student_id", "group_id", "subject_id", "attendance", "grades"]]

        self.addButton.clicked.connect(db_functions.ConnectionDB.clicked_add(self))
        self.deleteButton.clicked.connect(db_functions.ConnectionDB.clicked_delete(self))
        self.searchButton.clicked.connect(db_functions.ConnectionDB.clicked_search(self))
        self.updateButton.clicked.connect(db_functions.ConnectionDB.clicked_update(self))
        self.list.selectionModel().selectionChanged.connect(self.select_items)

        self.ids = ["group_id", "student_id", "subject_id", "teacher_id", "day_id"]
        self.tables = [["group_id", "group_name"],
                       ["student_id", "student_name"],
                       ["subject_id", "subject_name"],
                       ["teacher_id", "teacher_name", "subject_id"],
                       ["journal_id", "student_id", "group_id", "subject_id", "attendance", "grades"]]

        self.addButton.clicked.connect(self.clicked_add)
        self.deleteButton.clicked.connect(self.clicked_delete)
        self.searchButton.clicked.connect(self.clicked_search)
        self.updateButton.clicked.connect(self.clicked_update)
        self.list.selectionModel().selectionChanged.connect(self.select_items)

    def getValues(self):
        if self.tablesSelect.currentText().lower() == "groups":
            return (self.groups_id.text(), self.groups_name.text())
        elif self.tablesSelect.currentText().lower() == "students":
            return (self.students_id.text(), self.students_.text())
        elif self.tablesSelect.currentText().lower() == "teachers":
            return (self.teacher_id.text(), self.teacher_name.text(), self.teacher_subject.text())
        elif self.tablesSelect.currentText().lower() == "journal":
            return (self.journal_group.text(), self.journal_subject.text())
        elif self.tablesSelect.currentText().lower() == "subjects":
            return (self.subject_id.text(), self.subject_subject.text())

    def clicked_add(self):
        vals = self.getValues()
        query = "INSERT INTO %s values(%s)" % (
        self.tablesSelect.currentText(), ",".join(['?' for _ in range(len(vals))]).strip(","))
        try:
            pass
            con = sqlite3.connect("test.db")
            cur = con.cursor()
            cur.execute(query, vals)
            con.commit()
            self.clear()
            self.alert(f"{self.tablesSelect.currentText()} Changes",
                       f"Added to {self.tablesSelect.currentText()} successfully", "")

        except sqlite3.Error as error:
            self.alert(f"{self.tablesSelect.currentText()}", f"Error at {self.tablesSelect.currentText()}", str(error))
            con.rollback()
        finally:
            con.close()

    def clicked_delete(self):
        query = "delete from %s where %s=?" % (
        self.tablesSelect.currentText(), self.ids[self.tablesSelect.currentIndex()])
        print(query)
        try:
            con = sqlite3.connect("test.db")
            cur = con.cursor()
            cur.execute(query, list(self.getValues()[0]))
            con.commit()
            self.clear()
            self.alert(f"{self.tablesSelect.currentText()} Changes",
                       f"Deleted from {self.tablesSelect.currentText()} successfully", "")

        except sqlite3.Error as error:
            self.alert(f"{self.tablesSelect.currentText()}", f"Error at {self.tablesSelect.currentText()}", str(error))
            con.rollback()
        finally:
            con.close()

    def clicked_update(self):
        query = "update %s set %s where %s=?" % (
        self.tablesSelect.currentText(), "=? ,".join(self.tables[self.tablesSelect.currentIndex()][1:]) + "=? ",
        self.ids[self.tablesSelect.currentIndex()])
        print(query)
        print((self.getValues()[1:] + self.getValues()[:1]))
        try:
            pass
            con = sqlite3.connect("test.db")
            cur = con.cursor()
            cur.execute(query, (self.getValues()[1:] + self.getValues()[:1]))
            con.commit()
            self.clear()
            self.alert(f"{self.tablesSelect.currentText()}", f"Update {self.tablesSelect.currentText()} successfully",
                       "")

        except sqlite3.Error as error:
            self.alert(f"{self.tablesSelect.currentText()}", f"Error at {self.tablesSelect.currentText()}", str(error))
            con.rollback()
        finally:
            con.close()

    def clicked_search(self):
        try:
            tab = self.tables[self.tablesSelect.currentIndex()]
            query = "select * from %s where " % (self.tablesSelect.currentText())
            for column in self.tables[int(self.tablesSelect.currentIndex())]:
                query += " %s like '%%%s%%' or" % (column, self.search.text())
            query = query.strip("r").strip("o")
            con = sqlite3.connect("test.db")
            cur = con.cursor()
            self.list.setColumnCount(len(self.tables[self.tablesSelect.currentIndex()]))
            with_ = self.list.width() // len(tab)

            for x, y in enumerate(tab):
                self.list.setColumnWidth(x, with_)
            self.list.setHorizontalHeaderLabels(list(tab))

            self.list.setRowCount(0)
            for x, i in enumerate(cur.execute(query)):
                self.list.setRowCount(x + 1)
                for y, item in enumerate(i):
                    self.list.setItem(x, y, QtWidgets.QTableWidgetItem(str(item)))
                print(x, i)
        except sqlite3.Error as error:
            print(error)

    def select_items(self, selected, deselected):
        pass

    def clear(self):
        self.groups_id.setText("")
        self.groups_id.setText("")
        self.groups_name.setText("")
        self.students_.setText("")
        self.students_id.setText("")
        self.subject_id.setText("")
        self.subject_id.setText("")
        self.subject_subject.setText("")
        self.teacher_id.setText("")
        self.teacher_name.setText("")
        self.teacher_subject.setText("")
        self.journal_group.setText("")
        self.journal_subject.setText("")


    def alert(self, title="", message="", detais=""):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setDetailedText(detais)
        msgBox.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.deleteButton.setText(_translate("MainWindow", "DELETE"))
        self.updateButton.setText(_translate("MainWindow", "UPDATE"))
        self.addButton.setText(_translate("MainWindow", "ADD"))
        self.groupBox.setTitle(_translate("MainWindow", "Group"))
        self.label.setText(_translate("MainWindow", "ID"))
        self.label_2.setText(_translate("MainWindow", "Group"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Students"))
        self.label_3.setText(_translate("MainWindow", "ID"))
        self.label_4.setText(_translate("MainWindow", "Student"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Subject"))
        self.label_5.setText(_translate("MainWindow", "ID"))
        self.label_6.setText(_translate("MainWindow", "Subject"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Teachers"))
        self.label_7.setText(_translate("MainWindow", "ID"))
        self.label_8.setText(_translate("MainWindow", "Name"))
        self.label_11.setText(_translate("MainWindow", "Subject"))
        self.journal_day.setTitle(_translate("MainWindow", "journal"))
        self.label_10.setText(_translate("MainWindow", "Group"))
        self.label_12.setText(_translate("MainWindow", "Subject"))
        self.searchButton.setText(_translate("MainWindow", "search"))
        self.tablesSelect.setItemText(0, _translate("MainWindow", "Groups"))
        self.tablesSelect.setItemText(1, _translate("MainWindow", "Students"))
        self.tablesSelect.setItemText(2, _translate("MainWindow", "Subjects"))
        self.tablesSelect.setItemText(3, _translate("MainWindow", "Teachers"))
        self.tablesSelect.setItemText(4, _translate("MainWindow", "journal"))
        self.label_15.setText(_translate("MainWindow", "Search"))
        self.TabWidget_3.setTabText(self.TabWidget_3.indexOf(self.Lesson_3),
                                    _translate("MainWindow", "Lesson management"))
        self.SelectTable_Label_3.setText(_translate("MainWindow", "Select table"))
        self.SearchInThisTableLabel_3.setText(_translate("MainWindow", "Search in this table"))
        self.CancelChanges_button_3.setText(_translate("MainWindow", "Cancel changes"))
        self.Apply_Button_3.setText(_translate("MainWindow", "Apply"))
        self.File.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_database_file.setText(_translate("MainWindow", "Open database file"))
        self.actionCreate_new_database_file.setText(_translate("MainWindow", "Create new database file"))
