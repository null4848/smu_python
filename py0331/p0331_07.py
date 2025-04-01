# 5 * 5 2차원 리스트 -> 랜덤으로 1-25까지 숫자를 넣기
import random

# 1차원 리스트 생성 후 랜덤섞기
first_list = [i+1 for i in range(25)]
random.shuffle(first_list)

# 2차원 리스트 생성 후 1차원 리스트 값을 넣기
second_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        second_list[i][j] = first_list[5*i+j] # 5*i+j 중욧.

while True:
    # 2차원 형태로 출력
    print("        [ 좌표 맞추기 프로그램 ]")
    
    print("-"*45)
    
    print("*  |", end="\t")


    for i in range(5):
        print(i, end="\t")
    print()
    print("-"*45)
    for i in range(5):
        print(f"{i}  |", end="\t")
        for j in range(5):
            print(second_list[i][j], end="\t")
        print()
        
    # 입력 부분
    print("-"*45)
    num = int(input("1-25번 숫자를 입력하세요.>> "))
    
    # 좌표에 값 넣기
    for i in range(5):
        for j in range(5):
            if second_list[i][j] == num: second_list[i][j] = "X"
    print()

    
# import random

# a_list = [i+1 for i in range(25)]
# random.shuffle(a_list)

# b_list = [[0]*5 for i in range(5)]

# for i in range(5):
#     for j in range(5):
#         b_list[i][j] = a_list[5*1+j]

# for i in range(5):
#     print(i, end="\t")

# print()
# print("-"*40)
# for i in range(5):
#     print(f"{i}  |", end="\t")
#     for j in range(5):
#         print(b_list[i][j], end="\t")
#     print()
    