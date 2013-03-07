import ConfigParser

devices_file = 'config/devices.conf'

def open_devices_config():
    config_file = ConfigParser.SafeConfigParser()
    config_file.optionxform=str
    config_file.read(devices_file)
    return config_file

def get_list():
    config_file = open_devices_config()
    return config_file.sections()

def get_commands_list(device):
    config_file = open_devices_config()
    return config_file.options(device)

def get_device_value(device, command, index):
    config_file = open_devices_config()
    config_file.set('DEFAULT', 'index', index)
    return config_file.get(device, command)

def has_method(device, method):
    config_file = open_devices_config()
    return config_file.has_option(device, method)
