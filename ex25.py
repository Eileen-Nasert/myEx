# defining a function called 'break_words' with only one argument called 'stuff' (internal/local name) 
def break_words(stuff):
	""" This function will break up words for us."""
	words = stuff.split(' ') # function/command .split (on spaces (' ')) the object stuff and name it variable words
	return words # return makes the result of function available to other function, it does not print

# taking the results of first function (out put of previous return) and feeding it into this function (input)
def sort_words(words):
	""" Sorts the words."""
	return sorted(words)

# finds first word and prints it
def print_first_word(words):
	"""Prints the first worlds after popping it off."""
	word = words.pop(0) # function finds first world we typed into the console
	print word # displays first word in console

# finds last word and prints it
def print_last_word(words):
	""" Prints the last world after popping it off."""
	word = words.pop(-1)
	print word

# this single argument () needs an entire sentence
# this is a second order function because it uses previously defined function
# this function does the same thing as the first to functions combined: break and sort
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence) # reads sentence into worlds and sort it
	return sort_words(words)

# second order function (because it uses break_words, printed_last_words and printed_first_words)
def print_first_and_last(sentence):
	"""Prints the first and last worlds of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
# we can also type: return sort_words(break_words(sentence))
	
# another second order function
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)	


# """ called documentation comments
# we are executing from python (within terminal) not the command line, therefore
# this is not called a script, but a module
# this document defines several functions 
# .split is built in function/command -> in this case it splits on spaces
# return makes the result of function available to other function, it does not print
# .sorted is built in function which sorts the
# .pop(0) function finds the very first word of sth. we typed in
# .pop(-1) function finds the very last word of sth. we typed in
# you can print ever function's result by simply typing: print ex25.break_words(sentence)
# type: help(ex25) to get help on module
# type: help(ex25 break_words) to get help on specific function
# if you type from ex25 import at the beginning you don't have to specify ex25. when running function defined in module ex25
# just import a function grom a module from myscript import myfunction

# we need separate instruction to run this file in python:
# $ import ex25
# $ sentence = ”All good things come to those who wait.” # -> creating variable called sentence and assigning input sentence to it
# $ words = ex25.break_words(sentence) # ->importing module ex25.; then runs function 'break_words'; applying it to object (sentence) and feeding it into new variable called words
# $ words # to see result of new variable, which is also the output of function 1

# $ sorted_words = ex25.sort_words(words) # ->this runs function called sort_words in ex25. and then sorts the words alphabetically from previous new variable 'words'
# $ sorted_words

# $ ex25.print_first_word(words) # ->runs function print_first_word of module ex25. on object words; displays result automatically because function prints at the end
# $ ex25.print_last_word(words)
# $ words

# $ ex25.print_first_word(sorted_words) # ->runs function print_first_word of module ex25. on object sorted_words previously defined;
# $ ex25.print_last_word(sorted_words) # -> runs function print_last_word ....

# $ sorted_words = ex25.sort_sentence(sentence) # -> QEUSTION: are we renaming sorted_words?
# $ sorted_words

# $ ex25.print_first_and_last(sentence) # ->runs function print_first_and_last on object sentence
# $ ex25.print_first_and_last_sorted(sentence) # ->runs (last) function print_first_and_last_sorted
  
