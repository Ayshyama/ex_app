from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import QStringListModel, Qt, QModelIndex
import random
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 745)
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "MainWindow"))

        self.close_db_view()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def handle_combobox_change(self):
        self.titleLabel.setText(self.comboBox.currentText())
    
    def get_exercise(self):
        topic = self.comboBox.currentText().replace(" ", "_")
        
        conn = sqlite3.connect("exercise_db.db")
        cur = conn.cursor()

        exercises = cur.execute(f"SELECT * FROM {topic}")
        exercise_list = []

        for i in exercises:
            for j in i:
                exercise_list.append(j)

        self.outputLabel.setText(random.choice(exercise_list))

        cur.close()
        conn.close()
    
    def open_db(self):
        self.centralwidget2 = QtWidgets.QWidget(MainWindow)
        self.centralwidget2.setObjectName("centralwidget2")

        self.topic_comboBox = QtWidgets.QComboBox(self.centralwidget2)
        self.topic_comboBox.setGeometry(QtCore.QRect(75, 630, 240, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.topic_comboBox.setFont(font)
        self.topic_comboBox.setObjectName("topic_comboBox")
        #self.topic_comboBox.addItem("")

        conn = sqlite3.connect("exercise_db.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        tables = cursor.fetchall()
        idx = 0
        for table in tables:
            self.topic_comboBox.addItem("")
            for tab in table:
                tab = tab.replace("_", " ")
            self.topic_comboBox.setItemText(idx, QtCore.QCoreApplication.translate("MainWindow", tab))
            idx += 1

        cursor.close()
        conn.close()

        self.exercises_listView = QtWidgets.QListView(self.centralwidget2)
        self.exercises_listView.setGeometry(QtCore.QRect(75, 50, 861, 500))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exercises_listView.setFont(font)
        self.exercises_listView.setMouseTracking(True)
        self.exercises_listView.setObjectName("exercises_listView")
        model = QStringListModel()
        
        self.listButton = QtWidgets.QPushButton(self.centralwidget2)
        self.listButton.setGeometry(QtCore.QRect(385, 630, 240, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listButton.setFont(font)
        self.listButton.setObjectName("listButton")
        self.listButton.setText(QtCore.QCoreApplication.translate("MainWindow", "View list"))

        def list_exercises():
            topic = self.topic_comboBox.currentText().replace(" ", "_")
            
            conn = sqlite3.connect("exercise_db.db")
            cur = conn.cursor()

            exercises = cur.execute(f"SELECT * FROM {topic}")
            exercise_list = []

            for i in exercises:
                for j in i:
                    exercise_list.append(j)

            model.setStringList(exercise_list)
            self.exercises_listView.setModel(model)
            self.exercises_listView.show()

            #self.exercises_listView.setText(exercise_list)

            cur.close()
            conn.close()

        self.listButton.clicked.connect(list_exercises)

        self.deleteButton = QtWidgets.QPushButton(self.centralwidget2)
        self.deleteButton.setGeometry(QtCore.QRect(385, 680, 240, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.setText(QtCore.QCoreApplication.translate("MainWindow", "Delete"))

        def delete_item():
            selected_indexes = self.exercises_listView.selectedIndexes()
            
            topic = self.topic_comboBox.currentText().replace(" ", "_")
        
            conn = sqlite3.connect("exercise_db.db")
            cur = conn.cursor()

            for index in selected_indexes:
                selected_text = index.data(Qt.DisplayRole)

            cur.execute(f"DELETE FROM {topic} WHERE exercise= ?", (selected_text,))
            
            conn.commit()

            cur.close()
            conn.close()
            list_exercises()

        self.deleteButton.clicked.connect(delete_item)

        self.closeButton = QtWidgets.QPushButton(self.centralwidget2)
        self.closeButton.setGeometry(QtCore.QRect(695, 630, 240, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setText(QtCore.QCoreApplication.translate("MainWindow", "Close"))

        self.closeButton.clicked.connect(self.close_db_view)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget2)
        self.plainTextEdit.setGeometry(QtCore.QRect(75, 580, 750, 35))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget2)
        self.pushButton.setGeometry(QtCore.QRect(825, 580, 110, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText(QtCore.QCoreApplication.translate("MainWindow", "Add"))

        def insert_exercise():
            topic = self.topic_comboBox.currentText().replace(" ", "_")
        
            conn = sqlite3.connect("exercise_db.db")
            cur = conn.cursor()

            exercise_to_insert = self.plainTextEdit.toPlainText()

            cur.execute(f"INSERT INTO {topic} (exercise) VALUES (?)", (exercise_to_insert,))
            
            conn.commit()

            cur.close()
            conn.close()
            list_exercises()

        self.pushButton.clicked.connect(insert_exercise)




        MainWindow.setCentralWidget(self.centralwidget2)

    def close_db_view(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 630, 241, 41))

        font = QtGui.QFont()
        font.setPointSize(14)

        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.comboBox.currentTextChanged.connect(self.handle_combobox_change)

        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(400, 630, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)

        self.generateButton.setFont(font)
        self.generateButton.setObjectName("generateButton")

        self.generateButton.clicked.connect(self.get_exercise)

        self.dbButton = QtWidgets.QPushButton(self.centralwidget)
        self.dbButton.setGeometry(QtCore.QRect(700, 630, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)

        self.dbButton.setFont(font)
        self.dbButton.setObjectName("dbButton")

        self.dbButton.clicked.connect(self.open_db)

        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(76, 204, 861, 381))
        self.outputLabel.setWordWrap(True)
        font = QtGui.QFont()
        font.setPointSize(16)

        self.outputLabel.setFont(font)
        self.outputLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLabel.setObjectName("outputLabel")
        
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(270, 69, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(18)

        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.comboBox.setItemText(0, QtCore.QCoreApplication.translate("MainWindow", "String manipulation"))
        self.comboBox.setItemText(1, QtCore.QCoreApplication.translate("MainWindow", "Lists"))
        self.comboBox.setItemText(2, QtCore.QCoreApplication.translate("MainWindow", "Dictionaries"))
        self.comboBox.setItemText(3, QtCore.QCoreApplication.translate("MainWindow", "Tuples"))
        self.comboBox.setItemText(4, QtCore.QCoreApplication.translate("MainWindow", "Sets"))
        self.comboBox.setItemText(5, QtCore.QCoreApplication.translate("MainWindow", "Indexing and Slicing"))
        self.comboBox.setItemText(6, QtCore.QCoreApplication.translate("MainWindow", "Mutable and Imutable types"))
        self.comboBox.setItemText(7, QtCore.QCoreApplication.translate("MainWindow", "Data types"))
        self.comboBox.setItemText(8, QtCore.QCoreApplication.translate("MainWindow", "Methods of types"))
        self.comboBox.setItemText(9, QtCore.QCoreApplication.translate("MainWindow", "Comprehension"))
        self.comboBox.setItemText(10, QtCore.QCoreApplication.translate("MainWindow", "Exceptions"))
        self.comboBox.setItemText(11, QtCore.QCoreApplication.translate("MainWindow", "Local and global scope"))
        self.comboBox.setItemText(12, QtCore.QCoreApplication.translate("MainWindow", "Closures"))
        self.comboBox.setItemText(13, QtCore.QCoreApplication.translate("MainWindow", "Short circuit evaluation"))
        self.generateButton.setText(QtCore.QCoreApplication.translate("MainWindow", "Generate Exercise"))
        self.dbButton.setText(QtCore.QCoreApplication.translate("MainWindow", "Database"))
        self.outputLabel.setText(QtCore.QCoreApplication.translate("MainWindow", "Welcome!"))
        self.titleLabel.setText(QtCore.QCoreApplication.translate("MainWindow", self.comboBox.currentText()))

        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
