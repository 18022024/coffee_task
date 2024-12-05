import io
import sys
from PyQt6 import uic
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QWidget, QApplication

db_code = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>850</width>
    <height>550</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QTableView" name="db_table">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>40</y>
     <width>700</width>
     <height>400</height>
    </rect>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Table(QWidget):
    def __init__(self):
        super().__init__()
        f = io.StringIO(db_code)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('types')
        model.select()
        self.db_table.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Table()
    ex.show()
    sys.exit(app.exec())