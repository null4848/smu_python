# import stu_func
# import stu_func as stu # 별칭사용
# from stu_func import stu_print, stu_input, stu_output # 각각의 함수명

from stu_func import *
import random

def stu_edit():
    print("[ 학생성적 수정 ]")
    name = input("수정하려고 하는 학생이름을 입력하세요.>> ")
    temp = 0 # 찾지 못했을 경우
    for s in students:
        if s['name'] == name:
            temp = 1
            print(f"{name} 학생을 찾았습니다. 과목을 수정합니다.")
            print()
            print("[ 수정과목 선택 ]")
            print("1. 국어")
            print("2. 영어")
            print("3. 수학")
            print("-"*10)
            choice = int(input("원하는 번호를 입력하세요.>> "))
            sub_list = ['','kor','eng','math']
            if choice == 1:
                pre_score = s[sub_list[choice]]
                print(f"현재 {title[choice+1]} : {pre_score}")
                s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]}점수 입력 : "))
                s['total'] = s['kor'] + s['eng'] + s['math']
                s['avg'] = s['total']/3
                print(f"변경전 : {pre_score}점을 {s[sub_list[choice]]}점으로 변경하였습니다.")
                print()
            elif choice == 2:
                pre_score = s[sub_list[choice]]
                print(f"현재 {title[choice+1]} : {pre_score}")
                s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]}점수 입력 : "))
                s['total'] = s['kor'] + s['eng'] + s['math']
                s['avg'] = s['total']/3
                print(f"변경전 : {pre_score}점을 {s[sub_list[choice]]}점으로 변경하였습니다.")
                print()
            elif choice == 3:
                pre_score = s[sub_list[choice]]
                print(f"현재 {title[choice+1]} : {pre_score}")
                s[sub_list[choice]] = int(input(f"수정할 {title[choice+1]}점수 입력 : "))
                s['total'] = s['kor'] + s['eng'] + s['math']
                s['avg'] = s['total']/3
                print(f"변경전 : {pre_score}점을 {s[sub_list[choice]]}점으로 변경하였습니다.")
                print()
    if temp == 0:
        print("학생을 찾지 못하였습니다. 다시 실행하세요! ")
    print()
            
students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]

count = 4
title = ['번호','이름','국어','영어','수학','합계','평균','등수']
choice = 0


while True:
    # 화면 출력 부분
    choice = stu_print()
    
    if choice == 1: # 학생성적입력부분
        count = stu_input(count,students)
    elif choice == 2: # 학생성적출력부분
        stu_output(title, students)
    elif choice == 3: # 학생성적수정부분
        stu_edit()        
    elif choice == 4: # 등수처리
        stu_rank(students)

    elif choice == 0:
        print("[ 프로그램 종료 ]")
        break
    