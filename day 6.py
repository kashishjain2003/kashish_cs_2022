Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=print('HI')
HI
a
print(a)
None
def myfun():
    print('this is my first function')
myfun()
SyntaxError: invalid syntax
myfun()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    myfun()
NameError: name 'myfun' is not defined
def myfun():
    print('this is my first function')

    
myfun()
this is my first function
a=myfun()
this is my first function
def second():
    return 'hghgf'

second()
'hghgf'
b=second()
second()
'hghgf'
print(b)
hghgf
def third(x):
    print('hello')

    
third(x)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    third(x)
NameError: name 'x' is not defined
third()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    third()
TypeError: third() missing 1 required positional argument: 'x'
print(x)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
third('dsf')
hello
def fourth(x):
    return x*10

fourth(10)
100
def fourth(x):
    print('hi')
    print('hello')
    print('rgbnmg')
    return x*10

fourth(4)
hi
hello
rgbnmg
40
40
40
def five(x,y,z):
    return x+y+z

five(3,4,5)
12
12
12
def six(x,y,z):
    return x+y+z

six(7,6,8)
21
def seven(x,y,z=1):
    return x+y+z
seven()
SyntaxError: invalid syntax

seven(4,6,7)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    seven(4,6,7)
NameError: name 'seven' is not defined
seven(2,4,5)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    seven(2,4,5)
NameError: name 'seven' is not defined
def seven(x,y,z=1):
    return x+y+z

seven(2,3,4)
9
def eight(*x)
SyntaxError: expected ':'
def eight(*x):
    return(x)

eight(2,34,45)
(2, 34, 45)
(2, 34, 45)
(2, 34, 45)
def nine(**xx)
SyntaxError: expected ':'
def nine(**xx):
    return x

nine(3,4,5,6)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    nine(3,4,5,6)
TypeError: nine() takes 0 positional arguments but 4 were given
nine('name':'fgfg', 'sem':2)
SyntaxError: invalid syntax
nine(name='fgfg', sem=2)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    nine(name='fgfg', sem=2)
  File "<pyshell#63>", line 2, in nine
    return x
NameError: name 'x' is not defined. Did you mean: 'xx'?
def nine(**xx):
    return x

nine(name='fgfg', sem='second')
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    nine(name='fgfg', sem='second')
  File "<pyshell#68>", line 2, in nine
    return x
NameError: name 'x' is not defined. Did you mean: 'xx'?
def nine(**x):
    return x

nine(name='fgfg', sem='second')
{'name': 'fgfg', 'sem': 'second'}
{'name': 'fgfg', 'sem': 'second'}
{'name': 'fgfg', 'sem': 'second'}
def ten(*'kashish'):
    
SyntaxError: invalid syntax
def ten(*x):
    x='kashish'
    return x

ten(3)
'kashish'

def ten(*x):
    x='kashish'
    return *x
SyntaxError: can't use starred expression here

def ten(*x):
    x='kashish'
    return x

ten(*x)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    ten(*x)
NameError: name 'x' is not defined
def ten(*x):
    
    return x

ten('happy birthday')
('happy birthday',)
def ten(x):
    return x

ten('happy birthday')
'happy birthday'
def ten(x):
    return 'happy birthaday'

ten('kj')
'happy birthaday'
'happy birthaday'
'happy birthaday'
'happy birthaday'
'happy birthaday'
def birthday(name):
    print('Happy Birthday to you')
    print('Happy Birthday to you')
    print(f'happy birthday dear {name}')
    print('happy birthday')

    
birthday(gungun)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    birthday(gungun)
NameError: name 'gungun' is not defined
birthday ('gungun')
Happy Birthday to you
Happy Birthday to you
happy birthday dear gungun
happy birthday




 def seven(x,y,z): return x+y+z
 
SyntaxError: unexpected indent
myadd=lambda x,y,z: x+y+z
myadd(5,6,7)
18
import datetime as dt
aaj_ki_date=dt.date.today()
print(aaj_ki_date)
2022-09-19
2022-09-19import calendar
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
import calendar
print(calendar.calendar(2022))
                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

