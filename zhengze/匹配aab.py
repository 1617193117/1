Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> y = 'aabaaabaaaab'
>>> import re
>>> re.findall('(?:aab){3}', y)
[]
>>> re.findall('\w', y)
['a', 'a', 'b', 'a', 'a', 'a', 'b', 'a', 'a', 'a', 'a', 'b']
>>> re.findall('\w+', y)
['aabaaabaaaab']
>>> re.findall('(?:a){3}(?:a){3}(?:b){3}', y)
[]
>>> re.findall('\w+(aab)', y)
['aab']
>>> re.findall('\w+(aab){3}', y)
[]
>>> re.findall('\w+(aab)\{3,}', y)
[]
>>> re.findall('\w+(aab){3,}', y)
[]
>>> re.findall('\w+(aab)', y)
['aab']
>>> re.findall('(aab)', y)
['aab', 'aab', 'aab']
>>> 
