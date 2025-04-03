students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":1},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":67.0,"rank":1},
]

count = 4
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print(" "*25,end="")
    print("[ 학생성적 프로그램 ]")
    print("-"*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("-"*50)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()

    
    # 입력번호 확인
    if choice == 1:
        while True:
            print("[ 학생성적입력 ]")
            print("-"*30)
            no = count
            name = input("학생 이름을 입력하세요.(0. 이전화면 이동)>> ")
            if name == '0': continue
            kor = int(input("국어점수를 입력하세요.>> "))
            eng = int(input("영어점수를 입력하세요.>> "))
            math = int(input("수학점수를 입력하세요.>> "))
  
            total = kor+eng+math
            avg = total/3 # 나누기 -> float 타입
            rank = 0
            
            students.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg, "rank":rank})
            print("-"*30)
            print()
            print(f"{name} 학생성적이 등록되었습니다.")
            print()
            
            count += 1
            
            # for 문
            # score = [0]*3 #kor,eng,math
            # for i in range(3):
            #     score[i] = int(input(f"{title[i+2]}점수를 입력하세요."))
            
        
    elif choice == 2:
        print()
        print(" "*20,end="")
        print("[ 학생성적출력 ]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".foramat(*title))
        print("-"*60)
    
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}\t")
        print()
            
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break
