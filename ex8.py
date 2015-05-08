formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.", # note here that the double quotes get converted to single quotes. 
	"That you could type up right.",
	"But it didn't sing.", # the real question is why are these in double quotes
	"So I said goodnight." 
)

print 'This is for "doublequotes."'