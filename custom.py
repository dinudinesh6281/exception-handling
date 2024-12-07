class salerror(Exception):
    pass
# sal=int(input("enter your salary per month:"))
# name=input("enter your name:")
# sal=3000
# name='sanji'
# try:
#     if sal>=25000:
#         print('eligible to marry')
#     else:
#         raise salerror
# except salerror:
#     print(f'{name} your not eligible to marry')

sal=3000
name='sanji'
try:
    if sal>=25000:
        print('eligible to marry')
    else:
        raise Exception
except Exception:
    print(f'{name} your not eligible to marry')