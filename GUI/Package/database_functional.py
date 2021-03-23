import sqlite3
from Package.interface import Ui_MainWindow
from PyQt5 import QtWidgets

class ConnectionFunctions:

    def getValues(Ui_MainWindow: Ui_MainWindow):
        if Ui_MainWindow.tablesSelect.currentText().lower() == "group":
            return (Ui_MainWindow.groups_id.text(), Ui_MainWindow.groups_name.text())
        elif Ui_MainWindow.tablesSelect.currentText().lower() == "student":
            return (Ui_MainWindow.students_id.text(), Ui_MainWindow.students_.text())
        elif Ui_MainWindow.tablesSelect.currentText().lower() == "teacher":
            return (Ui_MainWindow.teacher_id.text(), Ui_MainWindow.teacher_name.text(), Ui_MainWindow.teacher_subject.text())
        elif Ui_MainWindow.tablesSelect.currentText().lower() == "subject":
            return (Ui_MainWindow.subject_id.text(), Ui_MainWindow.subject_subject.text())

    def clicked_add(Ui_MainWindow: Ui_MainWindow):
        vals = ConnectionFunctions.getValues(Ui_MainWindow)
        query = "INSERT INTO %s values(%s)" % (
        Ui_MainWindow.tablesSelect.currentText(), ",".join(['?' for _ in range(len(vals))]).strip(","))
        try:
            pass
            con = sqlite3.connect("test.db")
            cur = con.cursor()
            cur.execute(query, vals)
            con.commit()
            ConnectionFunctions.clear(Ui_MainWindow)
            Ui_MainWindow.alert(f"{Ui_MainWindow.tablesSelect.currentText()} Changes",
                       f"Added to {Ui_MainWindow.tablesSelect.currentText()} successfully", "")

        except sqlite3.Error as error:
            Ui_MainWindow.alert(f"{Ui_MainWindow.tablesSelect.currentText()}",
                       f"Error at {Ui_MainWindow.tablesSelect.currentText()}", str(error))
            con.rollback()
        finally:
            con.close()

    def clicked_delete(Ui_MainWindow: Ui_MainWindow):
        query = "delete from %s where %s=?" % (
        Ui_MainWindow.tablesSelect.currentText(), Ui_MainWindow.ids[Ui_MainWindow.tablesSelect.currentIndex()])
        print(query)
        try:
            con = sqlite3.connect("test.db")
            cur = con.cursor()
            cur.execute(query, list(ConnectionFunctions.getValues(Ui_MainWindow)[0]))
            con.commit()
            ConnectionFunctions.clear(Ui_MainWindow)
            Ui_MainWindow.alert(f"{Ui_MainWindow.tablesSelect.currentText()} Changes",
                       f"Deleted from {Ui_MainWindow.tablesSelect.currentText()} successfully", "")
        except sqlite3.Error as error:
            Ui_MainWindow.alert(f"{Ui_MainWindow.tablesSelect.currentText()}",
                                f"Error at {Ui_MainWindow.tablesSelect.currentText()}", str(error))
            con.rollback()
        finally:
            con.close()

    def clicked_update(Ui_MainWindow: Ui_MainWindow):
        query = "update %s set %s where %s=?" % (
        Ui_MainWindow.tablesSelect.currentText(), "=? ,".join(Ui_MainWindow.tables[Ui_MainWindow.tablesSelect.currentIndex()][1:]) + "=? ",
        Ui_MainWindow.ids[Ui_MainWindow.tablesSelect.currentIndex()])
        print(query)
        print((ConnectionFunctions.getValues(Ui_MainWindow)[1:] + ConnectionFunctions.getValues(Ui_MainWindow)[:1]))
        try:
            pass
            con = sqlite3.connect("test.db")
            cur = con.cursor()
            cur.execute(query, (ConnectionFunctions.getValues(Ui_MainWindow)[1:]
                                + ConnectionFunctions.getValues(Ui_MainWindow)[:1]))
            con.commit()
            ConnectionFunctions.clear(Ui_MainWindow)
            Ui_MainWindow.alert(f"{Ui_MainWindow.tablesSelect.currentText()}",
                                f"Update {Ui_MainWindow.tablesSelect.currentText()} successfully", "")
        except sqlite3.Error as error:
            Ui_MainWindow.alert(f"{Ui_MainWindow.tablesSelect.currentText()}",
                                f"Error at {Ui_MainWindow.tablesSelect.currentText()}", str(error))
            con.rollback()
        finally:
            con.close()

    def clicked_search(Ui_MainWindow: Ui_MainWindow):
        try:
            tab = Ui_MainWindow.tables[Ui_MainWindow.tablesSelect.currentIndex()]
            query = "select * from %s where " % (Ui_MainWindow.tablesSelect.currentText())
            for column in Ui_MainWindow.tables[int(Ui_MainWindow.tablesSelect.currentIndex())]:
                query += " %s like '%%%s%%' or" % (column, Ui_MainWindow.search.text())
            query = query.strip("r").strip("o")
            con = sqlite3.connect("test.db")
            cur = con.cursor()
            Ui_MainWindow.list.setColumnCount(len(Ui_MainWindow.tables[Ui_MainWindow.tablesSelect.currentIndex()]))
            with_ = Ui_MainWindow.list.width() // len(tab)

            for x, y in enumerate(tab):
                Ui_MainWindow.list.setColumnWidth(x, with_)
            Ui_MainWindow.list.setHorizontalHeaderLabels(list(tab))

            Ui_MainWindow.list.setRowCount(0)
            for x, i in enumerate(cur.execute(query)):
                Ui_MainWindow.list.setRowCount(x + 1)
                for y, item in enumerate(i):
                    Ui_MainWindow.list.setItem(x, y, QtWidgets.QTableWidgetItem(str(i[0])))
                print(x, i)
        except sqlite3.Error as error:
            print(error)

    def clear(Ui_MainWindow: Ui_MainWindow):
        Ui_MainWindow.groups_id.setText("")
        Ui_MainWindow.groups_name.setText("")
        Ui_MainWindow.students_.setText("")
        Ui_MainWindow.students_id.setText("")
        Ui_MainWindow.subject_id.setText("")
        Ui_MainWindow.subject_id.setText("")
        Ui_MainWindow.subject_subject.setText("")
        Ui_MainWindow.teacher_id.setText("")
        Ui_MainWindow.teacher_name.setText("")
        Ui_MainWindow.teacher_subject.setText("")


