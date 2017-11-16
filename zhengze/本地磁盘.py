Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> y = 'tel:010-12345678 address:changanRoad'
>>> import re
>>> re.findall('\d', y)
['0', '1', '0', '1', '2', '3', '4', '5', '6', '7', '8']
>>> re.findall('\d+', y)
['010', '12345678']
>>> re.findall('\d+-', y)
['010-']
>>> re.findall('\d+-\d+', y)
['010-12345678']
>>> y = 'localpath C:\code\cnkiCrawl'
>>> import re
>>> re.findall('\w+', y)
['localpath', 'C', 'code', 'cnkiCrawl']
>>> re.findall('\w', y)
['l', 'o', 'c', 'a', 'l', 'p', 'a', 't', 'h', 'C', 'c', 'o', 'd', 'e', 'c', 'n', 'k', 'i', 'C', 'r', 'a', 'w', 'l']
>>> re.findall('\w+-', y)
[]
>>> re.findall('\w:', y)
['C:']
>>> re.findall('\w:\code', y)
[]
>>> re.findall('\w:\w+', y)
[]
>>> re.findall('\w:\w+code', y)
[]
>>> 
