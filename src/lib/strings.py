print("Strings is sequence of characters")

single_quoted_string = 'data science'
doule_quoted_string = "from scratch"
mixed_quoted_string = "I am n't going to gym today."
multi_line_string = """ This is the first line.
This is second line
This is third line"""

print( single_quoted_string)
print(doule_quoted_string)
print(mixed_quoted_string)
print(multi_line_string)

print( len(single_quoted_string))
print( len(doule_quoted_string))
print( len(mixed_quoted_string))
print(len(multi_line_string))

# escape characters
tab_string = "\t"
raw_tab_string = r"\t"
new_line_string = "\n"

print( len(tab_string) )
print( len(raw_tab_string) )
print( len(new_line_string) )

example_string = "Hello \n World. I am learning \t PYTHON."
print(example_string)

# String indexing
# Word:    Happy
# Index:   0 1 2 3 4
# Reverse: 0 -4 -3 -2 -1

my_string = "Happy"
print( my_string )
print( len(my_string) )
print( my_string[ len( my_string) - 1] )

print("String indexing")
print( my_string[0] )
print( my_string[1] )
print( my_string[2] )
print( my_string[3] )
print( my_string[4] )

print("reverse indexing")
print( my_string[0] )
print( my_string[-4] )
print( my_string[-3] )
print( my_string[-2] )
print( my_string[-1] )


# Slicing of strings
# StringToBeSlice[ StartIndex: StopIndex(but not include it) : StepSize ]

slice_string = "ABCDEFGHIJKL"
print( slice_string[4:])
print( slice_string[:4])

print( slice_string[::])
print( slice_string[::1])
print( slice_string[::2])
print( slice_string[::3])
print( slice_string[::4])
print( slice_string[::-1])
print( slice_string[::-2])
print( slice_string[::-3])
print( slice_string[::-4])

#Slicing of a word without assigning it into a variable name
print( 'Terminal'[3:6] )

# Immutability - cannot be changed
# Strings does not support item replacement

print(my_string)
# Not possible , because string objects are immutable .
# my_string[0] = 'C'

#Desired output  - Cappy
desired_output = 'C' + my_string[1:]
print(desired_output)
print(my_string)

# Concatenation of strings
my_string = my_string + " Birthday"
print(my_string)

my_string = my_string + " Birthday"
print(my_string)

# String multiplication
my_article = "a"
print(my_article)
my_article = my_article * 5
print(my_article)

# Concatenation of a string and integer is not possible
# my_article_concatenation = my_article + 5
my_article_concatenation = my_article + '5'
print(my_article_concatenation)

sum = 5 + 5
print(sum)

concat = '5' + '5'
print(concat)

sample = "Hello Python"
print(sample.capitalize())
print(sample.casefold())
print(sample.upper())
print(sample.isupper())
print(sample.lower())
print(sample.islower())

# String Interpolation
print("Hello World " + sample)

# Format objects into the strings for the print statement
print( "This is a simple sentence. {}". format( ' Lets add another sentence here'))
print( "This is a simple sentence. {} {} {} {} ". format( 'one' , 'two' , 'three' , 'four' ))
print( "This is a simple sentence. {0} {1} {2} ". format( 'IndexZero', 'IndexOne' , 'IndexTwo'  ))
print( "This is a simple sentence. {2} {1} {0} ". format( 'IndexZero', 'IndexOne' , 'IndexTwo'  ))
print( "This is a simple sentence. {z} {o} {t} ". format( z = 'IndexZero', o = 'IndexOne' , t = 'IndexTwo'  ))
print( "This is a simple sentence. {t} {o} {z} ". format( z = 'IndexZero', o = 'IndexOne' , t = 'IndexTwo'  ))
print( "This is a simple sentence. {z} {z} {o} ". format( z = 'IndexZero', o = 'IndexOne' , t = 'IndexTwo'  ))

# Float formatting {value:width.precision f}

my_scores = 2000 / 2300
print(my_scores)

print(" My scores was {sc} ". format(sc = my_scores))
print(" My scores was {sc:1.4f} ". format(sc = my_scores))
print(" My scores was {sc:2.3f} ". format(sc = my_scores))

print( f"This is my final result { my_scores }")

print('I Like %s' %'apples')
print("I Like {lk}".format( lk = 'apples'))