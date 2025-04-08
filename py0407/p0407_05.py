# 변수, 함수 집합체 - 변수에 대한 그룹핑 kor,eng,math
# list,dict 타입 - 함수까지, sum,avg,rank 함수
# 입력받을때 처리 수정할때 직접처리
# 특정데이터 값이 들어왔을때 잘못된 데이터는 입력이 안되도록 구현

# class 클래스명:
    # 이부분에 관련 코드 구현
    
# class Car:
#     color = "white"
#     speed = 0
#     tire = 4
#     door = 5
    
    # 속도올리기
    # def speedUp(self, s):
    #     self.speed += s 
    # def speedDown(self, s):
    #     self.speed -= s
    
class Car:
    def __init__(self,color,tire,door): # 생성자 __init__
        self.color = color # self.color : Car 변수, color : 요청변수
        self.tire = tire
        self.door = door
        self.spped = 0
    
    color = "white"
    speed = 0
    tire = 4
    door = 5
    

    def speedUp(self, s):
        self.speed += s 
    def speedDown(self, s):
        self.speed -= s

        
# 리스트 선언
# a_list = [1,2,3,4,5]
# 리스트 값 입력
# a_list[0]=50
# 리스트 출력
# print(a_list)

# 클래스 객체선언
# a = Car()
# 클래스 변수에 값 입력
# a.speed = 50 # 참조변수.변수명
# 클래스 변수 값 출력 - 참조변수.변수명
# print(a.speed)

# 함수 사용방법 - 참조변수.함수명
# a.speedUp(20)
# print(a.speed)

# a_list2 = [1,2,3,4,5]
# a_list2 = a_list # 얕은복사
# a_list2 = [*a_list] # 깊은복사

# a = Car() # 각각의 변수, 함수가 됨

# red,5,4

# 생성자를 사용한 객체 선언과 동시에 데이터 입력
C = Car("red",5,4)

# a2 = Car() # 차를 구매한후 색칠도 다시하고, 문짝도 달고, 타이어도 달고..
# a2.color = "red"
# a2.tire = 5
# a2.door = 4

# blue,5,5
# a3 = Car()
# a3.color = "blue"
# a3.tire = 5



