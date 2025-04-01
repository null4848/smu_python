a_list = [1,2,3,"홍길동",4,5,6,7,8,9,10,11]

del a_list[0] # 인덱스 번호를 가지고 삭제
a_list.pop() # 마지막 데이터 삭제
a_list.pop(2) # 인덱스 번호 삭제
a_list.remove(2) # 2라는 값을 삭제
a_list.remove(8) # 11이라는 값을 삭제
a_list.clear # 모두 삭제

# ------------------------------

a_list.append(1) # 리스트 마지막에 1 추가
a_list.append(2)  # 리스트 마지막에 2 추가
a_list.insert(0,"홍길동") # 원하는 위치에 데이터
a_list.extend([10,11,12]) # 리스트 추가
print(a_list)

# ------------------------------

a_list[0] = "유관순"
print(a_list)

# ------------------------------

for a in a_list:
    print(a)

# ------------------------------

a_list.append(['컴퓨터공학','소프트웨어공학','무역학과'])
print(a_list)

# ------------------------------

print(len(a_list))

# ------------------------------

s_list = [1,2,3,1,2,2,2,1,3,4,5,7,7,7,10,9,8]
print("{} : {}".format(1, s_list.count(1)))

num = 0
for s in s_list:
    if s==1:
        num+=1
print("{} : {}".format(1,num))

s_list.sort() # 순차정렬, 낮은정렬
print(s_list)

s_list.sort(reverse=True) # 역순정렬, 높은순정렬
s_list.reverse() # 역순정렬, 높은순정렬
print(s_list)