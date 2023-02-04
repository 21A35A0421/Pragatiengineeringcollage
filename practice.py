calls=3000
sms=100
data=2048
duration=84
n=int(input('enter the day no'))
if n>duration:
    print('your plan is expired,please recharge')
else:
    csms=int(input("enter no of sms used:"))
    cdata=int(input('enter data used:'))
    ccalls=int(input('enter no of dailed calls'))
    if csms>=sms:
        print("sms linit is over")
    else:    
        print('total no of sms remainig:',sms-csms)
    if cdata>=data:
        print('data limit is over')
    else:
        print('amount no of data remainig:',data-cdata,'MB')
    if ccalls>=calls:
        print('calls limit is over')
    else:
        print('total no of calls remainig:',calls-ccalls)
    if n<duration:
        print('no of days remaining',duration-n)



    
