A wrapper for Python's config parser


You can create a config file:

```
[basis]
user = sunhf
time = 2012-12-31
memo =

[BowtIE]
# case insensitive for section name

path = /usr/bin/bowtie
Index = /mnt/Storage/sync/hg19
```

And then use it like this:

```
import Conf

cf = Conf("rule.conf")

print cf.basis
print cf.basis.user
print cf.basis.time

print cf.bowtie
print cf.bowtie.path
print cf.bowtie.index
```
