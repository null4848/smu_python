students = [
    [1,'홍길동', 100,100,100,300,100.0,1],
    [2,'유관순', 100,100,99,299,99.67,2],
    [3,'이순신', 100,100,99,299,99.67,2]
]

student = []
count = 4 # 학생번호를 생성
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
    # 화면 출력
    print("-"*30)
    print(" "*5, end="")
    print("[ 학생성적 프로그램 ]")
    print("-"*30)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("5. 학생성적정렬")
    print("6. 학생성적검색")
    print("7. 등수처리")
    print("0. 프로그램 종료")
    print("-"*30)
    
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    
    if choice == 1:
        print("[ 학생성적 입력 ]")
        no = count
        name = input("이름을 입력하세요.>> ")
        kor = int(input("국어점수를 입력하세요.>> "))
        eng = int(input("영어점수를 입력하세요.>> "))
        math = int(input("수학점수를 입력하세요.>> "))
        total = kor+eng+math
        avg = total/3
        rank = 1
        
        students.append([no,name,kor,eng,math,total,avg,rank])
        print(f"{no}번 {name} 학생성적이 등록되었습니다.")
        print()
        count += 1

    elif choice == 2:
        print("[ 학생성적 출력 ]")
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))

        for s in students:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*s))
        print()
        
    elif choice == 3:
        print("[ 학생성적 수정 ]")
        name = input("수정할 학생의 이름을 입력해주세요.>> ")
        
        for i,s in enumerate(students):
            temp = 0
            if name in s:
                temp = 1
                print(f"{name} 학생을 찾았습니다.")
                print()
            
                print("[ 수정하려는 과목 선택 ]")
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("0. 취소")
                print("-"*20)
                print()
                choice= int(input("성적을 수정할 과목의 번호를 입력하세요."))
                
                if choice == 1:
                    print("국어 성적 수정")
                    print(f"현재 국어 성적 : {s[2]}")
                    s[2] = int(input("변경할 국어 성적 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                    print(f"{name} 학생 성적이 수정되었습니다.")
                    break
                
                elif choice == 2:
                    print("영어 성적 수정")
                    print(f"현재 영어 성적 : {s[3]}")
                    s[3] = int(input("변경할 영어 성적 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                    print(f"{name} 학생 성적이 수정되었습니다.")
                    break
                
                elif choice == 3:
                    print("수학 성적 수정")
                    print(f"현재 수학 성적 : {s[4]}")
                    s[4] = int(input("변경할 수학 성적 : "))
                    s[5] = s[2]+s[3]+s[4]
                    s[6] = s[5]/3
                    print(f"{name} 학생 성적이 수정되었습니다.")
                    break
                
        if temp == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 실행하세요!")
        print()
            
                
    elif choice == 4:
        print("[ 학생성적 삭제 ]")
        name = input("삭제할 학생의 이름을 입력해주세요.>> ")
        
        for i,s in enumerate(students):
            temp = 0
            if name in s:
                temp = 1
                print(f"{name} 학생을 찾았습니다.")
                choice = int(input(f"{name} 학생의 성적을 삭제하시겠습니까? (0.아니요 1.예)"))
                if choice == 1:
                    print(f"{name} 학생의 성적을 삭제하였습니다.")
                    del students[i]
                else:
                    print(f"{name} 학생의 성적 삭제를 취소했습니다..")
                break
        
        if temp == 0:
            print(f"{name} 학생을 찾지 못했습니다. 다시 실행하세요!")
        print()

            
            
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break