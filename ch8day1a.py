__author__ = 'ortus'


def string(s):
    if len(s) >= 5:
        print(s[4])
    elif len(s) <= 5:
        return None

string("See")
string("See Spot")
string("See Spot Run")
string("Run Spot, Run")
