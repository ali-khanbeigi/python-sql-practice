import random
import string

def generate_password(lenght):
        chars = string.ascii_letters + string.digits + "%^&*#@$!()"
        password = ''.join(random.choice(chars) for i in range(lenght))
        return password
    
for n in range(4):
    lenght = int(input("طول پسوورد؟"))
    print("password:", generate_password(lenght)) 
print("تعداد تلاش ها بیش از حد مجاز")


