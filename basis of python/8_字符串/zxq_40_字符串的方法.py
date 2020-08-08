str1 = "hello hello python"

# 1.统计字符串长度
print(len(str1))

# 2.统计一个小字符串出现的次数
print(str1.count('llo'))
print(str1.count('abs'))

# 3.某子子字符串出现的位置
str3 = str1.index("lo")
# 如果是用 index 方法传递的子字符串不存在，程序会报错valueError！
# str3 = str1.index("avs")
print(str3)

"""
capitalize()   find()         isdigit()      isupper()      replace()      split()        upper()
casefold()     format()       isidentifier() join()         rfind()        splitlines()   zfill()
center()       format_map()   islower()      ljust()        rindex()       startswith()
count()        index()        isnumeric()    lower()        rjust()        strip()
encode()       isalnum()      isprintable()  lstrip()       rpartition()   swapcase()
endswith()     isalpha()      isspace()      maketrans()    rsplit()       title()
expandtabs()   isdecimal()    istitle()      partition()    rstrip()       translate()
"""