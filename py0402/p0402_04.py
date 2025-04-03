# print() 변수 뒤에 ()가 있으면 함수

a,b = 10,20
result = a+b
result2 = a-b
result3 = a*b
result4 = a/b

c,d = 100,200
r = c+d
r2 = c-d
r3 = c*d
r4 = c/d

e,f = 50,100
k = e+d
k2 = e-d
k3 = e*d
k4 = e/d

# 함수 선언
# def cal(x,y):
#     result = x+y
#     print(result)
#     result2 = x-y
#     print(result2)
#     result3 = x*y
#     print(result3)
#     result4 = x/y
#     print(result4)
    
# cal(a,b)
# cal(c,d)
# cal(e,f)

# def add():
#     print("안녕하세요.")
#     print("안녕하세요.")
#     print("안녕하세요.")
    
# print("누군가 오고 있어요")
# print("인사")
# add()

# def add(x,y):
#     print("x:",x)
#     print("y:",y)
#     print("x+y:",x+y)

# a = 10
# b = 20
# c = 30
# d = 40

# add(a,b)
# add(a,c)
# add(a,d)
# add(c,d)

# 두 수를 입력받아 사칙연산 (+,-,*,/) 출력하시오.
def cal(x,y):
    print("더하기 : ", x+y)
    print("빼기 : ", x-y)
    print("곱하기 : ", x*y)
    print("나누기 : ", x/y)
    
num1 = int(input(" 첫번째 숫자를 입력하세요.>> "))
num2 = int(input(" 두번째 숫자를 입력하세요.>> "))
cal(num1,num2)

num3 = int(input(" 첫번째 숫자를 입력하세요.>> "))
num4 = int(input(" 두번째 숫자를 입력하세요.>> "))
cal(num3,num4)

num5 = int(input(" 첫번째 숫자를 입력하세요.>> "))
num6 = int(input(" 두번째 숫자를 입력하세요.>> "))
cal(num5,num6)
