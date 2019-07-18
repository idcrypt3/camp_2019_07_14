import hashlib

user_entered_password = input("What would you like to encrypt? Keep in mind that this cannot be decrypted due to Hashing being almost impossible to reverse")
salt = "5gz"
db_password = user_entered_password+salt
h = hashlib.md5(db_password.encode())
print(h.hexdigest())