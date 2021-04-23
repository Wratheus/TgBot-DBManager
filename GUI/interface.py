from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sqlite3
from pprint import pprint


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

        # group_id and validation
        self.groups_id = QtWidgets.QLineEdit(self.groupBox)
        self.groups_id.setGeometry(QtCore.QRect(70, 28, 113, 23))
        self.groups_id.setObjectName("groups_id")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 57, 21))
        self.label.setObjectName("label")

        self.groups_id_validator_id_RE = QtCore.QRegExp('^\d{3}$')
        self.groups_id_validator = QtGui.QRegExpValidator(self.groups_id_validator_id_RE)
        self.groups_id.setValidator(self.groups_id_validator)

        # group and validation
        self.groups_name = QtWidgets.QLineEdit(self.groupBox)
        self.groups_name.setGeometry(QtCore.QRect(70, 58, 113, 23))
        self.groups_name.setObjectName("groups_name")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 57, 15))
        self.label_2.setObjectName("label_2")

        self.validator_groupname_RE = QtCore.QRegExp('^\d-[А-Яа-я]{3}-\d{3}$')
        self.validator_groupname = QtGui.QRegExpValidator(self.validator_groupname_RE)
        self.groups_name.setValidator(self.validator_groupname)

        # student groupbox
        self.groupBox_2 = QtWidgets.QGroupBox(self.Lesson_3)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 10, 191, 91))
        self.groupBox_2.setObjectName("groupBox_2")

        # student_id and validation
        self.students_id = QtWidgets.QLineEdit(self.groupBox_2)
        self.students_id.setGeometry(QtCore.QRect(70, 28, 113, 23))
        self.students_id.setObjectName("students_id")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 57, 21))
        self.label_3.setObjectName("label_3")

        self.students_id_validator_RE = QtCore.QRegExp('^\d{3}$')
        self.students_id_validator = QtGui.QRegExpValidator(self.students_id_validator_RE)
        self.students_id.setValidator(self.students_id_validator)

        # student_name and validation
        self.students_name = QtWidgets.QLineEdit(self.groupBox_2)
        self.students_name.setGeometry(QtCore.QRect(70, 58, 113, 23))
        self.students_name.setObjectName("students_name")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 57, 15))
        self.label_4.setObjectName("label_4")

        self.students_name_validation_RE = QtCore.QRegExp('^[А-Яа-я\s]{40}')
        self.students_name_validation = QtGui.QRegExpValidator(self.students_name_validation_RE)
        self.students_name.setValidator(self.students_name_validation)

        # subject Box
        self.groupBox_3 = QtWidgets.QGroupBox(self.Lesson_3)
        self.groupBox_3.setGeometry(QtCore.QRect(410, 10, 191, 91))
        self.groupBox_3.setObjectName("groupBox_3")

        # subject_id and validation
        self.subject_id = QtWidgets.QLineEdit(self.groupBox_3)
        self.subject_id.setGeometry(QtCore.QRect(70, 28, 113, 23))
        self.subject_id.setObjectName("subject_id")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 57, 21))
        self.label_5.setObjectName("label_5")

        self.subject_id_validator_RE = QtCore.QRegExp('^\d{3}$')
        self.subject_id_validator = QtGui.QRegExpValidator(self.subject_id_validator_RE)
        self.subject_id.setValidator(self.subject_id_validator)

        # subject_name and validation
        self.subject_subject_name = QtWidgets.QLineEdit(self.groupBox_3)
        self.subject_subject_name.setGeometry(QtCore.QRect(70, 58, 113, 23))
        self.subject_subject_name.setObjectName("subject_subject_name")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 57, 15))
        self.label_6.setObjectName("label_6")

        self.subject_subject_name_validation_RE = QtCore.QRegExp('^[А-Яа-я\s]{20}')
        self.subject_subject_name_validation = QtGui.QRegExpValidator(self.subject_subject_name_validation_RE)
        self.subject_subject_name.setValidator(self.subject_subject_name_validation)

        # teacher box
        self.groupBox_4 = QtWidgets.QGroupBox(self.Lesson_3)
        self.groupBox_4.setGeometry(QtCore.QRect(610, 10, 191, 121))
        self.groupBox_4.setObjectName("groupBox_4")

        # teacher_id and validation
        self.teacher_id = QtWidgets.QLineEdit(self.groupBox_4)
        self.teacher_id.setGeometry(QtCore.QRect(70, 28, 113, 23))
        self.teacher_id.setObjectName("teacher_id")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 57, 21))
        self.label_7.setObjectName("label_7")

        self.teacher_id_validation_RE = QtCore.QRegExp('^\d{3}$')
        self.teacher_id_validation = QtGui.QRegExpValidator(self.teacher_id_validation_RE)
        self.teacher_id.setValidator(self.teacher_id_validation)

        # teacher_name and validation
        self.teacher_name = QtWidgets.QLineEdit(self.groupBox_4)
        self.teacher_name.setGeometry(QtCore.QRect(70, 58, 113, 23))
        self.teacher_name.setObjectName("teacher_name")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 57, 15))
        self.label_8.setObjectName("label_8")

        self.teacher_name_validator_RE = QtCore.QRegExp('^[А-Яа-я\s]{40}')
        self.teacher_name_validator = QtGui.QRegExpValidator(self.teacher_name_validator_RE)
        self.teacher_name.setValidator(self.teacher_name_validator)

        # subject and validation
        self.teacher_subject = QtWidgets.QLineEdit(self.groupBox_4)
        self.teacher_subject.setGeometry(QtCore.QRect(70, 88, 113, 23))
        self.teacher_subject.setObjectName("teacher_subject")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(10, 90, 57, 15))
        self.label_11.setObjectName("label_11")

        # validator from subject_subject_name
        self.teacher_subject.setValidator(self.subject_subject_name_validation)

        # journal box
        self.journal_box = QtWidgets.QGroupBox(self.Lesson_3)
        self.journal_box.setGeometry(QtCore.QRect(610, 140, 191, 200))
        self.journal_box.setObjectName("journal_box")

        # journal_id and validation
        self.journal_id = QtWidgets.QLineEdit(self.journal_box)
        self.journal_id.setGeometry(QtCore.QRect(70, 15, 113, 23))
        self.journal_id.setObjectName("journal_id")
        self.label_journal_id = QtWidgets.QLabel(self.journal_box)
        self.label_journal_id.setGeometry(QtCore.QRect(10, 18, 57, 15))
        self.label_journal_id.setObjectName("label_journal_id")

        self.journal_id_validation_RE = QtCore.QRegExp('^\d{3}$')
        self.journal_id_validation = QtGui.QRegExpValidator(self.journal_id_validation_RE)
        self.journal_id.setValidator(self.journal_id_validation)

        # journal_student_id | [validation from student_id]
        self.journal_student = QtWidgets.QLineEdit(self.journal_box)
        self.journal_student.setGeometry(QtCore.QRect(70, 44, 113, 23))
        self.journal_student.setObjectName("journal_student")
        self.label_student_id = QtWidgets.QLabel(self.journal_box)
        self.label_student_id.setGeometry(QtCore.QRect(10, 47, 57, 15))
        self.label_student_id.setObjectName("label_student_id")

        self.journal_student.setValidator(self.students_id_validator)

        # journal_group_id | [validation from group_id]
        self.journal_group = QtWidgets.QLineEdit(self.journal_box)
        self.journal_group.setGeometry(QtCore.QRect(70, 75, 113, 23))
        self.journal_group.setObjectName("journal_group")
        self.label_group_id = QtWidgets.QLabel(self.journal_box)
        self.label_group_id.setGeometry(QtCore.QRect(10, 77, 57, 15))
        self.label_group_id.setObjectName("label_group_id")

        self.journal_group.setValidator(self.groups_id_validator)

        # journal_subject_id | [validation from subject_id]
        self.journal_subject = QtWidgets.QLineEdit(self.journal_box)
        self.journal_subject.setGeometry(QtCore.QRect(70, 105, 113, 23))
        self.journal_subject.setObjectName("journal_subject")
        self.label_subject_id = QtWidgets.QLabel(self.journal_box)
        self.label_subject_id.setGeometry(QtCore.QRect(10, 107, 57, 15))
        self.label_subject_id.setObjectName("label_subject_id")

        self.journal_subject.setValidator(self.subject_id_validator)

        # journal attendance and validation
        self.journal_attendance = QtWidgets.QLineEdit(self.journal_box)
        self.journal_attendance.setGeometry(QtCore.QRect(70, 135, 113, 23))
        self.journal_attendance.setObjectName("journal_attendance")
        self.label_attendance_id = QtWidgets.QLabel(self.journal_box)
        self.label_attendance_id.setGeometry(QtCore.QRect(10, 137, 57, 15))
        self.label_attendance_id.setObjectName("label_attendance_id")

        self.journal_attendance_validation_RE = QtCore.QRegExp('^([-+], ){500}')
        self.journal_attendance_validation = QtGui.QRegExpValidator(self.journal_attendance_validation_RE)
        self.journal_attendance.setValidator(self.journal_attendance_validation)

        # journal grades and validation
        self.journal_grades = QtWidgets.QLineEdit(self.journal_box)
        self.journal_grades.setGeometry(QtCore.QRect(70, 165, 113, 23))
        self.journal_grades.setObjectName("journal_attendance")
        self.label_grades_id = QtWidgets.QLabel(self.journal_box)
        self.label_grades_id.setGeometry(QtCore.QRect(10, 167, 57, 15))
        self.label_grades_id.setObjectName("label_grades_id")

        self.journal_grades_validation_RE = QtCore.QRegExp('^([1-5], ){500}')
        self.journal_grades_validation = QtGui.QRegExpValidator(self.journal_grades_validation_RE)
        self.journal_grades.setValidator(self.journal_grades_validation)

        # search and listbox
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
        self.CancelChanges_button_3 = QtWidgets.QPushButton(self.DB_viewer_3)
        self.CancelChanges_button_3.setGeometry(QtCore.QRect(540, 482, 111, 31))
        self.CancelChanges_button_3.setObjectName("CancelChanges_button_3")
        self.Apply_Button_3 = QtWidgets.QPushButton(self.DB_viewer_3)
        self.Apply_Button_3.setGeometry(QtCore.QRect(660, 482, 111, 31))
        self.Apply_Button_3.setObjectName("Apply_Button_3")
        MainWindow.setCentralWidget(self.Mainlayout)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 20))
        self.menubar.setObjectName("menubar")
        self.File = QtWidgets.QMenu(self.menubar)
        self.File.setObjectName("File")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.TabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ids = ["group_id", "student_id", "subject_id", "teacher_id", "journal_id"]
        self.tables = [["group_id", "group_name"],
                       ["student_id", "student_name"],
                       ["subject_id", "subject_name"],
                       ["teacher_id", "teacher_name", "subject_id"],
                       ["journal_id", "student_id", "group_id", "subject_id", "attendance", "grades"]]

        self.addButton.clicked.connect(self.clicked_add)
        self.deleteButton.clicked.connect(self.clicked_delete)
        self.searchButton.clicked.connect(self.clicked_search)
        self.updateButton.clicked.connect(self.clicked_update)
        self.tablesSelect.currentTextChanged.connect(self.disable_controls)
        self.list.selectionModel().selectionChanged.connect(self.select_items)

    def getValues(self):
        if self.tablesSelect.currentText().lower() == "groups":
            return (self.groups_id.text(), self.groups_name.text())
        elif self.tablesSelect.currentText().lower() == "students":
            return (self.students_id.text(), self.students_name.text())
        elif self.tablesSelect.currentText().lower() == "teachers":
            return (self.teacher_id.text(), self.teacher_name.text(), self.teacher_subject.text())
        elif self.tablesSelect.currentText().lower() == "journal":
            return (self.journal_id.text(), self.journal_student.text(), self.journal_group.text(),
                    self.journal_subject.text(), self.journal_attendance.text(), self.journal_grades.text())
        elif self.tablesSelect.currentText().lower() == "subjects":
            return (self.subject_id.text(), self.subject_subject_name.text())

    def disable_controls(self,value):
        if self.tablesSelect.currentText().lower() == "groups":
            self.groups_id.setEnabled(True)
            self.groups_name.setEnabled(True)
            self.students_id.setEnabled(False)
            self.students_name.setEnabled(False)
            self.teacher_id.setEnabled(False)
            self.teacher_name.setEnabled(False)
            self.teacher_subject.setEnabled(False)
            self.journal_id.setEnabled(False)
            self.journal_student.setEnabled(False)
            self.journal_group.setEnabled(False)
            self.journal_subject.setEnabled(False)
            self.journal_attendance.setEnabled(False)
            self.journal_grades.setEnabled(False)
            self.subject_id.setEnabled(False)
            self.subject_subject_name.setEnabled(False)
        elif self.tablesSelect.currentText().lower() == "students":
            self.groups_id.setEnabled(False)
            self.groups_name.setEnabled(False)
            self.students_id.setEnabled(True)
            self.students_name.setEnabled(True)
            self.teacher_id.setEnabled(False)
            self.teacher_name.setEnabled(False)
            self.teacher_subject.setEnabled(False)
            self.journal_id.setEnabled(False)
            self.journal_student.setEnabled(False)
            self.journal_group.setEnabled(False)
            self.journal_subject.setEnabled(False)
            self.journal_attendance.setEnabled(False)
            self.journal_grades.setEnabled(False)
            self.subject_id.setEnabled(False)
            self.subject_subject_name.setEnabled(False)
        elif self.tablesSelect.currentText().lower() == "teachers":
            self.groups_id.setEnabled(False)
            self.groups_name.setEnabled(False)
            self.students_id.setEnabled(False)
            self.students_name.setEnabled(False)
            self.teacher_id.setEnabled(True)
            self.teacher_name.setEnabled(True)
            self.teacher_subject.setEnabled(True)
            self.journal_id.setEnabled(False)
            self.journal_student.setEnabled(False)
            self.journal_group.setEnabled(False)
            self.journal_subject.setEnabled(False)
            self.journal_attendance.setEnabled(False)
            self.journal_grades.setEnabled(False)
            self.subject_id.setEnabled(False)
            self.subject_subject_name.setEnabled(False)
        elif self.tablesSelect.currentText().lower() == "journal":
            self.groups_id.setEnabled(False)
            self.groups_name.setEnabled(False)
            self.students_id.setEnabled(False)
            self.students_name.setEnabled(False)
            self.teacher_id.setEnabled(False)
            self.teacher_name.setEnabled(False)
            self.teacher_subject.setEnabled(False)
            self.journal_id.setEnabled(True)
            self.journal_student.setEnabled(True)
            self.journal_group.setEnabled(True)
            self.journal_subject.setEnabled(True)
            self.journal_attendance.setEnabled(True)
            self.journal_grades.setEnabled(True)
            self.subject_id.setEnabled(False)
            self.subject_subject_name.setEnabled(False)
        elif self.tablesSelect.currentText().lower() == "subjects":
            self.groups_id.setEnabled(False)
            self.groups_name.setEnabled(False)
            self.students_id.setEnabled(False)
            self.students_name.setEnabled(False)
            self.teacher_id.setEnabled(False)
            self.teacher_name.setEnabled(False)
            self.teacher_subject.setEnabled(False)
            self.journal_id.setEnabled(False)
            self.journal_student.setEnabled(False)
            self.journal_group.setEnabled(False)
            self.journal_subject.setEnabled(False)
            self.journal_attendance.setEnabled(False)
            self.journal_grades.setEnabled(False)
            self.subject_id.setEnabled(True)
            self.subject_subject_name.setEnabled(True)
            
    def clicked_add(self):
        vals = self.getValues()
        query = "INSERT INTO %s values(%s)" % (
        self.tablesSelect.currentText(), ",".join(['?' for _ in range(len(vals))]).strip(","))
        try:
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
            _a = []
            _a.append(self.getValues()[0])
            cur.execute(query, _a)
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
        try:
            index = self.list.selectionModel().currentIndex().row()
            if self.tablesSelect.currentText().lower() == "groups":
                self.groups_id.setText(str(self.list.item(index,0).text()))
                self.groups_name.setText(str(self.list.item(index,1).text()))
            elif self.tablesSelect.currentText().lower() == "students":
                self.students_id.setText(str(self.list.item(index,0).text()))
                self.students_name.setText(str(self.list.item(index,1).text()))
            elif self.tablesSelect.currentText().lower() == "teachers":
                self.teacher_id.setText(str(self.list.item(index,0).text()))
                self.teacher_name.setText(str(self.list.item(index,1).text()))
                self.teacher_subject.setText(str(self.list.item(index,2).text()))
            elif self.tablesSelect.currentText().lower() == "journal":
                self.journal_id.setText(str(self.list.item(index,0).text()))
                self.journal_student.setText(str(self.list.item(index,1).text()))
                self.journal_group.setText(str(self.list.item(index,2).text()))
                self.journal_subject.setText(str(self.list.item(index,3).text()))
                self.journal_attendance.setText(str(self.list.item(index,4).text()))
                self.journal_grades.setText(str(self.list.item(index,5).text()))
            elif self.tablesSelect.currentText().lower() == "subjects":
                self.subject_id.setText(str(self.list.item(index,0).text()))
                self.subject_subject_name.setText(str(self.list.item(index,1).text()))
                
        except Exception as err:
            print(err)
       

    def clear(self):
        self.groups_id.setText("")
        self.groups_name.setText("")
        self.students_name.setText("")
        self.students_id.setText("")
        self.subject_id.setText("")
        self.subject_id.setText("")
        self.subject_subject_name.setText("")
        self.teacher_id.setText("")
        self.teacher_name.setText("")
        self.teacher_subject.setText("")
        self.journal_group.setText("")
        self.journal_id.setText("")
        self.journal_grades.setText("")
        self.journal_attendance.setText("")
        self.journal_subject.setText("")
        self.journal_student.setText("")


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
        self.journal_box.setTitle(_translate("MainWindow", "Journal"))
        self.label_journal_id.setText(_translate("MainWindow", "ID"))
        self.label_student_id.setText(_translate("MainWindow", "Student ID"))
        self.label_group_id.setText(_translate("MainWindow", "Group ID"))
        self.label_subject_id.setText(_translate("MainWindow", "Subject ID"))
        self.label_attendance_id.setText(_translate("MainWindow", "Attendance"))
        self.label_grades_id.setText(_translate("MainWindow", "Grades"))

        self.searchButton.setText(_translate("MainWindow", "search"))
        self.tablesSelect.setItemText(0, _translate("MainWindow", "Groups"))
        self.tablesSelect.setItemText(1, _translate("MainWindow", "Students"))
        self.tablesSelect.setItemText(2, _translate("MainWindow", "Subjects"))
        self.tablesSelect.setItemText(3, _translate("MainWindow", "Teachers"))
        self.tablesSelect.setItemText(4, _translate("MainWindow", "Journal"))
        self.label_15.setText(_translate("MainWindow", "Search"))
        self.TabWidget_3.setTabText(self.TabWidget_3.indexOf(self.Lesson_3),
                                    _translate("MainWindow", "Lesson management"))

        self.CancelChanges_button_3.setText(_translate("MainWindow", "Cancel changes"))
        self.Apply_Button_3.setText(_translate("MainWindow", "Apply"))
        self.File.setTitle(_translate("MainWindow", "File"))
