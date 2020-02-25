import re

# compile an expression (the book way and thus our way)
# or JUST use the expression  (e.g., re.search(pattern, string))

msg = '''
My name is Paul York. Please contact me by email at 
paul.york@augusta.edu at your earliest convenience or 
twitter @ @ptyork or @@ tattoine or paul@yorkie. I 
collect corks. And I work. Mork from ork.
'''

patt = re.compile('\w?ork')   # 0 or 1 letter followed by "ork"
mat = patt.search(msg)
print(mat)
mat = patt.search(msg,21)
print(mat)
matches = patt.findall(msg)
print(matches)

for mat in patt.finditer(msg):
    print(mat)

phones = '''
7065551212
706-555-1313
706 555 1414
706.555.1515
(706) 555-1616
(706)555-1717
Bob-The-Best
706555667788
12345
'''

patt = re.compile('706')
print(patt.findall(phones))

'''
REGULAR EXPRESSION SYNTAX "RULES"
 - Custom character
   [abc] finds a or b or c
   [Yy] finds Y or y
   [0-6] finds 0,1,2,3,4,5 or 6
   [A-F] finds A,B,C,D,E,F
   [0-9A-Fa-f] finds a hex digit
 - Special characters
   \d  == numeric digit >> [0-9]
   \w  == "word" character >> [A-Za-z0-9]
   \s  == "space" character
   \S  == all but "space" character
   b{3} find exactly 3 b's ("bbb")
   x{6} find exactly 6 x's ("xxxxxx")
   v{2,5} finds 2, 3, 4 or 5 v's  ("vv", "vvv", "vvvv", "vvvvv")
   x{,6} find up to 6 x's
   x{6,} find at least 6 x's
   x? - find 0 or 1 x ==> {,1}
   x* - find 0 or many x's 
   x+ - find 1 or many x's ==> {1,}
'''

# pwnd_patt = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# pwnd_patt = re.compile(r'\d\d\d[- .]\d\d\d[- .]\d\d\d\d')
# pwnd_patt = re.compile(r'\d{3}[- .]\d{3}[- .]\d{4}')
pwnd_patt = re.compile(r'\d{3}[- .]?\d{3}[- .]?\d{4}')
print(pwnd_patt.findall(phones))

