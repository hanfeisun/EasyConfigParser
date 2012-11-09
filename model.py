from meta import Section, Base
class Conf(Base):
    basis = Section(["user", "time"])
    bowtie = Section(["path", "index"])







