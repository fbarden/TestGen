# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/send_cli.ui'
#
# Created: Wed Mar  6 19:40:45 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import devices
import interfaces
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_sendCLIDialog(object):

    def isCLI(self, s):
        if s.find(".cli") == -1:
            return False
        else:
            return True

    def createDeviceList(self, comboBox=None):
        if (comboBox==None) :
            comboBox = self.deviceComboBox
        device_list = devices.get_list()
        for device in device_list :
            if devices.has_method(device, "SendCLI") :
                comboBox.addItem(_fromUtf8(device))

    def createInterfaceList(self, comboBox=None):
        if (comboBox==None) :
            comboBox = self.interfaceComboBox
        interface_list = interfaces.get_list()
        for interface in interface_list :
            comboBox.addItem(_fromUtf8(interface[0]))

    def updateMethodList(self, interfaceSelection, listBox=None):
        if (listBox==None) :
            listBox = self.methodList
        listBox.clear()
        interface_dir = interfaces.get_interface_value(interfaceSelection)
        files_list = filter(self.isCLI, os.listdir(interface_dir))
        files_list.append('<none>')
        for file_name in files_list:
            item = QtGui.QListWidgetItem()
            item.setText(_fromUtf8(file_name))
            font = QtGui.QFont()
            font.setBold(False)
            font.setWeight(50)
            item.setFont(font)
            self.methodList.addItem(item)

    def updatePreview(self, commandSelection, interfaceSelection=None, previewBox=None):
        if (interfaceSelection==None) :
            interfaceSelection = self.interfaceComboBox.currentText()
        if (previewBox==None) :
            previewBox = self.previewTextEdit
        previewBox.clear()
        if (commandSelection=="") or (commandSelection=="<none>") :
            return
        interface_dir = interfaces.get_interface_value(interfaceSelection)
        command_file = interface_dir+commandSelection
        command_preview = open(command_file, 'r').read()
        previewBox.setText(command_preview)

    def updateCheckBox(self, deviceSelection):
        device_str = str(deviceSelection)
        self.rebootCheckBox.setEnabled(devices.has_method(device_str, "Reboot"))
        self.loginCheckBox.setEnabled(devices.has_method(device_str, "Login"))
        self.logoutCheckBox.setEnabled(devices.has_method(device_str, "Login"))


    def acceptSendCLI(self):
        special_case = False
        login_param = ""
        login_flag = ""
        logout_flag = ""
        device = str(self.deviceComboBox.currentText())
        index =  str(self.deviceIndexEdit.text())
        if self.loginCheckBox.isChecked() :
            login_param = " " + devices.get_device_value(device, "Login", index)
            login_flag = " --login"
            special_case = True
        if self.logoutCheckBox.isChecked() :
            logout_flag = " --logout"
            special_case = True
        if self.rebootCheckBox.isChecked() :
            reboot_params = " " + devices.get_device_value(device, "Reboot", index)
            result = "SendCLI_v2.py" + login_param + reboot_params + login_flag + logout_flag + "\n"
            return result
        device_params = " " + devices.get_device_value(device, "SendCLI", index)
        interface_dir = " " + interfaces.get_interface_print_value(self.interfaceComboBox.currentText())
        methodItem = self.methodList.currentItem()
        if ((methodItem == None) or (methodItem.text() == "<none>")):
            command_file='<none>'
        else :
            command_file = " -f" + interface_dir + self.methodList.currentItem().text()
        arguments = " " + self.argumentsEdit.text()
        if (command_file=="<none>"):
                if special_case:
                    result = "SendCLI_v2.py" + device_params + login_param + login_flag + logout_flag + "\n"
                    return result
        result = "SendCLI_v2.py" + device_params + login_param + command_file + arguments + login_flag + logout_flag + "\n"
        return result

    def setupUi(self, sendCLIDialog, parentUi):
        sendCLIDialog.setObjectName(_fromUtf8("sendCLIDialog"))
        sendCLIDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        sendCLIDialog.resize(617, 625)
        self.verticalLayout = QtGui.QVBoxLayout(sendCLIDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.sendCLILabel = QtGui.QLabel(sendCLIDialog)
        self.sendCLILabel.setObjectName(_fromUtf8("sendCLILabel"))
        self.horizontalLayout_4.addWidget(self.sendCLILabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.deviceLabel = QtGui.QLabel(sendCLIDialog)
        self.deviceLabel.setAccessibleName(_fromUtf8(""))
        self.deviceLabel.setObjectName(_fromUtf8("deviceLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.deviceLabel)
        self.deviceComboBox = QtGui.QComboBox(sendCLIDialog)
        self.deviceComboBox.setAccessibleName(_fromUtf8(""))
        self.deviceComboBox.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.deviceComboBox.setObjectName(_fromUtf8("deviceComboBox"))
        self.createDeviceList(self.deviceComboBox)
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.deviceComboBox)
        self.deviceIndexLabel = QtGui.QLabel(sendCLIDialog)
        self.deviceIndexLabel.setObjectName(_fromUtf8("deviceIndexLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.deviceIndexLabel)
        self.deviceIndexEdit = QtGui.QLineEdit(sendCLIDialog)
        self.deviceIndexEdit.setObjectName(_fromUtf8("deviceIndexEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.deviceIndexEdit)
        self.interfaceLabel = QtGui.QLabel(sendCLIDialog)
        self.interfaceLabel.setAccessibleName(_fromUtf8(""))
        self.interfaceLabel.setObjectName(_fromUtf8("interfaceLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.interfaceLabel)
        self.interfaceComboBox = QtGui.QComboBox(sendCLIDialog)
        self.interfaceComboBox.setAccessibleName(_fromUtf8(""))
        self.interfaceComboBox.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.interfaceComboBox.setObjectName(_fromUtf8("interfaceComboBox"))
        self.createInterfaceList(self.interfaceComboBox)
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.interfaceComboBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.commandsLabel = QtGui.QLabel(sendCLIDialog)
        self.commandsLabel.setObjectName(_fromUtf8("commandsLabel"))
        self.horizontalLayout_2.addWidget(self.commandsLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.methodList = QtGui.QListWidget(sendCLIDialog)
        self.methodList.setAccessibleName(_fromUtf8(""))
        self.methodList.setObjectName(_fromUtf8("methodList"))
        self.updateMethodList(self.interfaceComboBox.currentText(), self.methodList)
        self.verticalLayout_2.addWidget(self.methodList)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.previewLabel = QtGui.QLabel(sendCLIDialog)
        self.previewLabel.setObjectName(_fromUtf8("previewLabel"))
        self.horizontalLayout_3.addWidget(self.previewLabel)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.previewTextEdit = QtGui.QTextEdit(sendCLIDialog)
        self.previewTextEdit.setAccessibleName(_fromUtf8(""))
        self.previewTextEdit.setReadOnly(True)
        self.previewTextEdit.setObjectName(_fromUtf8("previewTextEdit"))
        self.verticalLayout_3.addWidget(self.previewTextEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.argumentsLabel = QtGui.QLabel(sendCLIDialog)
        self.argumentsLabel.setAccessibleName(_fromUtf8(""))
        self.argumentsLabel.setObjectName(_fromUtf8("argumentsLabel"))
        self.gridLayout.addWidget(self.argumentsLabel, 0, 0, 1, 1)
        self.argumentsEdit = QtGui.QLineEdit(sendCLIDialog)
        self.argumentsEdit.setAccessibleName(_fromUtf8(""))
        self.argumentsEdit.setObjectName(_fromUtf8("argumentsEdit"))
        self.gridLayout.addWidget(self.argumentsEdit, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.rebootCheckBox = QtGui.QCheckBox(sendCLIDialog)
        self.rebootCheckBox.setAccessibleName(_fromUtf8(""))
        self.rebootCheckBox.setObjectName(_fromUtf8("rebootCheckBox"))
        self.gridLayout_2.addWidget(self.rebootCheckBox, 0, 0, 1, 1)
        self.loginCheckBox = QtGui.QCheckBox(sendCLIDialog)
        self.loginCheckBox.setAccessibleName(_fromUtf8(""))
        self.loginCheckBox.setObjectName(_fromUtf8("loginCheckBox"))
        self.gridLayout_2.addWidget(self.loginCheckBox, 0, 1, 1, 1)
        self.logoutCheckBox = QtGui.QCheckBox(sendCLIDialog)
        self.logoutCheckBox.setAccessibleName(_fromUtf8(""))
        self.logoutCheckBox.setObjectName(_fromUtf8("logoutCheckBox"))
        self.gridLayout_2.addWidget(self.logoutCheckBox, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(sendCLIDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.deviceLabel.setBuddy(self.deviceComboBox)
        self.interfaceLabel.setBuddy(self.interfaceComboBox)
        self.argumentsLabel.setBuddy(self.argumentsEdit)

        self.retranslateUi(sendCLIDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), lambda : parentUi.acceptTeststep(self.acceptSendCLI()))
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), sendCLIDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), sendCLIDialog.reject)
        QtCore.QObject.connect(self.deviceComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), lambda deviceSelection=self.deviceComboBox.currentText() : self.updateCheckBox(deviceSelection))
        QtCore.QObject.connect(self.interfaceComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.previewTextEdit.clear)
        QtCore.QObject.connect(self.interfaceComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), lambda interfaceSelection=self.interfaceComboBox.currentText(), listBox=self.methodList : self.updateMethodList(interfaceSelection, listBox)  )
        QtCore.QObject.connect(self.methodList, QtCore.SIGNAL(_fromUtf8("currentTextChanged(QString)")), self.updatePreview)
        QtCore.QMetaObject.connectSlotsByName(sendCLIDialog)

        sendCLIDialog.setTabOrder(self.deviceComboBox, self.interfaceComboBox)
        sendCLIDialog.setTabOrder(self.interfaceComboBox, self.methodList)
        sendCLIDialog.setTabOrder(self.methodList, self.argumentsEdit)
        sendCLIDialog.setTabOrder(self.argumentsEdit, self.rebootCheckBox)
        sendCLIDialog.setTabOrder(self.rebootCheckBox, self.loginCheckBox)
        sendCLIDialog.setTabOrder(self.loginCheckBox, self.logoutCheckBox)
        sendCLIDialog.setTabOrder(self.logoutCheckBox, self.buttonBox)

    def retranslateUi(self, sendCLIDialog):
        sendCLIDialog.setWindowTitle(QtGui.QApplication.translate("sendCLIDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.sendCLILabel.setText(QtGui.QApplication.translate("sendCLIDialog", "SendCLI_v2", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceLabel.setText(QtGui.QApplication.translate("sendCLIDialog", "Device:", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceIndexLabel.setText(QtGui.QApplication.translate("sendCLIDialog", "Device Index:", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceIndexEdit.setText(QtGui.QApplication.translate("sendCLIDialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.interfaceLabel.setText(QtGui.QApplication.translate("sendCLIDialog", "Interface:", None, QtGui.QApplication.UnicodeUTF8))
        self.commandsLabel.setText(QtGui.QApplication.translate("sendCLIDialog", "Commands", None, QtGui.QApplication.UnicodeUTF8))
        self.methodList.setSortingEnabled(True)
        __sortingEnabled = self.methodList.isSortingEnabled()
        self.methodList.setSortingEnabled(False)
        self.methodList.setSortingEnabled(__sortingEnabled)
        self.previewLabel.setText(QtGui.QApplication.translate("sendCLIDialog", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.argumentsLabel.setText(QtGui.QApplication.translate("sendCLIDialog", "Arguments:", None, QtGui.QApplication.UnicodeUTF8))
        self.rebootCheckBox.setText(QtGui.QApplication.translate("sendCLIDialog", "reboot", None, QtGui.QApplication.UnicodeUTF8))
        self.loginCheckBox.setText(QtGui.QApplication.translate("sendCLIDialog", "login", None, QtGui.QApplication.UnicodeUTF8))
        self.logoutCheckBox.setText(QtGui.QApplication.translate("sendCLIDialog", "logout", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    sendCLIDialog = QtGui.QDialog()
    ui = Ui_sendCLIDialog()
    ui.setupUi(sendCLIDialog, None)
    sendCLIDialog.show()
    sys.exit(app.exec_())

