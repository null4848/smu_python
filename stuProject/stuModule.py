class Student:
    # 인스턴스 변수 - 객체선언할때 각각 변수들이 존재 : 공용으로 사용안됨
    # no = 1
    # name = "" # 인스턴스 변수
    count = 1 # 클래스 변수
    
    # 생성자 함수
    def __init__(self,name,kor,eng,math):
        self.no = Student.count
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = (kor+eng+math)/3
        self.rank = 0
        Student.count += 1  
        
    def stu_total(self):
        self.total = self.kor+self.eng+self.math
    def stu_avg(self):
        self.avg = self.kor+self.eng+self.math/3
        
    def __str__(self):
        return f"""{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"""

class Students:
    def __init__(self):
        self.students = []
        
    def add(self,s):
        self.students.append(s)
        
    def __str__(self):    
        for s in self.students:
            print("s.no,s.name,s.kor,s.eng,s.math,s.total,s.avg,s.rank")
        return ""
        