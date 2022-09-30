#Text Data

myStr = "Hello World"
myStr1 = "Dog"

#print(dir(myStr))

print(myStr.upper())

print(myStr.lower())

print(myStr.swapcase())

print(myStr.capitalize())

print(myStr.replace("hello", "bye").upper())

print(myStr.count("l"))

print(myStr.startswith("hola"))

print(myStr.endswith("world"))

print(myStr.split())

print(myStr.find("h"))

print(len(myStr))

print(myStr.index("e"))

print(myStr.isnumeric())

print(myStr.isalpha())

print(myStr[4])

print("my name is " + myStr1)

print(f"My nane is {myStr1}")

print("my name is {0}".format(myStr1))

a = """Lorem ipsum dolor sit amet,
Lorem ipsum dolor sit amet,
Lorem ipsum dolor sit amet
Lorem ipsum dolor sit amet"""
print(a)

a = '''asddfadsfadfs
asdfasdf
sadfasdf
asdasf'''
print(a)

#String are Arrays
a = "Hello, World!"
print(a[1])

#Looping Through a String

for x in "banana":
    print(x)

#String Length

a = "Hello World!"
print(len(a))

#Check String
txt = "The best thing in life are free!"
print("free" in txt)

#if statement:
txt = "The best things in life are free!"
if "free" in txt:
    print("yes, 'free' is present")

#Check if NOT
txt = "The best thing in life are free!"
print("expensive" not in txt)

#if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is Not present.")

#Slicing
b = "Hello World!"
print(b[2:8])

#Slice from the start
b = "Hello, World!"
print(b[:5])

#Slice To the End
b = "Hello, World!"
print(b[2:])

#Negative Indexing
b ="Hello, World!"
print(b[-5:-2])

#Remove Whitespace
a = " Hello, World!"
print(a.strip())

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#String Format
#We cannot combine strings and numbers like this.
#age = 36
#txt = "My name is John, I am " + age
#print(txt)

#But we can combine strings and numbers by using the format() method!
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Example two
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces or item {} for {} dollars."
print(myorder.format(quantity,itemno,price))

#Example three
quantity = 3
itemno = 567
prince = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, prince))

#Escape Characters

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value

#String Methods
#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#center()	Returns a centered string
#count()	Returns the number of times a specified value occurs in a string
#encode()	Returns an encoded version of the string
#endswith()	Returns true if the string ends with the specified value
#expandtabs()	Sets the tab size of the string
#find()	Searches the string for a specified value and returns the position of where it was found
#format()	Formats specified values in a string
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
#isalnum()	Returns True if all characters in the string are alphanumeric
#isalpha()	Returns True if all characters in the string are in the alphabet
#isdecimal()	Returns True if all characters in the ##tring are decimals
###sdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an id##ntifier
###slower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all ch##racters in the string are numeric
###sprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces          ##
###stitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the stri##g are upper case
###oin()	Joins the elements of an iterable to the end of the string
#ljust()	Returns a left justified version of the string                       ##
###ower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string       ##
###aketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts            ##
###eplace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and ##eturns the last position of where it was found
###index()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string   ##
###partition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list            ##
###strip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list   ##
###plitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value        ##
###trip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa        ##
###itle()	Converts the first character of each word to upper case
#translate()	Returns a translated string                              ##
###pper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 valu##s at the beginning
 ##
                                                                                 ##
"""
Metodos de cadena 

capitalize() Convierte el primer carácter en superior

case casefold() Convierte una cadena en minúsculas#

center() Devuelve una cadena centrada

count() Devuelve el número de veces que aparece un valor específico en una cadena

encode() Devuelve una versión codificada de la cadena

termina con () Devuelve verdadero si la cadena termina con el valor especificado

expandtabs() Establece el tamaño de tabulación de la cadena

find() Busca en la cadena un valor específico y devuelve la posición donde se encontró

format() Formatea los valores especificados en una cadena

format_map() Formatea los valores especificados en una cadena

index() Busca en la cadena un valor específico y devuelve la posición donde se encontró

isalnum() Devuelve True si todos los caracteres de la cadena son alfanuméricos

isalpha() Devuelve True si todos los caracteres de la cadena están en el alfabeto

isdecimal() Devuelve True si todos los caracteres de la cadena son decimales

isdigit() Devuelve True si todos los caracteres de la cadena son dígitos

isidentifier() Devuelve True si la cadena es un identificador

islower() Devuelve True si todos los caracteres de la cadena están en minúsculas
"""

