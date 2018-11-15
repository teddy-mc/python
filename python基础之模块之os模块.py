import os

print('#----------os.name:显示当前使用的平台----------------#')
print(os.name)
print('\n')


print('#----------os.getcwd():显示当前python脚本工作路径----------------#')
print(os.getcwd())
print('\n')


print('#----------os.listdir("dirname")#返回指定目录下的所有文件和目录名----------------#')
print(os.listdir())
print('\n')


print('#----------os.makedir建立目录----------------#')
os.makedirs('hahaha/linghuchong')
print(os.listdir())
print('\n')

print('#----------os.rename重命名目录----------------#')
os.rename('hahaha/linghuchong','hahaha/linghuchong_new')
print(os.listdir())
print('\n')

print('#----------os.remove删除一个文件----------------#')
os.remove('a.txt')
print(os.listdir())