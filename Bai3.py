import random
def create(n):
    password = ["CNTT", "KHMT", "KTPM", "HTTT"]
    student_tk = {}
    for i in range(1, n + 1):
        student_id = f"202360000{i}"
        rd = random.choice(password)
        password1 = student_id + rd
        student_tk[f"Account{i}"] = {
            "username" : student_id,
            "Password" : password1
        }
    return student_tk
n = int(input("Nhập số lượng tài khoản: "))
if 10 <= n <= 100000:
    accounts = create(n)
    for account, values in accounts.items():
       print(f"{account}: {{'Username': {values['username']}, 'Password' : {values['Password']}")
else:
    print("N/A")
             
    