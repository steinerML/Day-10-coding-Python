
# Random exercises with Built-In functions
a = "   Hola            "
b = "           one  "
#print a (as is)
print(a)
#print b (as is)
print(b)
#print a (without whitespaces and blank gaps)
print(a.strip())
#print b (without whitespaces and blank gaps)
print(b.strip())
#length
#print length a string
print(len(a))
#print length b string
print(len(b))
#replace ('old', 'new') (full words)
c = 'Hola'
c.replace('ola','ello')
print(c.replace('Hola','Hello World!'))

#replace just letters /characters
d = 'Email'
d.replace('a', '@')
print(d.replace('a', '@'))
type(d)
print(type(d)) #what kind of data type is this? It's a string!

#Methods for Python strings
#upper (uppercase)
e = "prInsEngracht aMstErdAM"
e.upper()
print(e.upper())

#lower (lowercase)
f = "SCHIPHOL BUSINESS PARK"
f.lower()
print(f.lower())

#split (Splits the string into a list and specifies the separator in between)
g = "Amsterdam Schiphol World Trade Center"
g.split(',')
print(g.split())

#replace
#Replaces a given string with another string
h =  "Hello, World!"
h.replace("World!","Universe!")
print(h.replace("World!","Universe!"))

#another way of doing the same
i = "I like tendies, tendies and only tendies"
x = i.replace('tendies', 'hamburgers')
print(x)

#replace a given amount of times (by default is ALL)
i = "I like tendies, tendies. Whenever I see tendies I go for tendies"
x = i.replace('tendies', 'guacamole', 2)
print(x)