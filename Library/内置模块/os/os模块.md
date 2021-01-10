### os 模块

#### 常用命令

##### 删除指定的文件

```python
os.remove(path)        
```

##### 重命名/移动文件或目录

```python
os.rename(src,dest)    
```

##### 返回文件的所有属性

```python
os.stat(path)       
```

##### 返回 path目录下的文件和目录 的列表

```python
os.listdir(path)
```

### os 模块下关于目录操作的相关方法

##### 创建目录

```python
os.mkdir(path)       
```



##### 创建多级目录  

```python
os.makedirs(path1/path2/path3/...)     
```

##### 删除目录

```python'
os.rmdir(abspath)    
```

​                     

##### 删除多级目录

```python
os.removedirs(path1/path2...)    
```

​      

##### 返回当前工作目录

```python
os.getcwd()      
```

​                      



##### 把path设为当前工作目录

```
os.chdir(path)     
```


​                    



                 

##### 遍历目录树

```
os.walk()             
```

​                              

##### 当前操作系统所使用的路径分隔符

```
os.sep   
```

​                     

##### 获取当前系统登录的用户名称

```
os.getlogin()     
```

​                   

##### 获得n个字节长度的随机字符串，通常用于加密运算

```python
os.urandom(n)        
```

​                   

##### 获取系统下的环境变量

```
os.get_exec_path()      
```

​                



#### os.path模块提供了目录相关（路径判断、路径切分、路径连接、文件夹遍历）的操作

##### 判断 path是否绝对路径

```
os.path.isabs(path) 
```

#####  判断 path是否为目录     

```
os.path.isdir(path) 
```

#####   判断 path是否为文件       

```
os.path.isfile(path)   
```



#####  判断指定路径的文件是否存在   

```
os.path.exists(path)  
```



##### 返回文件的大小     

```
os.path.getsize(filename) 
```



##### 返回绝对路径  

```
os.path.abspath(path) 
```



##### 返回目录的路径      

```
os.path.dirname(p) 
```



##### 返回文件的最后访问时间         

```
os.path.getatime(filename)  
```



#####  返回文件的最后修改时间

```
os.path.getmtime(filename) 
```



#####  递归方式遍历目录

```
os.path.walk(top,func,arg) 
```



##### 连接多个 path

```
os.path.join(path,*paths)   
```



##### 对路径进行分割，以列表形式返回    

```
os.path.split(path)   
```



##### 从路径中分割文件的扩展名  

```
os.path.splitext(path)      
```

