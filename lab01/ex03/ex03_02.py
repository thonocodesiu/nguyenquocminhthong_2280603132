def daonguoc(lst):
    return lst[::-1]
lst = input("nhap danh sach cac so cach nhay bang dau phay: ")
numbers = list(map(int, lst.split(',')))
listdaonguoc=daonguoc(numbers)
print("danh sach: ",listdaonguoc)
