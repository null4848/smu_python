print(" " * 20, end = "")
print("[ 학생성적 입력 ]")
count = 1

while True:
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("5. 학생성적정렬")
    print("6. 학생성적검색")
    print("7. 학생성적종료")
    print("0. 프로그램 종료")

    print("-"*30)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    print()
    
    no = 1
    if choice == 1:
        print("[ 학생 성적 입력 ]")
        
        students = list()

        name = input("이름을 입력하세요.>> ")
        kor = int(input("국어점수를 입력하세요.>> "))
        eng = int(input("영어점수를 입력하세요.>> "))
        math = int(input("수학점수를 입력하세요.>> "))
        total = kor+eng+math
        avg = total/3
        rank = 0
        student = [no,name,kor,eng,math,total,avg,rank]
        students.append(student)
        
    if choice == 2:
        print("[ 학생 성적 출력 ]")
        
        print("             [ 학생 성적 프로그램 ]")
        print("-"*65)
        print("번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수")
        print("-"*65)
        for stu in students:
            for i,s in enumerate(stu):
                if i != 6:
                    print(s,end="\t")
                else: # 평균일때
                    print(f"{s:.2f}", end="\t")
            print()
            
    if choice == 3:
        print("[ 학생 성적 수정 ]")
        name = input("학생 이름을 입력해주세요.>> ")
        
        if students[1] == name:
            kor = int(input("국어점수를 입력하세요.>> "))
            eng = int(input("영어점수를 입력하세요.>> "))
            math = int(input("수학점수를 입력하세요.>> "))
            students[2] = kor, 
            students[3] = eng, 
            students[4] = math

                
        print()
        
    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break

    
    