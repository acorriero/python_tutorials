from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s." % (from_file, to_file)

indata = open(from_file).read()

print "File %s exists? %r " % (to_file, exists(to_file))
raw_input("Are you sure? Hit enter to continue or ctrl d to exit.")

out_file = open(to_file, 'w').write(indata)

print " all done"
