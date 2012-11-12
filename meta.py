from ConfigParser import SafeConfigParser

class LowerSectionConfigParser(SafeConfigParser):
    def _read(self, fp, fpname):
        SafeConfigParser._read(self, fp, fpname)
        new_sections = self._dict()
        for a_section in self._sections:
            tmp = self._sections[a_section]
            new_sections[a_section.lower()] = tmp
        self._sections = new_sections


class Section():
    def __init__(self, item_list):
        for i in item_list:
            self.__dict__[i] = None

    def __str__(self):
        return repr(self.__dict__)


class Base():
    def __init__(self, conf):
        self.__conf__ = LowerSectionConfigParser()
        self.__conf__.read(conf)
        for section_name in dir(self):
            section = getattr(self, section_name)
            if isinstance(section, Section):
                for option_name in section.__dict__:
                    section.__dict__[option_name] = self.__conf__.get(section_name, option_name)
