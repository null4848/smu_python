### 파일 - 저장해서 불러오기

def score_cal(i,score):
    while True:
        score[i] = input(f"{title[i+2]} 점수를 입력하세요.>> ")
        if score[i].isdigit(): 
            score[i] = int(score[i])
            if 0<=score[i]<=100:
                break
            else: print("점수는 0~100사이의 값을 입력하셔야 합니다.")
        else: print("숫자만 가능합니다.")
    
students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]

count = 4    # 학생번호를 생성
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print(" "*10,end="")
    print("[ 학생성적 프로그램 ]")
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("0. 프로그램종료")
    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    
    # 번호 선택
    if choice == 1:
        while True:
            print("[ 학생성적 입력 ]")
            no = count
            name = input(f"{no}번 학생. 이름을 입력하세요.(0.이전화면 이동)>> ")
            # 이전화면 이동 확인
            if name == '0': break # 학생 성적입력에서 전체화면으로 이동
            score = [0]*3
            score_cal(0,score)
            score_cal(1,score)
            score_cal(2,score)

            # while True:
            #     kor = input("국어 점수를 입력하세요.>> ")
            #     if kor.isdigit(): 
            #         kor = int(kor)
            #         if 0<=kor<=100:
            #             break
            #         else: print("점수는 0~100사이의 값을 입력하셔야 합니다.")
            #     else: print("숫자만 가능합니다.")
                
            # while True:    
            #     eng = input("영어 점수를 입력하세요.>> ")
            #     if eng.isdigit(): 
            #         eng = int(eng)
            #         if 0<=eng<=100:
            #             break
            #         else: print("점수는 0~100사이의 값을 입력하셔야 합니다.")
            #     else: print("숫자만 가능합니다.")   
                         
            # while True:
            #     math = input("수학 점수를 입력하세요.>> ")
            #     if math.isdigit(): 
            #         math = int(math)
            #         if 0<=math<=100:
            #             break
            #         else: print("점수는 0~100사이의 값을 입력하셔야 합니다.")
            #     else: print("숫자만 가능합니다.")    
                
            total = score[0]+score[1]+score[2]
            avg = total/3
            rank = 0
                    
            # students 입력
            students.append({"no":no,"name":name,"kor":score[0],"eng":score[1],"math":score[2],"total":total,"avg":avg,"rank":rank})
            
            print(f"{no}번 {name} 학생 성적을 저장했습니다.")
            print()
            count += 1

    elif choice == 2:
        print("[ 학생성적 출력]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        print("-"*60)
        
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\t")
        print()
    
    elif choice == 3:
        print("[ 학생성적수정 ]")
        name = input("수정하려고 하는 학생 이름을 입력하세요.>> ")
        temp = 0 # 찾고자 하는 학생이 없을 경우
        for s in students:
            if name in s['name']:
                print(f"{name} 학생이 있습니다. 성적을 수정합니다.")
                print("[ 수정할 과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("-"*10)
                choice = int(input("원하는 번호를 입력하세요.>> "))
                
                # 수정할 과목 확인
                if choice == 1:
                    print(f"현재 국어점수 : {s['kor']}")
                    s['kor'] = int(input("변경 국어 점수 : "))
                    
                    # 합계, 평균 수정
                    print(f"국어점수 : {s['kor']}로 변경되었습니다.")
                elif choice == 2:
                    pass
                elif choice == 3:
                    pass
                
                print()
        
        if temp == 0:
            print("프로그램 종료")
            break
        
    elif choice == 0:
        print("[ 프로그램종료 ]")
        break