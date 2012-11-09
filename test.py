from model import Conf

cf = Conf("rule.conf")

print cf.basis
print cf.basis.user
print cf.basis.time

print cf.bowtie
print cf.bowtie.path
print cf.bowtie.index