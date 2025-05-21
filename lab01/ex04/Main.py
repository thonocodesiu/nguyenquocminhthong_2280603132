from Qlysinhvien import Qlysinhvien
qlsv = Qlysinhvien()
while (1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("****************************************MENU***************************************")
    print("**  1. Them sinh vien.                                                           **")
    print("**  2. Cap nhat thong tin sinh vien boi ID.                                      **")
    print("**  3. Xoa sinh vien boi ID.                                                     **")
    print("**  4. Tim kiem sinh vien theo ten.                                              **")
    print("**  5. Sap xep sinh vien theo diem trung binh.                                   **")
    print("**  6. Sap xep sinh vien theo ten chuyen nganh.                                  **")
    print("**  7. Hien thi danh sach sinh vien.                                             **")
    print("**  0. Thoat                                                                     **")
    print("***********************************************************************************")
    key = int(input("Nhap lua chon: "))
    if (key == 1):
        qlsv.nhapSV()
    elif (key == 2):
        if (qlsv.soLuongSV() > 0):
            id = int(input("Nhap ID sinh vien: "))
            qlsv.updateSV(id)
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif (key == 3):
        if (qlsv.soLuongSV() > 0):
            id = int(input("Nhap ID sinh vien: "))
            if (qlsv.deleteByID(id)):
                print("Da xoa sinh vien co ID = ", id)
            else:
                print("Khong tim thay sinh vien co ID = ", id)
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif (key == 4):
        if (qlsv.soLuongSV() > 0):
            keyword = input("Nhap ten sinh vien: ")
            kq = qlsv.findbyName(keyword)
            qlsv.showSV(kq)
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif (key == 5):
        if (qlsv.soLuongSV() > 0):
            qlsv.sortByDiemTB()
            print("Da sap xep sinh vien theo diem trung binh")
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif (key == 6):
        if (qlsv.soLuongSV() > 0):
            qlsv.sortByName()
            print("Da sap xep sinh vien theo ten")
        else:
            print("Khong co sinh vien nao trong danh sach")
    elif (key == 7):
        if (qlsv.soLuongSV() > 0):
            qlsv.showSV(qlsv.getListSV())
        else:
            print("Khong co sinh vien nao trong danh sach")    
    elif (key == 0):
        break
    else:
        print("Lua chon khong hop le")