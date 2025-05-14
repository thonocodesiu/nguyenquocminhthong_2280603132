def chiaHETCHO5(so):
    sothapphan=int(so,2)
    if sothapphan % 5 ==0:
        return True
    else:
        return False
chuoisonhiphan = input("nhap va chuoi so nhi phan(su dung dau phay): ")
danhsachsonhiphan = chuoisonhiphan.split(',')
soChiahetcho5 = [so for so in danhsachsonhiphan if chiaHETCHO5(so)]
if len(soChiahetcho5)>0:
    ket_qa=','.join(soChiahetcho5)
    print("cac so nhi phan chia het cho 5",ket_qa)
else:
    print("khong co so nao")