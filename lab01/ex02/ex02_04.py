j=[]
for so in range(2000,3201):
    if (so % 7==0) and (so % 5 !=0):
        j.append(str(so))
print(",".join(j))
        