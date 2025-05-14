def tao_tuple_tu_list(lst):
    return tuple(lst)
il= input("nhap danh sach cac so, cach nhau bang day phay")
numbers = list(map(int,il.split(',')))
my_tp=tao_tuple_tu_list(numbers)
print("list: ",numbers)
print("tuple: ",my_tp)