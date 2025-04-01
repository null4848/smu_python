# 5X5 리스트 = 0으로 초기화
sample_list = [[0]*5 for i in range(5)]
print(sample_list)

# 5X5 리스트 = 0으로 초기화
sample_list = list() # list 초기화
for i in range(5):
    temp=[]
    for j in range(5):
        temp.append(0)
    sample_list.append(temp)

print(sample_list)


# a_list = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25],
# ]

# import random
# 1. 순차적 리스트 생성
# sample_list = [i+1 for i in range(25)]
# 2. 리스트 섞기
# random.shuffle(sample_list) # 랜덤리스트 - 리스트의 숫자가 랜덤으로 섞임
# 3. 2차원 초기화 리스트 생성
# a_list = [[0]*5 for i in range(5)] # 깊은 복사
# 4. 2차원 리스트에 랜덤 리스트의 값을 출력
# for i in range(5):
    # for j in range(5):
    #     a_list[i][j] = sample_list[5*i+j] # 랜덤숫자가 들어감.
        
# 5 X 5 리스트 출력
# for i in range(5):
#     for j in range(5):
#         print(a_list[i][j],end="\t")
#     print()
        
# 5*5 리스트 초기화
# a_list =[[0]*3]*5 # 얕은 복사
# a_list = [[0]*5 for i in range(5)] # 깊은 복사
# print(a_list)
# for i in range(5):
# for j in range(5):
# a_list[i][j] = 5*i+(j+1)
# print(a_list)

        
# 1 - 25
# import random
# a_list = [i+1 for i in range(25)]
# print(a_list) # 1,2,....,24,25
# random.shuffle(a_list)
# print(a_list)

# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25


# for i in range(5):
#     for j in range(5):
#         print(a_list[i][j], end=" ")
#     print()

# a_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for i in range(3):
#     for j in range(3):
#         print(a_list[i][j], end="\t")
#     print()

# 1차원 리스트
# aa= [10,20,30]
# print(aa[0]) # 10

# 2차원 리스트
# aa = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

# print(aa[0]) # [1,2,3,4]
# print(aa[0][1]) # 2


# 리스트 값 변경
# a_list = [1,2,3,4,5,6,7,8,9]
# a_list[5] = 10
# print(a_list)

# 값을 변경할 때 1:2, 2의 위치값이 포함
# a_list[1:2] = [100,200]
# print(a_list)

# 역순출력
# a_list = [1,2,3,4,5,6,7,8,9]
# print(a_list[::-1])

# a_list = [1,2,3,4,5]
# print(a_list[5])

# 모양출력
# for i in range(10):
#     for j in range(i+1): # 1,2,3,4,5,6,7,8,9,10
#         print("*",end="")
#     print()

# continue - 그 위치에서 중지 후 다시 for문 실행
# 1-10까지 진행을 하는데, 1,2,3 - continue : 제외,4,5,6,7,8,9,10

# break - 반복문 완전 중지
# 1-10까지 진행을 하는데, 1,2,3 - break 반복문 끝

# pass -> 실행할 구문이 없음, for문을 계속 반복
# 1-10까지 진행을 하는데, 1,2,3 - pass, 4,5,6,7,8,9,10 10번을 실행

# # 입력한 숫자가 50을 넘으면 프로그램을 종료하고 총합을 구하시오
# 입력한 숫자 중 5의 배수는 제외

# for i in range(10):
#     if i%2==1:continue
#     print(i)

# for i in range(10):
#     if i%2==1:break
#     print(i)
    
# for i in range(10):
#     if i%2==1:pass
#     print(i)


# sum = 0
# while True:
#     if sum<50:
#         num = int(input("숫자를 입력해주세요. >> "))
#         if num%5==0:
#             print(f"입력한 숫자 : {num}, 5의 배수는 제외!")
#             continue # 실행을 1번 중지
#         sum = sum + num
#     else: break
# print("총합 :",sum)
    
# 1-100까지의 숫자의 합을 구할때 합계가 200을 넘을때 숫자를 출력하시오.
# 1+2+3+4+...200 이 넘는 위치 값을 출력하시오.
# break

# sum = 0
# i = 0
# for i in range(100):
#     sum = sum + i
#     if sum >= 200:
#         break
    
# print(f"i : {i}, sum : {sum}")
# print(f"i이전 : {i-1}, sum : {sum-i}")


# 반복문 - for, while
# 1-100까지 리스트 생성
# a_list = [i+1 for i in range(100)]
# print(a_list)

# sum = 0
# a_list 홀수의 합계를 구하시오
# for i in a_list:
#     if i%2==1:
#         sum = sum + i
# print("홀수 합계 : ",sum)

# random.random() 함수 : 0<=x<1 사이의 랜덤실수를 가져옴.
# import random
# print(random.random())
# print(int(random.random()*10)+1) # 1, 10
# print(int(random.random()*10)+0) # 0, 9
# print(random.randint(1,10))

# import random
# a_list = [i+1 for i in range(45)]
# print(a_list)
# random.shuffle(a_list)
# print(a_list)
# print(a_list[:6])

# 로또 프로그램
# 6개 랜덤숫자와 입력숫자 6개를 출력하시오.

# import random
# lotto = [i+1 for i in range(45)] #1,2,3....44,45
# lotto_input = []
# my_input = []

# lotto_input = random.sample(lotto, 6)
# for i in range(1,7):
#     lotto.append(random.randint(1,45))

# for j in range(1, 7):
#     input_num = int(input("숫자를 입력하세요.>> "))
#     my_input.append(input_num)

# print("로또번호 :",lotto_input)
# print("입력번호 :",my_input)

# 10번의 숫자를 입력받아, 합계를 구하시오.
# for문, while문
# total_for = 0
# for i in range(3):
#     num = int(input("숫자를 입력하세요.>> "))
#     total_for += num
    
# print("합계 : ",total_for)

# total_whie=0
# i = 0
# while i<3:
#     num = int(input("숫자를 입력하세요.>> "))
#     i = i + 1
#     total_whie += num
    
# print("합계 : ",total_whie)

# while 문
# i = 0
# while i<10:
#     print(i)
#     i = i+1

# for 문
# for i in range(10):
#     print(i)