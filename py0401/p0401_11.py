students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":1},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":67.0,"rank":1},
]

count = 4
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    print(" "*15, end="")
    print("[ 학생성적 프로그램 ]")
    print("-"*50)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("-"*50)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()


    if choice == 1:
        while True:
            no = count
            print(" "*15, end="")
            print("[ 학생성적입력 ]")
            print("-"*50)
            name = input("학생 이름을 입력하세요.(0.이전화면 이동)>> ")
            if name == '0':
                print("이전화면으로 이동합니다.")
                break
            kor = int(input("국어점수를 입력하세요.>> "))
            eng = int(input("영어점수를 입력하세요.>> "))
            math = int(input("수학점수를 입력하세요.>> "))
            total = kor+eng+math
            avg = total/3
            rank = 1
            print("-"*50)
            students.append({"no":no, "name":name,"kor":kor, "eng":eng, "math":math, "avg":avg, "total":total, "rank":rank})
            print(f"{name} 학생성적이 등록되었습니다.")
            print()
            
            count += 1
            break
            
        
    if choice == 2:
        print(" "*15, end="")
        print("[ 학생성적출력 ]")
        print("-"*50)
        
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        print("-"*50)

        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}\t")
        print()
