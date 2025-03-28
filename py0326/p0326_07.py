a = 100
b = 50

# b = 100, a = 50 값을 교체

print(a)
print(b)

# a = b
# b = a

# print(a) # 50
# print(b) # 50

# 두 변수의 값을 교체하려면, 추가적인 변수 c를 하나 두고 값을 보관해서 교체
# c = a
# a = b
# b = c

a,b = b,a # 파이썬 a,b의 변수 값 교체 방법

print(a) # 50 
print(b) # 100

# 입력 : input, 출력 : print

# 변수에 괄호가 있다면 함수 -> 어떠한 기능 구현을 말함
# print()

# 입력 - !무조건! 문자열(str) 타입
# 타입 변경 - 정수 : int(), 실수 : float(), 문자열 : str()
a = input("1. 숫자를 입력하세요. ")
b = input("2. 숫자를 입력하세요. ")
a = float(a) # str -> float
b = float(b) # str - > float
print(a)
print(b)
print(a,b) 
print(type(a)) # 문자열
print(type(b)) # 문자열
print(a+b) # 10 + 5 15 X 105 문자열이기 때문에 계산이 안됨

