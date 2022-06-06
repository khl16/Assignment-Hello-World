

# 1. TASK: print "Hello World"
print(  "Hello World" )


# 2. print "Hello Noelle!" with the name in a variable
name2 = "kahled"
print( "Hello World",name2)	# with a comma
print( "Hello World "+name2 )	# with a +


# 3. print "Hello 42!" with the number in a variable
name3 = 27
print( "Hello World",name3 )	# with a comma
# print( "Hello World"+name3 )	# with a +	-- this one should give us an error!


# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat".format(fave_food1) ) # with .format()
print( "I love to eat ", f"{fave_food2}"+" and "+f"{fave_food1}" ) # with an f string

