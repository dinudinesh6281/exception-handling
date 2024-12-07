# n=20
# b=0
# try:
#     print(n/b)
# except:
#     print("can't divide by zero")

d={}
try:
    d[{'a','b',9}]=89
    d['a']=39
    print(d)
except:
    print("unhashable type set")