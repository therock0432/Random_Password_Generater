import random
new = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-_=+/.,?\@$%&*()!:'[]{}"
len = 8
p = "".join(random.sample(new, len))
print("Password is :", p)
