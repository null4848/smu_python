# 이름, 국어, 영어, 수학 입력받아 합계, 평균 출력하시오
# 이름 : 홍길동
# 합계 : 300 
# 평균 : 100.0 소수점은 1자리까지 출력하시오.

# name = input("이름을 입력하시오 : ")
# print("이름 : ",name)

# kor = int(input("국어 성적을 입력하시오 : "))
# eng = int(input("영어 성적을 입력하시오 : "))
# math = int(input("수학 성적을 입력하시오 : "))
# sci = int(input("과학 성적을 입력하시오 : "))


# total = kor+eng+math+sci
# avg = total/4

# print("국어 : ",kor)
# print("영어 : ",eng)
# print("수학 : ",math)
# print("과학 : ",sci)
# print("합계 : ",total)
# print("평균 : %.1f" % avg)

# 프린트 시 \n : 엔터키, \t : tab 키
# print("안녕하세요.\n반갑습니다.\t 저는 홍길동이라고 합니다.")

# format() 문자 형태 지정
a = 10
b = 3
print("%d / %d = %.2f" % (a,b,a/b))
str_print = "{} / {} = {:.2f}".format(a,b,a/b)
print(str_print)