from sys import argv

_, filename = argv

fd = open(filename)

print "The file %r" % filename
print fd.read()
