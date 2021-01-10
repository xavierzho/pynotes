import importlib

s = "math"
m = __import__(s)
c = m.pi
b = m.sin(3)
print(c)

a = importlib.import_module(s)

print(a.pi)
