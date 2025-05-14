sogiolam = float(input("nhap vao so gio lam: "))
luongio = float(input("nhap vao luong theo gio: "))
giotieuchuan = 28
giovuotchan = max(0,sogiolam-giotieuchuan)
thuclinh= giotieuchuan*luongio+giovuotchan*luongio*1.5
print(f"so tien thuc linh: {thuclinh}")
