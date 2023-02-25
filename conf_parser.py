import configparser

def get_configs(file_name):
    config = configparser.ConfigParser()
    config.read(file_name)
    print(config.sections())
    
    