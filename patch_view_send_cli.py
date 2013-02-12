import devices
import interfaces

    def createInterfaceList(self, comboBox):
        interface_list = interfaces.get_list()
        for interface in interface_list :
	    comboBox.addItem(_fromUtf8(interface[0]))

    def createDeviceList(self, comboBox):
        device_list = devices.get_list()
        for device in device_list :
            comboBox.addItem(_fromUtf8(device))

    def setupUi(self, Form):
	self.createDeviceList(self.deviceComboBox)
        self.createInterfaceList(self.interfaceComboBox)
