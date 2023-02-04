str1=input()
str2=input()
if len(str1)==len(str2):
    if sorted(str1)==sorted (str2):
        print("it is an aligram ")
    else:
        print("it is not a aligram")
else:
    print("lenth problem,not an aligram")
