Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> A = 20
>>> print(type(A))
<class 'int'>
>>> print(type(str(A)))
<class 'str'>
>>> int("42")
42
>>> print(type(A))
<class 'int'>
>>> print(type(str(A)))
<class 'str'>
>>> S = 4.8
>>> type(S)
<class 'float'>
>>> print(type(str(S)))
<class 'str'>
>>> print(type(int(A)))
<class 'int'>
>>>  easy_as = [1,2,3]
SyntaxError: unexpected indent
>>> easy_as = [1,2,3]
>>> print(easy_as)
[1, 2, 3]
>>> empty_list = []
>>> letters = ['A','B','C','D','E']
>>> numbers = [1,2,3,4,5]
>>> empty_list
[]
>>> letters
['A', 'B', 'C', 'D', 'E']
>>> numbers
[1, 2, 3, 4, 5]
>>> mixed_list = [1,3,"ABCDEF",6,"QWERTY",7,8,9]
>>> mixed_list
[1, 3, 'ABCDEF', 6, 'QWERTY', 7, 8, 9]
>>> numbers.append(6,7,8,9)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    numbers.append(6,7,8,9)
TypeError: append() takes exactly one argument (4 given)
>>> numbers.append[6,7,8,9]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    numbers.append[6,7,8,9]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> numbers.append(9)
>>> numbers
[1, 2, 3, 4, 5, 9]
>>> numbers[4]
5
>>> numbers[1:4]
[2, 3, 4]
>>> letters[:4]
['A', 'B', 'C', 'D']
>>> c = [letters,numbers]
>>> c
[['A', 'B', 'C', 'D', 'E'], [1, 2, 3, 4, 5, 9]]
>>> c[0]
['A', 'B', 'C', 'D', 'E']
>>> c[1]
[1, 2, 3, 4, 5, 9]
>>> c[0][1]
'B'
>>> 
