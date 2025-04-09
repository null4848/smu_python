# 숫자맞추기 프로그램
# 5 * 5 2차원 리스트 -> 랜덤으로 1-25까지 숫자를 넣기
# 1차원 리스트 생성
# 1차원 리스트 랜덤으로 섞기
# 2차원 리스트 생성
# 2차원 리스트에 1차원 랜덤번호를 넣기

# import random
# first_list = [i+1 for i in range(25)]
# random.shuffle(first_list)

# print(first_list)

# second_list = [[0]*5 for i in range(5)]
# for i in range(5):
#     for j in range(5):
#         second_list[i][j] = first_list[5*i+j]

# while True:
#     print("      [ 좌표 맞추기 프로그램]")
#     print("-"*50)
#     print("*  |", end="\t")
    
#     for i in range(5):
#         print(i, end = "\t")
#     print()
#     print("-"*45)

#     for i in range(5):
#         print(f"{i}  |",end="\t")
#         for j in range(5):
#             print(second_list[i][i], end="\t")
#         print()
            
#     print("-"*50)
#     number = int(input("1-25번 숫자를 입력하세요.>> "))
    
#     for i in range(5):
#         for j in range(5)
#             if number == second_list[i][j]:
#                 number = "X"
#         print()
        
# 숫자맞추기 프로그램
# 5 * 5 2차원 리스트 -> 랜덤으로 1-25까지 숫자를 넣기
# 1차원 리스트 생성
# 1차원 리스트 랜덤으로 섞기
# 2차원 리스트 생성
# 2차원 리스트에 1차원 랜덤번호를 넣기

import random

first_list = [i+1 for i in range(25)]
random.shuffle(first_list)

second_list = [[0]*5 for i in range(5)]
for i in range(5):
    for j in range(5):
        second_list[i][j] = first_list[5*i+j]

while True:
    print("        [ 좌표 맞추기 프로그램] ")
    print("-"*45)
    print("*  |", end="\t")

    for i in range(5):
        print(f"{i}", end="\t")
    print()
    print("-"*45)

    for i in range(5):
        print(f"{i}  |", end="\t")
        for j in range(5):
            print(second_list[i][j], end="\t")
        print()
    print("-"*45)
        
    number = int(input("1-25번 숫자를 입력하세요.>> "))
    
    for i in range(5):
        for j in range(5):
            if second_list[i][j] == number:
                second_list[i][j] = "X"
    print()
        


        