
students = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1}

def cal(ss): 
    ss['kor'] = int(input("수정할 국어 점수를 입력하세요.>> "))
    ss['total'] = ss['kor'] + ss['eng'] + ss['math']
    ss['avg'] = ss['total']/3

print("[ 학생성적 수정 ]")
s = {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1}

# 국어점수 변경 함수 호출
cal(s)
print("수정된 국어점수 : ",s['kor'])


# def cal(a_list):
#     a_list[0]=100
#     a_list[1]=200
    

# a_list = [0,0]
# a_list[0] = 10
# a_list[1] = 20

# print("함수 호출 전 a_list :",a_list[0],a_list[1])

# cal(a_list)
# print("함수 호출 후 a_list :",a_list[0],a_list[1])
# 함수 선언

# def cal(a,b):
#     a=100 # 지역변수 - 함수내일반변수는함수를벗어나면사라짐 - bool,int,float,str
#     b=200

# # 함수 밖

# a=10 # 전역변수
# b=20
# print("함수호출전 a,b :",a,b) # a = 10 b = 20

# # 함수 호ㅊ출
# cal(a,b)
# print("함수호출후 a,b :",a,b)



# students = [
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
# ]

# def stu_print():
#     for s in students:
#         print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}\t")
        
# print("1. 학생성적입력")
# print("2. 학생성적출력")
# choice = int(input("원하는 번호를 입력하세요.>> "))
# if choice == 2:
#     stu_print()


# 이름. 국어, 영어, 수학 점수를 입력받아, 합계, 평균을 출력하시오.

# 함수 선언
# def cal(kor, eng, math):
#     total = kor+eng+math
#     avg = total/3
#     return total, avg

# no = 1
# name = input("이름을 입력하세요.>> ")
# kor = int(input("국어점수를 입력하세요.>> "))
# eng = int(input("영어점수를 입력하세요.>> "))
# math = int(input("수학점수를 입력하세요.>> "))
# total, avg = cal(kor, eng, math)
# print(f"합계 : {total}, 평균 : {avg}")
      
# 직사각형 넓이와 둘레를 구하는 프로그램을 구현하시오.
# 가로 * 세로, 가로길이*2+세로길이*2

# def cal(x,y):
#     sum = (x+y)*2
#     mul = x*y
#     print(f"넓이 : {mul}, 둘레 : {sum}")
    
    
# # 가로 세로 입력

# x = int(input("가로를 입력하세요.>> "))
# y = int(input("세로를 입력하세요.>> "))
# cal(x,y)

# 입력을 5개를 받아, 짝수만 모두 더한 값을 출력하시오.
# def cal(n_list):
#     sum = 0
#     for n in n_list:
#         if n%2==0: sum += n
#     return sum

# n_list = [0]*5
# for i in range(5):
#     n_list[i] = int(input("숫자를 입력하세요.>> "))
#     result = cal(n_list)
# print("짝수의 합 :",result)

# 함수를 사용해서 두 수를 입력받아
# 10~20 입력받으면 10+11+12+13...20 출력하시오.
# def add(n1,n2):
#     if n1>n2: n1,n2 = n2,n1
#     sum = 0
#     for i in range(n1,n2+1):
#         sum = sum + i
#     print("합계 : ", sum)
    
# n1 = int(input("숫자를 입력하세요.>> "))
# n2 = int(input("숫자를 입력하세요.>> "))
# # 큰수 먼저 넣어도, 10,2->2,10\

# add(n1,n2)

# 함수사용
# 중복 코드가 잇을때
# 소스가 너무 복잡할대
# 먼저 프로그ㅐㅁ 모두 구현해두고 중복되고 잇는지 확인후 함수 사용


# num1, num2, num3 값을 입력받아, 합계, 평균을 구하시오
# # 함수선언
# def add(kor,eng,math):
#     return kor+eng+math

# kor = input("국어 점수를 입력하세요.>> ")
# eng = input("영어 점수를 입력하세요.>> ")
# math = input("수학 점수를 입력하세요.>> ")
# total = add(kor,eng,math)
# avg = total/3

# print(kor,eng,math,total,avg)