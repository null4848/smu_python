### 학생 성적 프로그램

count = 4
students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]
title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:   
    print("-"*40)
    print("학생 성적 프로그램")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 등수처리")
    print('5. 학생성적정렬')
    print("6. 학생성적삭제")
    print("7. 학생성적저장")
    print("0. 프로그램 종료")
    print("-"*40)

    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()

    if choice == 1:
        while True:
            print("-"*40)
            print(" "*10, end="")
            print(" [ 학생 성적 입력 ]")
            print("-"*40)
            
            no = count
            name = input(f"{no}번 학생의 이름을 입력하세요.>> ")
            kor = int(input("국어 점수를 입력하세요.>> "))
            eng = int(input("영어 점수를 입력하세요.>> "))
            math = int(input("수학 점수를 입력하세요.>> "))
            total = kor+eng+math
            avg = total/3
            rank = 1
            
            students.append({"no":no, "name":name, "kor":kor, "eng":eng, "math":math, "total":total, "avg":avg, "rank":rank})
            
            print()
            print(f"{no}번 {name} 학생의 성적이 입력되었습니다. ")
            print()

            count+=1
            
            break
                    
    elif choice == 2:
        print("-"*40)
        print(" "*10, end="")
        print(" [ 학생 성적 출력 ]")
        print("-"*40)
        
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        
        for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\t")
        print()
    
    elif choice == 3:
        print("-"*40)
        print(" "*10, end="")
        print(" [ 학생 성적 수정 ]")
        print("-"*40)
        
        name = input("성적을 수정하고 싶은 학생의 이름을 입력해주세요.>> ")
        
        temp = 0
        
        for s in students:
            if name == s['name']:
                temp = 1
                print(f"{name} 학생이 존재합니다.")
                print()
                print("1. 국어")
                print("2. 영어")
                print("3. 수학")
                print("-"*10)
        
                choice = int(input("수정하고 싶은 과목의 번호를 골라주세요.>> "))
                print()

                if choice == 1:
                    print(f"{name} 학생의 현재 국어 성적 : {s['kor']}")                    
                    s['kor'] = int(input("수정할 국어 성적 : "))
                    print(f"국어 성적이 {s['kor']}로 변경되었습니다.")
                    
                elif choice == 2:
                    print(f"{name} 학생의 현재 영어 성적 : {s['eng']}")                    
                    s['eng'] = int(input("수정할 영어 성적 : "))
                    print(f"영어 성적이 {s['eng']}로 변경되었습니다.")
                    
                elif choice == 3:
                    print(f"{name} 학생의 현재 수학 성적 : {s['math']}")                    
                    s['math'] = int(input("수정할 수학 성적 : "))
                    print(f"수학 성적이 {s['math']}로 변경되었습니다.")
                
                else:
                    print("잘못된 입력입니다.")
                    
                s['total'] = s['kor']+s['eng']+s['math']
                s['avg'] = s['total']/3
                print()
                print(f"{name} 학생의 성적이 수정되었습니다.")
                    
        if temp == 0:
            print(f"{name} 학생이 존재하지 않습니다. 다시 입력해주세요.")

    elif choice == 4:
        print("-"*40)
        print(" "*10, end="")
        print(" [ 등수 처리 ]")
        print("-"*40)
        
        for s in students:
            num = 1
            for ss in students:
                if s['total'] <ss['total']:
                    num+=1
            s['rank'] = num
        print("등수 처리가 완료되었습니다.")
        print()
            

    elif choice == 5:
        students2 = [*students] # 복사
        print("-"*40)
        print(" "*10, end="")
        print(" [ 학생 성적 정렬 ]")
        print("-"*40)
        print("1. 이름 순차정렬")
        print("2. 이름 역순정렬")
        print("3. 합계 순차정렬")
        print("4. 합계 역순정렬")
        print("5. 번호 순차정렬")
        print("6. 번호 역순정렬")
        print("0. 이전화면이동")
        print("-"*40)
        
        choice = int(input("원하는 정렬 번호를 입력해주세요.>> "))
        
        if choice == 1:
            students2.sort(key=lambda x:x['name'] )
        elif choice == 2:
            students2.sort(key=lambda x:x['name'], reverse=True)
        elif choice == 3:
            students2.sort(key=lambda x:x['total'])
        elif choice == 4:
            students2.sort(key=lambda x:x['total'], reverse=True)
        elif choice == 5:
            students2.sort(key=lambda x:x['no'])
        elif choice == 6:
            students2.sort(key=lambda x:x['no'], reverse=True)
        elif choice == 0:
            print("이전 화면으로 이동합니다.")
            
        print
        
    elif choice == 6:
        print("-"*40)
        print(" "*10, end="")
        print(" [ 학생 성적 삭제 ]")
        print("-"*40)
        
        name = input("삭제하고자 하는 학생의 이름을 입력해주세요.>> ")
        
        temp = 0
        
        for i,s in enumerate(students):
            if name == s['name']:
                temp = 1
                print(f"{name} 학생이 존재합니다.") 
                print()
                num = int(input("삭제하시겠습니까? 1.예 2.아니요.>>"))
                
                if num == 1:
                   del(students[i])
                   print(f"{name} 학생 성적을 삭제하였습니다.")
                   
                else:
                   print(f"{name} 학생 성적 삭제를 취소하였습니다.")
                break
               
        if temp == 0:
            print(f"{name} 학생을 찾지 못하였습니다. 다시 입력해주세요.")
        print()
                
    else:
        print(" [ 프로그램 종료 ]")
        break
        

        
        
        

        
        
        
        
        