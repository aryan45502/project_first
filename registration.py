import os
import pickle
print(os.path.isfile("student.txt"))


if os.path.isfile("student.txt"):
    f=open("student.txt")
    print("file opened")
    f.close()
else:
    print("file not found")


f=open("student.txt",mode='w')
f.write("Hello")
f.close()


f=open("student.txt",mode='a')
lst=['ram\n','shyam\n','hari\n','gita\n']
f.writelines(lst)
f.close()
print("success")


f=open('student.txt',mode='r')
print(f.tell())
data=f.read(5)
print(data)
print(f.tell())
data1=f.read(3)
print(data1)
print(f.tell())




f=open("student.txt",mode='r')
data=f.read()
print(data)
f.close()
print("completed")


f1=open("student.txt",mode='r')
f2=open("student.txt",mode='w')
data=f1.read()
f2.write(data)
f1.close()
f2.close()


#opening file using with statement
"""with open ("<file>","<mode>") as <var>:"""


with open ('student.txt') as f:
    data=f.read()
    print(data)
print(f.closed)

f = open("student.txt","rb")
d = pickle.load(f)
print(d)
f.close()


