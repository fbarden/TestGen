import ConfigParser

paths_file = '../config/paths.conf'

def get_commands_path():
	config_file = ConfigParser.RawConfigParser()
	config_file.read(paths_file)
	return config_file.get('PATHS', 'commands')

def get_commands_print_path():
	config_file = ConfigParser.RawConfigParser()
	config_file.read(paths_file)
	return config_file.get('PATHS', 'commands_print')

def get_testcases_path():
	config_file = ConfigParser.RawConfigParser()
	config_file.read(paths_file)
	return config_file.get('PATHS', 'testcases')
