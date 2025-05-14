from Sinhvien import Sinhvien
class Qlysinhvien:
    listSV = []
    def taoID(self):
        maxID = 1
        if (self.soLuongSV()>0):
            maxID = self.listSV[0].id
            for sv in self.listSV:
                if (sv.id > maxID):
                    maxID = sv.id   
            maxID += 1
        return maxID
    def soLuongSV(self):
        return self.listSV.__len__()
    def nhapSV(self):
        id = self.taoID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh: ") 
        major = input("Nhap nganh: ")
        diemTB = float(input("Nhap diem trung binh: "))
        sv = Sinhvien(id,name,sex,major,diemTB)
        self.xepHocluc(sv)
        self.listSV.append(sv)
    def updateSV(self,id):
        sv:Sinhvien = self.findbyID(id)
        if (sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh: ")
            major = input("Nhap nganh: ")
            diemTB = float(input("Nhap diem trung binh: "))
            sv.name = name
            sv.sex = sex
            sv.major = major
            sv.diemTB = diemTB
            self.xepHocluc(sv)
        else:   
            print("Khong tim thay sinh vien")
    def sortByID(self):
        self.listSV.sort(key=lambda x: x.id, reverse=False) 
    def sortByName(self):
        self.listSV.sort(key=lambda x: x.name, reverse=False)
    def sortByDiemTB(self):
        self.listSV.sort(key=lambda x: x.diemTB, reverse=False)
    def findbyID(self,id):
        serchResult = None
        if(self.soLuongSV() > 0):
            for sv in self.listSV:
                if (sv.id == id):
                    serchResult = sv
        return serchResult
    def findbyName(self,keyword):
        listSV= []
        if(self.soLuongSV() > 0):
            for sv in self.listSV:
                if(keyword.upper() in sv.name.upper()):
                    listSV.append(sv)
        return listSV
    def deleteByID(self,id):
        isDelete = False
        sv = self.findbyID(id)
        if (sv != None):
            self.listSV.remove(sv)
            isDelete = True
        return isDelete
    def xepHocluc(self,sv):
        if (sv.diemTB >= 8):
            sv.hocluc = "Gioi"
        elif (sv.diemTB >= 6.5):
            sv.hocluc = "Kha"
        elif (sv.diemTB >= 5):
            sv.hocluc = "Trung binh"
        else:
            sv.hocluc = "Yeu"
    def showSV(self,listSvien):
        print("{:8} {:18} {:8} {:8} {:8} {:8}".format("ID","Name","Sex","Major","DiemTB","Hocluc"))
        if (listSvien.__len__() > 0):
            for sv in listSvien:
                print("{:8} {:18} {:8} {:8} {:8} {:8}".format(sv.id,sv.name,sv.sex,sv.major,sv.diemTB,sv.hocluc))
        print("\n")
    def getListSV(self):
        return self.listSV