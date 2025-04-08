class Student:
    
    phone = ""
    address = ""
    count = 1
    
    def __init__(self,name,kor,eng,math):
        self.no = Student.count
        Student.count += 1
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = self.total/3
        self.rank = 0
        
    def s_total(self):
        self.total = self.kor+self.eng+self.math
        
    def s_avg(self):
        self.avg = self.total/3
        
    def s_print(self):
        print(self.no,self.name,self.kor,self.eng,self.math,self.total,self.avg,self.rank)
        
# 객체선언  변수 = 생성자호출
# no 번호를 부여하지 않음
s = Student("홍길동",100,100,99)
s.s_print()
s2 = Student("유관순",90,90,91)
s2.s_print()


s.kor = 50
s.s_total()
s.s_avg()
s.s_print()
