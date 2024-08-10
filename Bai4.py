dict = {
    "n" : 1500,
    "m" : 2,
    "CLUSTERS" : 3,
    "ITER" : 10000,
    "METHOD" : "FCM",
    "MEASURE" : "EUCLIDEAN",
    "YEARS" : 51
}
print(f"Nội dung từ điển là: {dict}")

dict["MEASURE"] = "MANHATAN"
print(f"Nội dung từ điển sau khi sửa là: {dict}")

method_values = dict.get("METHOD", "Thông số METHOD không tồn tại")
print(f"Thông số METHOD hiện đang được đặt là: {method_values}")

dict["LOSS FUNCTION"] = "NORM_2"
print(f"Từ điển sau khi thêm là: {dict}")

if "YEARS" in dict:
    del dict["YEARS"]
print(f"Từ điển sau khi xóa là: {dict}")

dictSet = set(dict.values())
print(dictSet)

dictList = list(dict.values())
print(dictList)