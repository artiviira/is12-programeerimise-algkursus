from random import randint

kuulid = ['s']*5 + ['m']*10 + ['v']*15


arv = len(kuulid)-1
kuul = randint(0,arv)
kuul1 = kuulid[kuul]
print kuul1
del kuulid[kuul]


arv = len(kuulid)-1
kuul = randint(0,arv)
kuul2 = kuulid[kuul]
print kuul2
del kuulid[kuul]






