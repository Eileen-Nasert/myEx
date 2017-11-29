print "inclass ex\n"

# inclass ex1
name = raw_input('Type your name\n')
if not name.isalpha(): # .isalpha is command for looking if name is typed in all letters
	print "not a name!"
else: 
	print "Your name: %s" % name

# inclass ex2
myVar = 1/10.
print "%.16f" %myVar # this will print 16 numbers after the decimal point
print "%16.f" %myVar # this will print 16 numbers before the decimal point

# inclass ex3 using lists:
myLst_1=['zebra',5,False]
myStr='z' #-> Return false, because there is no item z in list
myStr in myLst[0] # zero refers to the first item/element of the list -> will return zebra
myStr in 'zebra' #which wis the same as myLst[0]
myStr in myLst[-1] #- 1 refers to last item in list myLst

myLst1=[3,4,2,8664,325,12]
mySet= set(myLst) #declaring a set by converting every list
myLst[2:6] # slices up list
len(myLst) #will give me the length
for i in myLst:
	print"\n", i
	
myLst.count('zebra') # counts how many times an item is occuring in a list
min(myLst) # will return smallest number or earliest letter in the alphatet
may(myLst)

myLstmix=[' ', 'strange', 33, True, '!']
min(myLstmix)

order of min: first boolean, then numbers, empty, character, then strings

myLstmix.remove(true)

Type your name
js0
not a name!
MacBook-Pro:Scripts Eileen$ python ex33.py
ex33
While Loops

Type your name
Eileen
Your name: Eileen
MacBook-Pro:Scripts Eileen$ python ex33.py
ex33
While Loops

Type your name
999
not a name!
MacBook-Pro:Scripts Eileen$ python
Python 2.7.14 |Anaconda, Inc.| (default, Oct  5 2017, 02:28:52) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> myLstmix=[' ', 'strange', 33, True, '!']
>>> min(myLstmix)
True
>>> myLstmix=[' ', 'strange', 33, '!']
>>> min(myLstmix)
33
>>> myLstmix=[' ', 'strange', '!']
>>> min(myLstmix)
' '
>>> myLstmic.remove(' ')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'myLstmic' is not defined
>>> myLstmix.remove(' ')
>>> myLst
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'myLst' is not defined