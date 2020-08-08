import pickle
a1 = "zxq"
a2 = 1231
a3 = [10, 120, 230]

with open("data.dat", "wb") as f:

    pickle.dump(a1, f)
    pickle.dump(a2, f)
    pickle.dump(a3, f)


with open("data.dat", "rb") as f:
    b1 = pickle.load(f)
    b2 = pickle.load(f)
    b3 = pickle.load(f)
    print(b1), print(b2), print(b3)

print(id(a1)), print(id(b1))
