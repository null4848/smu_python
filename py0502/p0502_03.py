### 학생성적프로그램에서 1명의 학생을 등록해보세요.

from stuConn import *

conn = connections()


name = input("이름을 입력하세요.>> ")
kor = int(input("국어 점수를 입력하세요.>> "))
eng = int(input("영어 점수를 입력하세요.>> "))
math = int(input("수학 점수를 입력하세요.>> "))
total = kor+eng+math
avg = total/3


query = "insert into stuscore values(stuscore_seq.nextval, :sname, :skor, :seng, :smath, :stotal, :savg, 0)"
cursor = conn.cursor()
cursor.execute(query, sname=name, skor=kor, seng=eng, smath=math, stotal=total, savg=avg)
conn.commit() 
conn.close()

