from PyQt5.QtWidgets import QWidget, QAction, QMenu
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5 import uic, QtCore, QtSql
import DataBaseModule

class DataBaseForm(QWidget):
    '''Форма базы данных'''
    def __init__(self):
        super().__init__()
        uic.loadUi("DataBaseForm.ui", self)
        self.idModel = 0
        self.GetTableModel('wordsgrouptab')
        self.comboBox.currentIndexChanged.connect(self.RefreshTable)
        self.InitContextMenu()

    def GetTableModel(self, table):
        '''Вывод модели таблицы'''
        if table == 'dialogtab': model = DataBaseModule.GetTableViewModel("select * from " +table, 'dialogtab')
        else: model = DataBaseModule.GetTableViewModel("select * from " +table, 'dialogtab')
        self.tableView.setModel(model[0])
        self.tableView.resizeRowsToContents()
        self.tableView.resizeColumnsToContents()
        self.idModel = model[1]
        self.lineEdit.setText(str(self.idModel))


    def RefreshTable(self):
        '''Обновить таблицу '''
        self.GetTableModel(self.comboBox.currentText())

    def InitContextMenu(self):
        '''инициализация контекстного меню'''
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableView.customContextMenuRequested.connect(self.RunContextMenu)

        self.moreInfoAct = QAction('Подробнее', self)
        self.moreInfoAct.triggered.connect(self.OpenMoreInfoForm)
        self.deleteRecordAct =QAction('Удалить запись', self)

    def RunContextMenu(self, pos):
        '''Запуск контекстного меню'''
        menu = QMenu(self)
        menu.addAction(self.moreInfoAct)
        menu.addAction(self.deleteRecordAct)
        menu.exec_(self.sender().mapToGlobal(pos))

    def OpenMoreInfoForm(self):
        currentDiscount = self.tableView.currentIndex()
        self.lineEdit.setText(self.tableView.model().data(self.tableView.model().index(currentDiscount.row(), self.idModel), 0))

