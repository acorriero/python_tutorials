from sys import argv

script, filename = argv

print "we going to rease %r" % filename
print "if not ctrl c" 
print "fi ok hit retrun"

raw_input("?")

print "open file .."
target = open(filename, 'w')

#print 'truncating '
#target.truncate()

print "now im going task for 3 line"

line1 = raw_input("1 ")
line2 = raw_input("2 ")
line3 = raw_input("3 ")

print "im going to writ these t ofile %s" % filename

target.write("%s\n%s\n%s" % (line1, line2, line3))

target.close()

target = open(filename)
print target.read()
target.close()
