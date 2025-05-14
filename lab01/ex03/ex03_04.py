def truycapphantu(tuple_data):
    dautien= tuple_data[0]
    cuoicung= tuple_data[-1]
    return dautien,cuoicung
ip = eval(input("nhap tuple,vd 1, 2,3: "))
dau,cuoi=truycapphantu(ip)
print("dau tien: ",dau)
print("cuoi cung: ",cuoi)