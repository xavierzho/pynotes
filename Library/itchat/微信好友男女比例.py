import itchat

# 登录微信
ifchat.auto_Login(hotReload=True)
# 获取好友信息
friends = itchat.get_friends(update=True)

# print(friends)
#微信1 男 2女
total = 0
man = 0
women = 0
other = 0

for i in friends:
    sex = i['Sex']
    if sex == 1:
        man +=1
    elif sex ==2:
        women +=1
    else :
        other +=1
    total +=1
print('总人数为：%d人'%total)
print('男有：%d人'%(man,str(round(man/total*100,2))+'%'))
print('女有：%d人'%(women,str(round(women/total*100,2))+'%'))
print('男有：%d人'%(other,str(round(mother/total*100,2))+'%'))