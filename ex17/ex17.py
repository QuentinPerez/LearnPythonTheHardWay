from sys import argv
from os.path import exists

_, filename = argv

print '%s exist ? %r' % (filename, exists(filename))
