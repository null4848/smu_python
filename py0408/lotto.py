# lotto 프로그램
 
import random
lotto = random.sample(range(1,46),6)
my_lotto = []
lotto_count = 0
lotto_list = []

i = 0
while i<6:
    print("랜덤번호 : ", lotto)
    lotto_input = int(input(f"{i+1}번째 로또 번호를 입력해주세요.>> "))
    if lotto_input not in my_lotto:
        my_lotto.append(lotto_input)
        i += 1
        
for j in range(6):
    print("확인 : ", my_lotto[j])    
    if my_lotto[j] in lotto:
        lotto_list.append(my_lotto[j])
        lotto_count += 1
        
print(f"랜덤번호 : {lotto}")
print(f"입력번호 : {my_lotto}")
print(f"당첨개수 : {lotto_count}")
print(f"당첨번호 : {lotto_list}")
