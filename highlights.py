import ConfigParser

highlight_file = 'config/highlights.conf'

def open_highlights_config():
    config_file = ConfigParser.SafeConfigParser()
    config_file.optionxform=str
    config_file.read(highlight_file)
    return config_file

def get_styles_list():
    config_file = open_highlights_config()
    return config_file.options('Styles')

def get_devices_list():
    config_file = open_highlights_config()
    return config_file.options('Devices')

def get_style_value(style):
    config_file = open_highlights_config()
    return config_file.get('Styles', style)

def get_device_value(device):
    config_file = open_highlights_config()
    return config_file.get('Devices', device)