Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:01:55) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> x="hello"  #str
>>> print(x)
hello
>>> x=20     #int
>>> print(x)
20
>>> x=20.5   #float
>>> print(x)
20.5
>>> x=1j   #complex
>>> print(x)
1j
>>> x=["apple","banana","cherry"]   #list
>>> print(x)
['apple', 'banana', 'cherry']
>>> x=("apple","banana","cherry")#typle
>>> print(x)
('apple', 'banana', 'cherry')
>>> x=range (6)      #range
>>> print(x)
range(0, 6)
>>> x={"name":"disha","age":22}     #dict
>>> print(x)
{'name': 'disha', 'age': 22}
>>> x={"apple","banana","cherry"}        #set
>>> print(x)
{'cherry', 'banana', 'apple'}
>>> x=frozenset(["apple","banana","cherry"])  #frozenset
>>> print(x)
frozenset({'cherry', 'banana', 'apple'})
>>> x=True  #bool
>>> print(x)
True
>>> x=b"hello"   #bytes
>>> print(x)
b'hello'
>>> x=bytearray (5)   #bytearray
>>> print(x)
bytearray(b'\x00\x00\x00\x00\x00')
x=memoryview(bytes(5))    #memoryview
SyntaxError: invalid syntax
>>> x=memoryview(bytes(5))   #memoryview
>>> x=None #None type
>>> print(x)
None
>>> 