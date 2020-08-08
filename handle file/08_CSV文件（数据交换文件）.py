import csv


with open("123.csv", "r") as f:
    a_csv = csv.reader(f)

    for row in a_csv:
        print(row)


with open("123.csv", "w") as f:
    b_csv = csv.writer(f)
    b_csv.writerow(["ID", "姓名", "年龄"])
    b_csv.writerow(["10001", "zxq", "12"])

    c = [["10002", "123", "23"]]
    b_csv.writerows(c)

