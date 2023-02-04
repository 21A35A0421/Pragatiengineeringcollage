email='murali@gmail.com'
pwd=123456
otp=5678
cemail=input('enter email:')
cpwd=int(input('enter password'))
if email==cemail and pwd==cpwd:
    print('login succesful')
    cotp=int(input('enter otp'))
    if otp==cotp:
        print('order conformed sucessfully')
    else:
         print('order cancelled due to invali otp')
elif email!=cemail and pwd==cpwd:
    print('login failed due to invalid email')
elif email==cemail and pwd!=cpwd:
    print('login failed due to invalid passward')
elif email!=cemail and pwd!=cpwd:
    print('login failed due to invalid email and passward')

