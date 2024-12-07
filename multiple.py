
d={}
a=20
b=0
try:
    d[{'a','b',9}]=89
    print(a/b)
    # d['a']=39
    print(d)
except TypeError:
    print("unhashable type set")
except ZeroDivisionError:
    print('zero divizon erro')