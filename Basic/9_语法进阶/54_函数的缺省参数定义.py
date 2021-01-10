def print_info(name, gender=True):
    """

    @param name: 班上的同学姓名
    @param gender: True 男生 False 女生
    @return:
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name, gender_text))


# 假设班上的同学，男生居多
# 提示：在指定缺省参数的默认值的时，应该用最常见的值作为默认值！

print_info("小明")
print_info("老王")
print_info("小妹", False)
