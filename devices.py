import ConfigParser

devices_file = 'config/devices.conf'

def get_list():
	config_file = ConfigParser.RawConfigParser()
	config_file.optionxform=str
	config_file.read(devices_file)
	return config_file.sections()

def get_commands_list(device):
	config_file = ConfigParser.RawConfigParser()
	config_file.optionxform=str
	config_file.read(devices_file)
	return config_file.options(device)

def get_device_value(device, command):
	config_file = ConfigParser.RawConfigParser()
	config_file.optionxform=str
	config_file.read(devices_file)
	return config_file.get(device, command)
	
