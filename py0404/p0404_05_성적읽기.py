# with 함수 사용시 f.close() 생략

# with open("py0404/stu.txt","r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

# 모든 학생 영어점수에 +2을 하시오
# aStr = "1,홍길동,100,99,199"
# a_list = aStr.split(",")

# f=open("py0404/stu2.txt","r",encoding="utf-8")
# line = f.readline()
# a_list = line.split(",")
# print(a_list)
# print(int(a_list[3])+1)
# f.close()

# while True:
#     line = f.readline()
#     if not line: break
#     a_list = line.split(",")
# print(a_list)
# print(int(a_list[3] )+ 1)

#stu.txt-> 영어성적 1증가 합계 1증가
# 전체리스트 추력
# 1, 홍길동, 100, 99, 199
# 2, 유관순, 90, 90, 180
# 3, 이순신, 80, 81, 161
students = []
f = open("py0404/stu.txt","r",encoding="utf-8")
while True:
    line = f.readline()
    if not line: break
    print(line.strip())
    s = line.strip().split(",")
    
    print("변경 영어 : ", int(s[3])+1)
    print("변경 합계 : ", int(s[4])+1)
    
    # list 수정
    s[0] = int(s[0])
    s[2] = int(s[2])
    s[3] = int(s[3])+1
    s[4] = int(s[4])+1
    print("{},{},{},{},{}".format(*s))
    students.append({"no":int(s[0]),"name":s[1],"kor":int(s[2]),"eng":int(s[3])+1,"total":int(s[4])+1})
f.close()

for ss in students:
    print(ss)

print(students)