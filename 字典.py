Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict = {'abc': 456}
>>> dict1 = {'abc': 456}
>>> dict1
{'abc': 456}
>>> dick1['abc']

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    dick1['abc']
NameError: name 'dick1' is not defined
>>> dict1['abc']=852
>>> dictt['abc']

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dictt['abc']
NameError: name 'dictt' is not defined
>>> dict1['abc']
852
>>> del dict1['abc']
>>> users = {
	'A':{
	'first':'yu',
	'last':'lei',
	'location':'hs',
	},
}
>>> for usersname, usersinfo in users.items():
	print("userid: " + usersname)
	print("userinfo:" + str(usersinfo))

	
userid: A
userinfo:{'last': 'lei', 'location': 'hs', 'first': 'yu'}
>>> dict = {'Name':'Zara','Age': 7}
>>> print "Value : %s" % dict.keys()
Value : ['Age', 'Name']
>>> print "Key : %s" % dict.keys()
Key : ['Age', 'Name']
>>> for key in dict.keys():
	print key

	
Age
Name
>>> for key in dict.keys():
	print dict[key]

	
7
Zara
>>> dict = {'Name':'Robert','Number': 12}
>>> print "Value : %s" % dict.keys()
Value : ['Name', 'Number']
>>> 
>>> print "Key : %s" % dict.keys()
Key : ['Name', 'Number']
>>> for key in dict.keys():
	print key

	
Name
Number
>>> for key in dict.keys():
	print dict[key]

Robert
12

>>> 
