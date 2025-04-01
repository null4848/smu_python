# 좌표 맞추기 프로그램을 구현하시오
import random
first_list = [i+1 for i in range(25)]
random.shuffle(first_list)

second_list=[[0]*5 for i in range (5)]

while True:
    
    for i in range(5):
        for j in range(5):
            second_list[i][j] = first_list[5*i+j]
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
        
    print("-"*45)
    num = int(input("1-25번 숫자를 입력하세요.>> "))
    
    for i in range(5):
        for j in range(5):
            if second_list[i][j] == num: 
                second_list[i][j] = "X"
    print()
        
    
