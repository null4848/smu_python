# 1-100까지 랜덤숫자를 생성해서 정답을 맞추는 프로그램을 구현하시오.

# 랜덤 숫자 생성
# num list 생성
# n 변수 생성
# 10번 for문 생성
# 입력한 숫자, num list에 저장
# 정답 비교
# 데이터 출력

import random
num = []
ran_num = random.randint(1,100)
n = 0

for n in range(1,11):
    
    input_num = int(input("숫자를 입력하시오.>> "))
    num.append(input_num)

    if ran_num == input_num:
        print("정답입니다.")
        break
    elif ran_num > input_num:
        print("더 큰 수를 입력하세요.")
    else:
        print("더 작은 수를 입력하세요.")
        
    
print("도전 회수 : {}".format(n))
print("도전 번호 : {}".format(num))
print("랜덤 번호 : {}".format(ran_num))


