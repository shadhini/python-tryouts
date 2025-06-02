"""
================================================================
Strings
================================================================

Strings are objects in Python.
These String objects have a bunch of capabilities.
So there are callable methods that belong to these string objects, which are specific to the object.

print() input() functions are general purpose functions, which don't belong to a particular object.


Immutable Strings
----------------------------------------------------------------
String Object methods doesn't change the original object;
Instead they return new objects as Strings are immutable in Python; i.e. they cannot be modified.
Thus calling a String method results in creating a new String object in memory.
Strings are immutable in many other programming languages as well.
"""

chapter = "Python Basics"

################
# UPPERCASE
################
print(chapter.upper())
print(chapter)
# this upper() method doesn't change our original string
# it returns a new string

################
# lowercase
################
print(chapter.lower())

################
# find
################
# Check whether a string contains a character or sequence of characters.
# If the string contains the character/character sequence, then returns the starting index of it.
# Otherwise, return -1.

print(chapter.find('y'))
# returns the index of the first occurrence of 'y' in the string
print(chapter.find('Y'))
# returns -1 as capital "Y" is not present in the string

################
# replace
################
print(chapter.replace('Basics', 'Love !!!'))
print(chapter.replace('basics', 'Craze !'))

#################
# `in` operator
#################
# Can be used to check whether a string contains a character or sequence of characters.
# If the string contains the character/character sequence, then returns True.
# Otherwise, returns False.

print("Python" in chapter)