# don't run ex28.py in terminal, instead run python and type in Boolean problems

print "ex28"
print "Boolean Practice\n"

True and True # (AND) => True -> correct
False and True # (AND) => False  -> correct
1 == 1 and 2 == 1 # True AND False => FALSE -> correct
"test" == "test" # TRUE -> correct
1 == 1 or 2 != 1 # True OR True => TRUE -> correct
True and 1 == 1 # True AND True => TRUE -> correct
False and 0 != 0 # False AND FALSE => FALSE -> correct
True or 1 == 1 # True OR True => TRUE -> correct
"test" == "testing" # FALSE -> correct
1 != 0 and 2 == 1 # True AND False => FALSE -> correct
"test" != "testing" # TRUE -> correct
"test" == 1 # FALSE -> correct
not (True and False) # not (False) => TRUE -> correct
not (1 == 1 and 0 != 1) # not(True and True -> True) => FALSE -> correct
not (10 == 1 or 1000 == 1000) # not (False or True -> True) => FALSE -> correct
not (1 != 10 or 3 == 4) # not(True or False -> True) => FALSE -> correct
not ("testing" == "testing" and "Eileen" == "Cool Gal") # not (True and False -> False) => TRUE -> correct
1 == 1 and (not ("testing" == 1 or 1 == 0)) # True and not (False or False -> False) => TRUE -> correct
"chunky" == "bacon" and (not (3 == 4 or 3 == 3)) # False and not (False or True -> True) => FALSE -> correct
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) # True and not (True or False -> True) => FALSE -> correct

#False and will aways end in false
#True or will always end in true