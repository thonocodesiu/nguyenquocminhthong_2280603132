def xoaphantu(diction,key):
    if key in diction:
        del diction[key]
        return True
    else:
        return False
my_dic={'a':1,'b':2,'c':3,'d':4}
keydelete='b'
kq=xoaphantu(my_dic,keydelete)
if kq:
    print("phan tu da duoc xoa: ",my_dic)
else:
    print("khong tim thay")