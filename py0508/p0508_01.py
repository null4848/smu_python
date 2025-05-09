from pyFunc import *

conn = connections()


## db 연결
while True:
    print("[ 학생성적 프로그램 ]")
    print("1. 학생전체 출력")
    print("2. 학반별 최고등수 출력")
    print("3. 학반별 최하등수 출력")
    print("4. 부서별 최고연봉 출력")
    print("5. stuscore2 학반 부여 (1,10 - 1... )")
    print("6. 회원정보 rownum을 사용, 11-20번 출력")
    print("-"*20)
    choice = int(input("원하는 번호를 입력하세요.>> "))
    
    if choice == 1:
        print("[ 학생전체 출력 ]")
        print("-"*20)

        cursor = conn.cursor()
        query = "select * from stuscore"
        cursor.execute(query)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        print()
            
        
    elif choice == 2:
        print("[ 학반별 최고등수 출력 ]")
    elif choice == 3:
        print("[ 학반별 최하등수 출력 ]")
    elif choice == 4:
        print("[ 부서별 최고연봉 출력 ]")
    elif choice == 5:
        cursor = conn.cursor()
        print("[ stuscore2 학반 부여 (1,10 - 1... ) ]")
        query = """ select sno, name, total, avg,
            case
            when sno between 1 and 10 then 1
            when sno between 11 and 20 then 2
            when sno between 21 and 30 then 3
            when sno between 31 and 40 then 4
            when sno between 41 and 50 then 5
            when sno between 51 and 60 then 6
            when sno between 61 and 70 then 7
            when sno between 71 and 80 then 8
            when sno between 81 and 90 then 9
            when sno between 91 and 100 then 10
            when sno between 101 and 110 then 11
            end as sclass
            from stuscore2"""
        cursor.execute(query)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        print()

    elif choice == 6:        
        cursor = conn.cursor()
        print("[ 회원정보 rownum을 사용, 11-20번 출력 ]")
        query = """select * from (
                select rownum rnum, a.* from member a)
                where rnum between 11 and 20"""
        cursor.execute(query)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
        print()
   