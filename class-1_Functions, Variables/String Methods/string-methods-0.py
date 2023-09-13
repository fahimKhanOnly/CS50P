# String methods

text = "fAhIm kHaN"
info = "My name is Fahim Montasir Khan, I'm 18 Years old."

# capitalize()
text.capitalize() #  "Fahim khan"


# casefold()
text.casefold() #  "fahim khan"



# center(length [, character])
f"\'{text.center(12)}\'" #  '--fAhIm kHaN--'
# solved same problem more Efficiently
f"\'{text.center(len(text) + 2)}\'" #  '--fAhIm kHaN--'
f"\'{text.center(len(text) + 4, '-')}\'" #  '--fAhIm kHaN--'




# count(sub [, start [, end]])
info.count("a") #  5
info.count("a", 20) #  3
info.count("a", 20, -8) #  2




# endswith(suffix [, start [, end]])
info.endswith(".") #  True
info.endswith(" old", 10, -1) #  True
info.endswith("My", 0, -1) #  False

# solved same problem more efficiently
split = info.split()[-1][:-1]
split.endswith("old", -len(split)) #  True




# expandtabs(tabsize=8)
text1 = "\'\tHello\tWorld\t!\t\'"
text1.expandtabs(11) #  '          Hello      World      !          '




# find(sub [, start [, end]])
info.find("fahim") #  -1
info.find(".", len(info) - 1, len(info)) #  48

# Note: The find() method should be used only if you need to know the position of sub. To check if sub is a substring of not, use the in operator:
"Fahim" in info # True




# index(sub [, start [, end]])
# Like find(), but it is raise ValueError when the substring is not found
info.index(".", len(info) - 1, len(info)) #  48




# isalnum()
# Example of character that are not alphanumeric: (space)!#%&? etc.
text2 = "Fahim768"
text2.isalnum() #  True




# isalpha()
# Note: Example of characters that are nto alphabet letters: (space)!#%&? etc.
text3 = "Fahim"
text3.isalpha() #  True
text.isalpha() #  False




# isdecimal()
text4 = "352"
text4.isdecimal() #  True
# The method can also be used on unicode objects
"\u0030".isdecimal() #  True
# "\u0030" This is unicode for '0'
"\u0048".isdecimal() #  False
# "u0048" This is unicode for 'H'




# isdigit()
text4.isdigit() # True
"#!".isdigit() #  False
# This method also be used on unicode objects
"\u0030".isdigit() #  True
# "\u0030" unicode for '0'
"\u0042".isdigit() #  False
# "\u00B2" unicode for '²'




# islower()
"fahim khan".islower() #  True
"Fahim Khan".islower() #  False




# isnumeric()
# This method also be used on unicode objects
"35635".isnumeric() #  True
"fahim34".isnumeric() #  False




# isspace()
"    ".isspace() #  True
"".isspace() #  False




# istitle()
text.istitle() #  False
"Fahim Montasir Khan".istitle() #  True




# isupper()
"Fahim Khan".isupper() #  False
"FAHIM KHAN".isupper() #  True
