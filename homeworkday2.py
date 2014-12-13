__author__ = 'ortus'


def qlegit2quit():
    i = 1
    while i != 0:
        print("Hi!")
        x = input("type Q for quit").upper().strip()
        if x == "Q":
            return x



qlegit2quit()