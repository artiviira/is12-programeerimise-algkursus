from random import randint
import time
klass = ['Kairo','Aigar','Timo','Arti']
print klass
print len(klass)
a=len(klass)
a = randint(0,a-1)
vastaja = "Klassi ette tuleb vastama "
print vastaja+klass[a]
del klass[a]
print klass
print len(klass)
a=len(klass)
a = randint(0,a-1)
print vastaja+klass[a]






