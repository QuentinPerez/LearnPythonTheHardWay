

def print_all(*args):
    str1, str2, bool1 = args
    print str1, str2, bool1


def print_two(arg1, arg2):
    print "arg1 %s, arg2 %s" % (arg1, arg2)


def print_none():
    print "none"

print_all("titi", 'toto', False)
print_two("1", "2")
print_none()
