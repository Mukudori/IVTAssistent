from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, \
    QLineEdit, QPushButton, QComboBox

from clients_subsystem.rii.database.CathedraModule import Cathedra
from clients_subsystem.rii.database.ClientModule import Client

class CathedraForm(QWidget):
    def __init__(self, id=0, parent=0):
        super().__init__()
        self.ID=id
        self.Parent = parent
        self.initUI()
        if id:
            self.initEdit()

    def initUI(self):
        vLay = QVBoxLayout()
        hl1 = QHBoxLayout()
        self.lName = QLabel('Наименование')
        self.leName =QLineEdit()
        hl1.addWidget(self.lName)
        hl1.addWidget(self.leName)
        vLay.addLayout(hl1)

        hl2 = QHBoxLayout()
        self.lZav = QLabel('Заведующий')
        self.cbZav = QComboBox()
        hl2.addWidget(self.lZav)
        hl2.addWidget(self.cbZav)
        vLay.addLayout(hl2)

        self.pbSave = QPushButton('Сохранить')
        self.pbSave.clicked.connect(self.save)
        vLay.addWidget(self.pbSave)

        self.setLayout(vLay)

    def initEdit(self):
        rec = Cathedra().getRecord(self.ID)
        self.leName.setText(rec['name'])
        self.teacherList = Client().getTeachersListFromIDCath(rec['id'])
        self.cbZav.clear()
        self.cbZav.addItems([rec['shortfio'] for rec in self.teacherList])
        ind=-1
        for i in range(len(self.teacherList)):
            if rec['idZav'] == self.teacherList[i]['id']:
                ind = i
                break
        if ind!= -1:
            self.cbZav.setCurrentIndex(ind)

    def getIDZav(self):
        ind = self.cbZav.currentIndex()
        if ind < 0: ind = 0
        zav = self.teacherList[ind]['id']
        return zav

    def insertRecord(self):
        zav = self.getIDZav()
        Cathedra().insertRecord(name=self.leName.text(),
                                idZav=zav)

    def updateRecord(self):
        zav = self.getIDZav()
        Cathedra().updateRecord(id=self.ID,
                                name=self.leName.text(),
                                idZav=zav)


    def save(self):
        if self.ID:
            self.updateRecord()
        else:
            self.insertRecord()
        if self.Parent:
            self.Parent.RefreshTable()
        self.close()


