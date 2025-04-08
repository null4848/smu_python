from stuModule import Student

s1 = Student("홍길동",100,90,99)
s2 = Student("유관순",100,90,99)

print(s1) # class 객체에서 __str__

if s1 == s2:
    print("합계점수가 같습니다.")
else:
    print("합계점수가 다릅니다.")

