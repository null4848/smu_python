# 1. 두 숫자를 입력받아, 합과 곱을 출력하시오.

a = input("1. 숫자를 입력하시오 : ")
b = input("2. 숫자를 입력하시오 : ")
a = float(a)
b = float(b)

print("두 숫자의 합 : ", a + b)
print("두 숫자의 곱 : ", a * b)

print(a,b)

c = a
a = b
b = c

print(a,b)

# a = 100 # int 타입
# st = "안녕" # str 타입
# print("변수값 :", a)
# print("변수값 : " +a) # 에러 - 다른 타입을 + 연산자를 사용할 수 없음
# print("변수값 :", st)
# print("변수값 : " + st )

a = 10
b = 5
print(a,"+", b, "=", a+b)

c = 100
d = 7
print(a,"+", b, "=", a+b)
print("%d * %d = %d" % (c,d,c*d))
print(c,"/",d,"=",c/d)
print("%d / %d = %07.2f" % (c,d,c/d))

