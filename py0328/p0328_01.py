# 파이썬 타입
# bool 타입 / 숫자 - int 타입, float 타입 / str 타입

# bool 타입 -> True, False
# int 타입 -> 정수형
# float 타입 -> 실수형
# str 타입 -> 문자열 타입 : "", ''와 같은 문자열 안에 입력

if True:
    print("참입니다.")
    
if False:
    print("거짓입니다.")
    
# 같은 의미의 코드
if 10>3:
    print("정상")
if True:
    print("정상")

# 연산 숫자일 때만 가능
print(1+2)
print(1+1.2)
# print("안녕"+1) -> 출력 안됨
print("안녕")
# 타입이 다른 경우는 쉼표를 이용해서 출력
print("안녕",1)

print(10/3)
print("숫자 : {:.2f}".format(10/3))

# 문자열 -> 숫자형태일 경우
print("1") # 문자열 타입
print("숫자1") # 숫자 태의 문자열만 숫자 타입으로 변경 가능
print(int("1")+1) # st 타입

# 숫자 타입 변경 -> int, float으로 변경 가능
print(int(1.5)) # float -> int로 타입변경 : 소수점이 사라짐

# 문자열 float -> int 변경은 안됨
# print(int("1.5")) -> 에러남
print(float("1.5")) # 가능

print(str(1.5)) # 문자열 타입 변경

#--------------------------------------------------------------------------
# 변수
a =  10 # = -> 할당을 의미함
a = 5 # int 타입
b = 1.5 # float 타입
c = "안녕" # str 타입

# print(c+a) str + int 덧셈 불가능
print(a+b) # int + float 덧셈 가능

# list 타입 - 값을 여러개 저장
list_a = [1,2,3,4]
print(list_a)

print(list_a[0]+list_a[1]+list_a[2]+list_a[3])

# input -> 데이터를 입력받는 명령어 : str 타입 1개
# score = input("데이터를 입력하세요.>> ")
# print("입력 데이터 : ",score)

# 두 수를 입력받아 합계, 평균을 출력하시오.
# num1 = input("숫자를 입력하세요.>> ")
# num2 = input("숫자를 입력하세요.>> ")
# print(num1+num2) #100200

# int 타입으로 변경
# num1 = int(input("숫자를 입력하세요.>> "))
# num2 = int(input("숫자를 입력하세요.>> "))
# print(num1+num2) #300

# 조건문
# score = int(input("점수를 입력하세요.>> "))
# if score>=60:
#     print("합격")
# else:
#     print("불합격")
    
# score = int(input("점수를 입력하세요.>> "))
# if score>=70:
#     print("합격")
# elif score>=60:
#     print("재시험")
# else:
#     print("불합격")

score = int(input("점수를 입력하세요.>> "))
# 90점 이상 A,B,C,D,F를 출력하시오.
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")