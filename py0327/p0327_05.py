# 조건문 <if, if~else, if~elif~else>
# 3가지 조건
# 음수, 0, 양수

# num = int(input("숫자를 입력하세요.>> "))
# if num>0:
#     print("양수입니다.")
# elif num==0:
#     print("0입니다.")
# else:
#     print("음수입니다.")

# 60점 이상이면 합격, 60점 미만이면 불합격
# num = int(input("시험 성적을 입력해주세요.>> "))
# if num >= 60:
#     print("합격입니다.")
# else:
#     print("불합격입니다.")
    
# 70점 이상 합격 69~60점 재시험 60점 미만 불합격
# num = int(input("시험 성적을 입력해주세요.>> "))
# if num >= 70:
#     print("합격입니다.")
# elif 60<=num<=69:
#     print("재시험입니다.")
# else:
#     print("불합격입니다.")

# 시험 -> 90점 이상 A, 80점 이상 B, 70점 이상 C, 60점 이상 D, F
#100~97점, A+ 96~93점, A 92~90 A-, 89~87점 B+ 86~83점 B, 82~80 B-
score = int(input("점수를 입력하세요.>> "))
if score>=90:
    print("A",end="")
    if score>=97: print("+")
    elif score>=93: pass # 지나가겠다는 의미
    else: print("-")
elif score>=80:
    print("B",end="")
    if score>=87: print("+")
    elif score>=83: pass
    else: print("-")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")
    
# print("안녕", end="") #end 옵션을 사용하면 줄바꿈을 하지 않음
# print("하세요")

