import configparser


class ConfigHelper:
    def __init__(self, path: str = 'configs/config.ini'):
        self.path = path
        self.parser = configparser.ConfigParser()
        self.parser.read(path)

    def get(self, section: str, key: str):
        return self.parser.get(section, key)

    def getint(self, section: str, key: str):
        return self.parser.getint(section, key)

    def getboolean(self, section: str, key: str):
        return self.parser.getboolean(section, key)

    def getfloat(self, section: str, key: str):
        return self.parser.getfloat(section, key)

    def set(self, section: str, key: str, value):
        self.parser.set(section, key, value)
        with open(self.path, 'w') as config_file:
            self.parser.write(config_file)
