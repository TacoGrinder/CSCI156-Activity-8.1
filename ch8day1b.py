__author__ = 'ortus'


def revrs(s):
    for i in reversed(range(len(s))):
        print(s[i])


revrs("1234ABCD")