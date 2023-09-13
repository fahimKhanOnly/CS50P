# String Methods


# join(iterable)
ls = ["Fahim", "Montasir", "Khan"]
sep = "-"
sep.join(ls) #  Fahim-Montasir-Khan
# Join sep as a Separator in the list



# lower()
"Fahim".lower() #  fahim
"FAHIM KHAN".lower() #  fahim khan



# lstrip([chars])
lStr = "    Fahim    "
"\'" + lStr.lstrip() + "\'" #  'Fahim    '
url = "https://www.example.com/path"
url.lstrip("https://") #  www.example.com/path



# partition(sep)
partStr = "My name is Fahim Khan."
partStr.partition("Fahim Khan") #  ('My name is ', 'Fahim Khan', '.') 
partStr.partition("fahim") #  ('My name is Fahim Khan.', '', '')




# removeprefix(prefix, /)
url.removeprefix("https://") #  www.example.com/path
url.removeprefix(" ") #  https://www.example.com/path




# removesuffix(suffix, /)
url.removesuffix("path") #  https://www.example.com/
url.removesuffix("/") #  https://www.example.com/path



# replace(old, new [, count])
"I am fahim. Is your name fahim?".replace("fahim", "Fahim") #  I am Fahim. Is your name Fahim?
"I am fahim. Is your name fahim?".replace("fahim", "Fahim", 1) #  I am Fahim. Is your name fahim?



# rfind(sub [, start [, end]])
"Fahim Khan".rfind("i") #  3
"Fahim".rfind("A") #  -1



# rindex(sub [, start [, end]])
txt = "My name is Fahim"
txt.rindex("i") #  14
txt.rindex(" ") #  10
# txt.rindex("S") #  ValueError



# rsplit(sep=None, maxsplit= -1)
txt1 = "Fahim Montasir Khan"
txt1.rsplit() #  ['Fahim', 'Montasir', 'Khan']




# rstrip([chars])
txt2 = "   Fahim Khan   "
f"'{txt2.rstrip()}'" #  '   Fahim Khan'




# split(sep=None, maxsplit= -1)
txt1.split() #  ['Fahim', 'Montasir', 'Khan']




# splitlines(keepends=False)
lines = """My name is Fahim.
I'm 18 years old.
"""
lines.splitlines() #  ['My name is Fahim.', "I'm 18 years old."]




# startswith(prefix [, start [, end]])
"Fahim Khan".startswith("a", 1) #  True
"Fahim Khan".startswith("f") #  False




# strip([chars])
f"\'{txt2.strip()}\'" #  'Fahim Khan'
'www.example.com'.strip('cmow.') #  'Fahim Khan'




# swapcase()
"fAHIM mONTASIR kHAN".swapcase() #  Fahim Montasir Khan




# title()
"fahim montasir khan".title() #  Fahim Montasir Khan




# upper()
"fahim khan".upper() #  FAHIM KHAN
"Fahim Montasir Khan".upper() #  FAHIM MONTASIR KHAN




# zfill(width)
print("Fahim".zfill(10)) #  00000Fahim
print("-35".zfill(5)) #  -0035
