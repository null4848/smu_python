a,b = 100, 200
c = 300; d = 400
e = 500 
f = 600

# 관계 연산자 True, False
# print(a==b)
# print(a!=b)
# print(a>b, a<b, a>=b, a<=b)

# 연산자 우선 순위
# 산술 연산자 -> 관계 연산자 -> 논리 연산자
# 정도만 알면 굿

# 조건식
# a = int(input("숫자를 입력하세요.>> "))
# if a<100:
#     # True -> 아래의 내용을 실행
#     print("입력한 값은 100보다 작은 수 입니다.")
# else:
#     # False -> 아래의 내용을 실행
#     print("입력한 값은 100보다 큰 수 입니다.")

# 양수, 음수인지 확인 - 0은 양수
# input_num = int(input("숫자를 입력하세요.>> "))

# 들여쓰기가 중요!!
# if input_num>=0:
#     print("양수입니다.")
# else:
#     print("음수입니다.")

# num -> 짝수인지, 홀수인지 확인
num = int(input("숫자를 입력하세요.>> "))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
    
if num % 3 == 0:
    print("3의 배수입니다.")
else:
    print("3의 배수가 아닙니다.")


