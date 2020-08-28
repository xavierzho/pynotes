import re

string = "Python is the best language in the world"

res = re.match('P', string)

print(res.group())

