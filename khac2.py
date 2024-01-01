ho_ten = ["An", "Binh", "Lan", "Hoa", "Thang"]
diem = [7.5, 8.8, 7.0, 9.5, 8.5]

def tao_thong_tin_sv(ho_ten,diem):
    diem_sv = dict(zip(ho_ten, diem))
    return diem_sv
print(tao_thong_tin_sv(ho_ten,diem))

def top_2_sv(ho_ten, diem):
    if len(ho_ten) < 2 or len(diem) < 2:
        return "Không đủ dữ liệu để tìm top 2 sinh viên."
        
    thong_tin_sv = list(zip(ho_ten, diem))
    thong_tin_sv.sort(key=lambda x: x[1], reverse=True)
    top_2 = thong_tin_sv[:2]

    return top_2
    
ket_qua = top_2_sv(ho_ten, diem)
print("Thông tin top 2 sinh viên:")
for sv in ket_qua:
    print(f"{sv[0]} - {sv[1]}")
