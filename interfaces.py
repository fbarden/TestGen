import paths
import ConfigParser

interfaces_file = 'config/interfaces.conf'

def get_list():
	config_file = ConfigParser.RawConfigParser()
	config_file.optionxform=str
	config_file.read(interfaces_file)
	return config_file.items('COMMANDS')

def get_interfaces_list():
	config_file = ConfigParser.RawConfigParser()
	config_file.optionxform=str
	config_file.read(interfaces_file)
	return config_file.options('COMMANDS')

def get_interface_value(interface):
	config_file = ConfigParser.RawConfigParser()
	config_file.optionxform=str
	config_file.read(interfaces_file)
	return (paths.get_commands_path() + config_file.get('COMMANDS', interface))
	
