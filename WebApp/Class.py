class Class:
    'This class represent classes, for example /CS225/'
    def __init__(self, clas):
        self.clas = clas
        self.sectionList = []
    def add_section(self, section):
        self.sectionList.append(section)
