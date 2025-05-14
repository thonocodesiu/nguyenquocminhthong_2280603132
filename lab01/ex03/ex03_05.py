def demsolanxuathien(lst):
    dem={}
    for item in lst:
        if item in dem:
            dem[item]+=1
        else:
            dem[item]=1
    return dem
istr=input("nhap danh sach cac tu, cach nhau bang dau space: ")
wlist=istr.split()
solanxuathien=demsolanxuathien(wlist)
print("so lan xuat hien: ",solanxuathien)
        