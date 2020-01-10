# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.


def find_second(S, t):
    first = S.find(t)
    second = S.find(t, first+1)
    return second


danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')


# Solution 2
def find_second(S, t):
    first = S.find(t)
    return S.find(t, first+1)


danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')
# Solition 3


def find_second(S, t):
    return S.find(t, S.find(t)+1)


danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')

#danton = "De l'audace, encore de l'audace, toujours de l'audace"
#print find_second(danton, 'audace')
# >>> 25

#twister = "she sells seashells by the seashore"
#print find_second(twister,'she')
# >>> 13
