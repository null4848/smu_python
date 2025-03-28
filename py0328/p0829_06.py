# 숫자 맞추기 프로그램
import random

# 입력한 숫자 저장 리스트
input_list = []

# randint(1,45) 1~45번 사이의 숫자 1개를 가져옴.
lotto = random.randint(1,45)

#------------
for i in range(10):
    int_input = int(input("{}번째 숫자를 입력하세요.(1-45번 사이)>> ".format(i+1)))
    input_list.append(int_input) # 리스트에 숫자 추가!!! 

    # 랜덤번호와 입력번호 비교
    if lotto==int_input:
        print("당첨")
        break # for문 종료
    elif lotto>int_input:
        print("틀렸습니다. {}보다 더 큰 수를 입력하세요.".format(int_input))
    else:
        print("틀렸습니다. {}보다 더 작은 수를 입력하세요.".format(int_input))
#---------

print("랜덤번호 : {}".format(lotto))
print("입력번호 : {}".format(input_list))