# set -> 중복을 제거해서 키를 확인
# myset1 = {1,2,2,3,3,3,5,5,7}
# print(myset1)

# menu_list = ['삼각김밥','바나나','삼각김밥','사과','도시락','삼각김밥']
# print(set(menu_list)) # 리스트 타입을 set 타입으로 변경해서 확인

# -------------------------------------------------------

# 
# list = [1,2,3,4,5]
# list2 = [101,102,103,104,105]
# list2 = [i+100 for i in list] # 리스트 내포
# print(list2)

# format 함수 천단위 표시
# list3 = ['10,100, '10,200', '10,300', '10,400', '10,500']
# list3 = ["{:,d}".format((i+100)*100) for i in list]
# print(list3)

# 리스트 내포 : if 조건절을 넣을수 잇음.
# n_list = [i for i in range(1,51) if i%3==0]
# print(n_list)

# 2개의 리스트를 1개로 묶음.
n_list = ['홍길동','유관순','이순신','강감찬','김구']
t_list = [100,99,89,79,100]
a_list = [10.0,9,0,8.0,7.0,10.0]
# for n, t in zip(n_list, t_list):
#     print(f"{n} : {t}")
    
# students = {"no":1, "name":"홍길동", "kor":100}
# for key,value in students.items():
    # print(f"{key} : {Value}")

# for key,value in enumerate(students):
    # print(f"{key} : {Value}")

# tuple_list = list(zip(n_list, t_list))
print(list(zip(n_list, t_list))) # 3개 이상 가능
print(dict(zip(n_list,t_list))) # 불가능 
