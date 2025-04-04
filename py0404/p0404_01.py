# def add(a,b):
#     return a+b

# print(add(10,20))

# def fun(a,b,c):
#     return max(a,b,c)

# print(max(10,5,20))

# 람다식 lamda -> 함수 축약형
# def 함수명 (매개변수) : return 값
# def func2(a):
#     return a*20

# lambda 매개변수:값
# lambda a:a*20

# def func(x):
#     return x**2

# a_list=[1,2,3,4,5] # list 모든 값에 제곱을 해서 리스트를 생성
# aa_list=[]
# for i in a_list:
#     aa_list.append(1**2)

# map(함수, 리스트)
# 리스트에 함수를 적용ㅎㅑ소 다시 함수상태로 변환
# print(list(map(func, aa_list)))

# 람다식
# print(list(map(lambda x:x**2,a_list)))

# filter() 함수 :  리스트에 함수르렂ㄱ요해서 ㅈ고ㅓㄴ에 맞는 것만 다시 스트로 자겅
# a_list=[1,2,3,4,5]
# aa_list=[]
# for i in a_list:
#     if i %2==0:
#         aa_list.append[i]
#     print(aa_list)
    
# filter 함수 사용
# def func(x):
#     if x%2==0:
#         return x
    
# b_lsit = list(filter(func,a_list))
# print(b_lsit)

# c_list = list(filter(lambda x:x%2==0,a_list))

# 리스트 sort() 정렬됨
# a_list = [20,50,10,40,90]
# a_list.sort() # 순차정렬
# print(a_list)
# a_list.sort(reverse=True)
# print(a_list)

students = [
    {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100.0,"rank":1},
    {"no":2,"name":"유관순","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
    {"no":3,"name":"이순신","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":2},
]

# dict 타입은 sort() 함수를 사용할수 없음
# students.sort()
# print(sort)

# print(students)
# print("-"*60)
# students.sort(key=lambda x:x['name']) # 이름으로 순차정렬
# print(students)
# students.sort(key=lambda x:x['name'], reverse=True) # 이름으로 역순 정렬
# print(students)

# print(students)
# print("-"*60)
# students.sort(key=lambda x:x['total'])
# print(students)
# print("-"*60)
# students.sort(key=lambda x:x['total'],reverse=True)
# print(students)

s_list = sorted(students,key=lambda x:x['name'])
print(s_list)
print("-"*60)
print(students)