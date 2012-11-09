from ConfigParser import SafeConfigParser

class Section():
    def __init__(self, item_list):
        for i in item_list:
            self.__dict__[i] = None
    def __str__(self):
        return repr(self.__dict__)

class Base():
    def __init__(self, conf):
        self.__conf__ = SafeConfigParser()
        self.__conf__.read(conf)
        for section_name in dir(self):
            section = getattr(self, section_name)
            if isinstance(section, Section):
                for option_name in section.__dict__:
                    section.__dict__[option_name] = self.__conf__.get(section_name, option_name)
