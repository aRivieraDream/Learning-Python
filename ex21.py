print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newline and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires explanation
\n\t\twhere there is none.
"""

print "__________________"
print poem
print "__________________"

five = 10 -2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
start_point = 10000
beans, jars, crates = secret_formula(start_point)

def sentence(beans, jars, crates):
	print "This replaces repeating strings"
	print "We have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#	this is a helper method which unpacks a single var into three vars to be passed to 
#sentence
def sen2(vars):
	beans, jars, crates = vars
	return sentence(beans, jars, crates)

print "With a starting point of: %d" % start_point
print "We have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10 

print "We can also do that this way."
#print "We have %d beans, %d jars, and %d crates." % secret_formula(start_point)
#replace last line with call to function
print sen2(secret_formula(start_point))
