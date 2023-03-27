from mk2 import *
str1 = str(input("Enter the String1: "))
str2 = str(input("Enter the String2: "))
result = comp_str(str1, str2)
if result == 0:
    print("0")
elif result>0:
    print("1")
elif result<0:
    print("-1")