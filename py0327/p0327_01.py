# 파이썬 변수타입
# bool 타입 - True, False 
# int 타입 - 정수 , float 타입 - 실수 
# str 타입 - 문자열

# print() - 출력
print("안녕") # 문자열 출력

# 변수 선언
변수 = 10 # 변수명 한글 가능 (영어 권장) 
a = 20 
num = 30

# format 형태 사용 권장
print("입력된 숫자 : ", a)
print("입력된 숫자 : %d" % a) # 두 개 이상 -> 괄호 필수
print("입력된 숫자 : {} ".format(a))
print(f"입력된 숫자 : {a}")

# input -> 입력
# input을 이용해 입력된 값은 str 타입이기 때문에 형변환을 해줘야 함
# num1 = int(input("숫자를 입력하세요.>> "))
# num2 = int(input("숫자를 입력하세요.>> "))
# print("입력된 숫자 : {}, {} / 합계 : {}".format(num1,num2,num1+num2))

# 학생 성적 프로그램
# 이름, 국어, 영어, 수학 입력받아, 합계, 평균을 출력하는 프로그램을 구현
print("-"*50)
print("                 학생성적프로그램")
print("-"*50)
name = input("이름을 입력하세요.>> ")
kor = int(input("국어 점수를 입력하세요.>> "))
eng = int(input("영어 점수를 입력하세요.>> "))
math = int(input("수학 점수를 입력하세요.>> "))
total = kor + eng + math
avg = total/3
print()
print("이름\t국어\t영어\t수학\t합계\t평균\t")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name,kor,eng,math,total,avg))