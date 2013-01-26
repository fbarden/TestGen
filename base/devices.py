import ConfigParser

devices_file = '../config/devices.conf'

def get_list(command):
	config_file = ConfigParser.RawConfigParser()
	config_file.read(devices_file)
	return config_file.items(command)

def get_devices_list(command):
	config_file = ConfigParser.RawConfigParser()
	config_file.read(devices_file)
	return config_file.options(command)

def get_device_value(command, device):
	config_file = ConfigParser.RawConfigParser()
	config_file.read(devices_file)
	return config_file.get(command, device)
	