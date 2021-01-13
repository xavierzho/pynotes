import os

for parent, _, filenames in os.walk('D:/ProxyPool/'):
    for fn in filenames:
        if fn.endswith('.py'):
            fp = os.path.join(parent, fn)
            with open(fp, encoding='utf-8', mode='r') as f:
                f_list = f.readlines()
                try:
                    second = f_list.index('"""\n', 2)
                except ValueError:
                    continue
                else:
                    with open(fp, encoding='utf-8', mode='w') as f2:
                        f2.writelines(f_list[second + 2:])
