import math

# a = 3.141592
# b = 3.51582

# 올림
# print(math.ceil(a))
# 반올림
# print(round(a)) # 3
# print(round(b,3)) # 3자리까지 표시, 3.516
# print(round(a,4)) # 4자리까지 표시, 3.1416
# 버림
# print(math.floor(b)) # 3

# a에서 소수점 3자리에서 ceil 올림해서 2자리까지 표시해서 출력하시오.
# 3.15

# a * 100 / 100
# a * 100 # 314.1592
# print(math.ceil(a*100) / 100) # 3.15

# b에서 소수점 5자리에서 ceil올림해서 4자리까지 표시해서 출력하시오.

# print(math.ceil(b*10000)/10000)

# math 안에 있는 함수를 출력
# print(dir(math))

# import random

# 0.0000000000000000 < x < 1.0000000000000000
# print(random.random())
# 1-45까지 랜덤숫자 출력
# print(random.randint(1,45))

# 리스트에서 1개 랜덤추출
# a_list = [1,2,3,4,5]
# print(random.choice(a_list))

# 리스트에서 개수만큼 랜덤 추출 - 중복 없이
# print(random.sample(a_list,3))

# 리스트를 랜덤으로 섞기.
# random.shuffle(a_list)
# print(a_list)

# 카드 스페이드 > 다이아 > 하트 > 클로버
# 번호 1-A,2,3,4,5,6,7,8,9,10,11-J,12-Q,13-K

# 카드 1장 - 카드모양, 번호
# 카드 모양 4개
# 번호 13개
# 카드 총 개수 : 52장 카드가 존재

# 리스트 - 딕셔너리
# [
    # {"shape":4,"no":1},
    # {"shape":4,"no":2}
# ]

import random

cList = []
sh = ["CLOVER", "HEART", "DIAMOND", "SPADE"]
no = ["","A","2","3","4","5","6","7","8","9","10","J","Q","K"]

# 카드 생성
for i in range(52):
    cList.append({"shape":i//13, "no":i%13+1})

# 카드 랜덤으로 섞기
random.shuffle(cList)

# myCard, youCard

myCard = []
youCard = []

for i in range(5):
    myCard.append(cList[i])

for i in range(5,10):
    youCard.append(cList[i])

# 내 카드 출력 - 번호에 해당하는 글자를 출력
for i in myCard:
    print(f"[ {sh[i['shape']] }, {no[i['no']]} ]" )
    
# 상대 카드 출력
for i in youCard:
    print(f"[ {sh[i['shape']] }, {no[i['no']]} ]")

# 전체 카드 출력
# for c in cList:
#     print(c['shape`'],c['no'])

# 내 카드, 상대카드를 비교해서 - 승리, 패배,무승부
# 숫자만 비교해서 숫자가 높은 카드 - 승리
# 0,0 1,1 2,2 3,3

# score = {"myWin":0, "youWin":0,"draw":0 }

# mywin = []
# youwin = []
# draw = []
# for i in range(5):
    
#     if myCard[i]['no'] > youCard[i]['no']:
#         score["myWin"] += 1
#         mywin.append(myCard[i])
#     elif myCard[i]['no'] < youCard[i]['no']:
#         score["youWin"] += 1
#         youwin.append(myCard[i])
#     else:
#         score["draw"] += 1
#         draw.append(myCard[i])
        
# print()
# print("[ 카드 승부 확인 ]")
# print(f"승리 : {score["myWin"]}, 무승부 : {score["draw"]} , 패배 : {score["youWin"]}")
# print()

# def card_print(x):
#     for i in x:
#         print(f"[ {sh[i['shape']] }, {no[i['no']]} ]" )
#     print()


# # 승리한 카드 출력
# print("승리한 카드 출력") 
# card_print(mywin)
# print("패배한 카드 출력")
# # 패배한 카드 출력
# card_print(youwin)
# print("무승부 카드 출력")
# # 무승부 카드 출력
# card_print(draw)

score = [0]*5

mywin = []
youwin = []
draw = []
for i in range(5):
    
    if myCard[i]['no'] > youCard[i]['no']:
        score[i] = 2
        mywin.append(myCard[i])
    elif myCard[i]['no'] < youCard[i]['no']:
        score[i] = 1
        youwin.append(myCard[i])
    else:
        score[i] = 0
        draw.append(myCard[i])
        
print()
print("[ 카드 승부 확인 ]")
print(f"승리 : {score.count(2)} 무승부 : {score.count(1)} , 패배 : {score.count(0)}")
print()

# 승리 카드 출력
print("[ 승리 카드 ]") 
for i, c in enumerate(myCard):
    if score[i] == 2:
        print(f"[ {sh[c['shape']] }, {no[c['no']]} ]")

# 패배 카드 출력
print("패배한 카드 출력")

# 무승부 카드 출력
print("무승부 카드 출력")
