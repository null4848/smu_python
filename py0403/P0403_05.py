# 로또 프로그램
import random
# 6개 숫자 랜덤 번호 생성
# 6개 입력한 번호 생성
# 당첨번호 확인
# 출력

my_lotto = []
win_lotto = []
lotto = [ i+1 for i in range(45)]
lotto2 = [ i+1 for i in range(45)]

def lotto_shuffle():
    global lotto
    random.shuffle(lotto)


while True:
    print("[ 로또 프로그램 ]")
    print("-"*30)
    print("1. 로또프로그램 재실행")
    print("2. 로또번호 입력")
    print("3. 로또번호 당첨확인")
    print("4. 로또리스트 모두 확인")
    print("5. 내가입력한 로또번호 확인")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    
    if choice == 1:
        lotto_shuffle()
    elif choice == 2:
        print("[ 로또번호 입력 ]")
        
    elif choice == 2:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 0:
        pass
    
    











































my_lotto = [0]*6
win_lotto = []
lotto = [i+1 for i in range(45)]
lotto2 = [i+1 for i in range(45)]

def lotto_shuffle():
    global lotto, lotto2
    random.shuffle(lotto)
    lotto2 = [i+1 for i in range(45)]
    
lotto_shuffle()
while True:
    print("[ 로또 프로그램 ]")
    print("-"*30)
    print("1. 로또프로그램 재실행")
    print("2. 로또번호 입력")
    print("3. 로또번호 당첨확인")
    print("4. 로또리스트 모두 확인")
    print("5. 내가입력한 로또번호 확인")
    print("0. 프로그램 종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    
    if choice == 1:
        lotto_shuffle()
    elif choice == 2:
        count = 0
        while True:
            print("[ 로또번호 입력 ]")
            print("-"*60)
            for i in range(45):
                if i%7 != 0: print(lotto2[i],end="\t")
                else:
                    print()
                    print(lotto2[i],end="\t")
            print()
            print()
            choice = int(input("로또번호를 입력하세요.(0. 이전화면)>> "))
            if choice == 0:
                break
            elif choice<0 or choice>45:
                print(f"{choice}는 존재하지 않는 번호입니다.")
                continue
            
            temp = 0
            for i in lotto2:
                if i == choice:
                    lotto2[i-1] = "X"
                    my_lotto[count] = choice
                    count += 1
                    temp = 1
                    
            if temp == 0: print(f"{choice}는 이미 입력한 번호입니다. 다시 입력해주세요.")
            
            if count >= 6:
                print("로또번호 6개를 입력 완료하셨습니다.")
                break
                            
    elif choice == 3:
        for i in lotto[:6]:
            for j in my_lotto:
                if i == j:
                    win_lotto.append(i)
        print("[ 로또당첨번호 확인 ]")
        print("-"*50)

        print(f"당첨 번호 : {lotto[:6]}")
        print(f"입력한 번호 : {my_lotto}")
        print(f"당첨된 번호 : {win_lotto}")
        print(f"당첨 갯수 : {len(win_lotto)}개")
                    
    elif choice == 4:
        print(lotto)
    elif choice == 5:
        print(my_lotto)
    else:
        print("[ 프로그램 종료 ]")
        break