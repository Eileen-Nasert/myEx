print "ex08"
print "Printing, Printing\n"

formatter = "%r %r %r %r"
print formatter % (1, 2 , 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True) 
#python recognizes true and false as keywords, quotes would make them into strings and they wouldn't work in python anymore
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)