dict = {
    "SV001" : 3.2,
    "SV002" : 3.3,
    "SV003" : 3.4,
    "SV004" : 2.9,
    "SV005" : 1.8,
    "SV006" : 1.2
}

dem = sum(1 for score in dict.values() if 3.0 <= score <= 3.5)
dict["SV007"] = 3.8

dict = {id: score for id, score in dict.items() if score >=2.0}
print(f"Từ điển có số sinh viên có điểm tổng kết trong đoạn [3.0, 3.5] là: {dem}")
print(f"Từ điển sau khi cập nhật là: ")
for id, score in dict.items():
    print(f"Mã sinh viên: {id}, điểm tổng kết là: {score:.2f}")