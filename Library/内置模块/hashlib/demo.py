import hashlib

m = hashlib.sha256()
m.update('hello'.encode('utf-8'))
m.update('world'.encode('utf-8'))
res = m.hexdigest()
print(res)

m1 = hashlib.sha256()
m1.update('hell'.encode('utf-8'))
m1.update('o'.encode('utf-8'))
m1.update('wo'.encode('utf-8'))
m1.update('rld'.encode('utf-8'))
res1 = m1.hexdigest()
print(res1)



