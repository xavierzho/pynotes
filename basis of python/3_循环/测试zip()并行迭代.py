for i in [1, 2, 3]:
    print(i)

names = ("钟锡权1", "zxq", "weqwe", "1231")
ages = ("12", "13", "14", "15")
jobs = ("teacher", "progamer", "hoster")

for name, age, job in zip(names, ages, jobs):
    print("{0}--{1}--{2}".format(name, age, job))



