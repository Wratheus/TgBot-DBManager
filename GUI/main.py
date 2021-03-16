from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import interface

# DB Functional
class ConnectionDB(interface.Ui_MainWindow):

    def struct(self):
        self.ids = ["id", "student_id", "subject_id", "teacher_id", "day_id"]
        self.tables = [["student_id", "student_name"],
                       ["subject_id", "subject_name"],
                       ["teacher_id", "teacher_name", "subject_id"],
                       ["journal_id", "student_id", "group_id", "subject_id", "attendance", "grades"]]

        self.addButton.clicked.connect(self.clicked_add)
        self.deleteButton.clicked.connect(self.clicked_delete)
        self.searchButton.clicked.connect(self.clicked_search)
        self.updateButton.clicked.connect(self.clicked_update)
        self.list.selectionModel().selectionChanged.connect(self.select_items)

    def getValues(self):
        if self.tablesSelect.currentText().lower() == "group":
            return (self.groups_id.text(), self.groups_name.text())
        elif self.tablesSelect.currentText().lower() == "student":
            return (self.students_id.text(), self.students_.text())
        elif self.tablesSelect.currentText().lower() == "teacher":
            return (self.teacher_id.text(), self.teacher_name.text(), self.teacher_subject.text())
        elif self.tablesSelect.currentText().lower() == "subject":
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
                    self.list.setItem(x, y, QtWidgets.QTableWidgetItem(str(i[0])))
                print(x, i)
        except sqlite3.Error as error:
            print(error)

    def select_items(self, selected, deselected):
        pass

    def clear(self):
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

    def alert(self, title="", message="", detais=""):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setDetailedText(detais)
        msgBox.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = interface.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())