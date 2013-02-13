# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/send_cli.ui'
#
# Created: Tue Feb 12 18:13:59 2013
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

class Ui_sendCLIForm(object):

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
        if self.loginCheckBox.isChecked() :
            login_param = " " + devices.get_device_value(device, "Login")
            login_flag = " --login"
            special_case = True
        if self.logoutCheckBox.isChecked() :
            logout_flag = " --logout"
            special_case = True
        if self.rebootCheckBox.isChecked() :
            reboot_params = " " + devices.get_device_value(device, "Reboot")
            result = "SendCLI_v2.py" + login_param + reboot_params + login_flag + logout_flag + "\n"
            print result
            return
        device_params = " " + devices.get_device_value(device, "SendCLI")
        interface_dir = " " + interfaces.get_interface_value(self.interfaceComboBox.currentText())
        methodItem = self.methodList.currentItem()
        if (methodItem == None):
            command_file='<none>'
        else :
            command_file = " -f" + interface_dir + self.methodList.currentItem().text()
        arguments = " " + self.argumentsEdit.text()
        if (command_file=="<none>"):
                if special_case:
                    result = "SendCLI_v2.py" + device_params + login_param + login_flag + logout_flag + "\n"
                    print result
                    sendCLIForm.close()
                return
        result = "SendCLI_v2.py" + device_params + login_param + command_file + arguments + login_flag + logout_flag + "\n"
        print result
        sendCLIForm.close()

    def setupUi(self, sendCLIForm):
        sendCLIForm.setObjectName(_fromUtf8("sendCLIForm"))
        sendCLIForm.setWindowModality(QtCore.Qt.ApplicationModal)
        sendCLIForm.resize(401, 388)
        sendCLIForm.setAccessibleName(_fromUtf8(""))
        self.verticalLayout = QtGui.QVBoxLayout(sendCLIForm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.deviceLabel = QtGui.QLabel(sendCLIForm)
        self.deviceLabel.setAccessibleName(_fromUtf8(""))
        self.deviceLabel.setObjectName(_fromUtf8("deviceLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.deviceLabel)
        self.deviceComboBox = QtGui.QComboBox(sendCLIForm)
        self.deviceComboBox.setAccessibleName(_fromUtf8(""))
        self.deviceComboBox.setObjectName(_fromUtf8("deviceComboBox"))
        self.createDeviceList(self.deviceComboBox)
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.deviceComboBox)
        self.interfaceLabel = QtGui.QLabel(sendCLIForm)
        self.interfaceLabel.setAccessibleName(_fromUtf8(""))
        self.interfaceLabel.setObjectName(_fromUtf8("interfaceLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.interfaceLabel)
        self.interfaceComboBox = QtGui.QComboBox(sendCLIForm)
        self.interfaceComboBox.setAccessibleName(_fromUtf8(""))
        self.interfaceComboBox.setObjectName(_fromUtf8("interfaceComboBox"))
        self.createInterfaceList(self.interfaceComboBox)
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.interfaceComboBox)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.methodList = QtGui.QListWidget(sendCLIForm)
        self.methodList.setAccessibleName(_fromUtf8(""))
        self.methodList.setObjectName(_fromUtf8("methodList"))
        self.updateMethodList(self.interfaceComboBox.currentText(), self.methodList)
        self.horizontalLayout.addWidget(self.methodList)
        self.previewTextEdit = QtGui.QTextEdit(sendCLIForm)
        self.previewTextEdit.setAccessibleName(_fromUtf8(""))
        self.previewTextEdit.setReadOnly(True)
        self.previewTextEdit.setObjectName(_fromUtf8("previewTextEdit"))
        self.horizontalLayout.addWidget(self.previewTextEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.argumentsLabel = QtGui.QLabel(sendCLIForm)
        self.argumentsLabel.setAccessibleName(_fromUtf8(""))
        self.argumentsLabel.setObjectName(_fromUtf8("argumentsLabel"))
        self.gridLayout.addWidget(self.argumentsLabel, 0, 0, 1, 1)
        self.argumentsEdit = QtGui.QLineEdit(sendCLIForm)
        self.argumentsEdit.setAccessibleName(_fromUtf8(""))
        self.argumentsEdit.setObjectName(_fromUtf8("argumentsEdit"))
        self.gridLayout.addWidget(self.argumentsEdit, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.rebootCheckBox = QtGui.QCheckBox(sendCLIForm)
        self.rebootCheckBox.setAccessibleName(_fromUtf8(""))
        self.rebootCheckBox.setObjectName(_fromUtf8("rebootCheckBox"))
        self.gridLayout_2.addWidget(self.rebootCheckBox, 0, 0, 1, 1)
        self.loginCheckBox = QtGui.QCheckBox(sendCLIForm)
        self.loginCheckBox.setAccessibleName(_fromUtf8(""))
        self.loginCheckBox.setObjectName(_fromUtf8("loginCheckBox"))
        self.gridLayout_2.addWidget(self.loginCheckBox, 0, 1, 1, 1)
        self.logoutCheckBox = QtGui.QCheckBox(sendCLIForm)
        self.logoutCheckBox.setAccessibleName(_fromUtf8(""))
        self.logoutCheckBox.setObjectName(_fromUtf8("logoutCheckBox"))
        self.gridLayout_2.addWidget(self.logoutCheckBox, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(sendCLIForm)
        self.buttonBox.setAccessibleName(_fromUtf8(""))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.deviceLabel.setBuddy(self.deviceComboBox)
        self.interfaceLabel.setBuddy(self.interfaceComboBox)
        self.argumentsLabel.setBuddy(self.argumentsEdit)

        self.retranslateUi(sendCLIForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), sendCLIForm.close)
        QtCore.QObject.connect(self.deviceComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.updateCheckBox)
        QtCore.QObject.connect(self.interfaceComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.previewTextEdit.clear)
        QtCore.QObject.connect(self.interfaceComboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.updateMethodList)
        QtCore.QObject.connect(self.methodList, QtCore.SIGNAL(_fromUtf8("currentTextChanged(QString)")), self.updatePreview)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.acceptSendCLI)
        QtCore.QMetaObject.connectSlotsByName(sendCLIForm)

        sendCLIForm.setTabOrder(self.deviceComboBox, self.interfaceComboBox)
        sendCLIForm.setTabOrder(self.interfaceComboBox, self.methodList)
        sendCLIForm.setTabOrder(self.methodList, self.argumentsEdit)
        sendCLIForm.setTabOrder(self.argumentsEdit, self.rebootCheckBox)
        sendCLIForm.setTabOrder(self.rebootCheckBox, self.loginCheckBox)
        sendCLIForm.setTabOrder(self.loginCheckBox, self.logoutCheckBox)
        sendCLIForm.setTabOrder(self.logoutCheckBox, self.buttonBox)

    def retranslateUi(self, sendCLIForm):
        sendCLIForm.setWindowTitle(QtGui.QApplication.translate("sendCLIForm", "SendCLI", None, QtGui.QApplication.UnicodeUTF8))
        self.deviceLabel.setText(QtGui.QApplication.translate("sendCLIForm", "Device:", None, QtGui.QApplication.UnicodeUTF8))
        self.interfaceLabel.setText(QtGui.QApplication.translate("sendCLIForm", "Interface:", None, QtGui.QApplication.UnicodeUTF8))
        self.methodList.setSortingEnabled(True)
        __sortingEnabled = self.methodList.isSortingEnabled()
        self.methodList.setSortingEnabled(False)
        self.methodList.setSortingEnabled(__sortingEnabled)
        self.argumentsLabel.setText(QtGui.QApplication.translate("sendCLIForm", "Arguments:", None, QtGui.QApplication.UnicodeUTF8))
        self.rebootCheckBox.setText(QtGui.QApplication.translate("sendCLIForm", "reboot", None, QtGui.QApplication.UnicodeUTF8))
        self.loginCheckBox.setText(QtGui.QApplication.translate("sendCLIForm", "login", None, QtGui.QApplication.UnicodeUTF8))
        self.logoutCheckBox.setText(QtGui.QApplication.translate("sendCLIForm", "logout", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    sendCLIForm = QtGui.QWidget()
    ui = Ui_sendCLIForm()
    ui.setupUi(sendCLIForm)
    sendCLIForm.show()
    sys.exit(app.exec_())

