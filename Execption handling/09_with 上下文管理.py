"""
with context_expr[as var]：
    语句块

with 上下文管理可以自动管理资源，在 with 代码块执行完
毕后自动还原进入该代码之前的 现场或上下文。不论何种原因
跳出 with 块，不论是否有异常，总能保证资源正常释放。极
大的简化了工作，在文件操作、网络通信相关的场合非常常用。
"""
with open("d:/bb.txt") as f:
    for line in f:
        print(line)
