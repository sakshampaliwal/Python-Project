import random
passlen=int(input("enter length of password:"))
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*_"
p="".join(random.sample(s,passlen))
print(p)