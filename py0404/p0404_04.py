f=open("py0404/stu.txt","a",encoding="utf-8")
count = 1
no = count
name = input("이름을 입력하세요. >> ")
kor = int(input("국어점수를 입력하세요. >> "))
eng = int(input("영어점수를 입력하세요. >> "))
total = kor+eng
lines = f"{no},{name},{kor},{eng},{total}\n"
f.write(lines)
f.close()
print("학생성적이 저장되었습니다.")