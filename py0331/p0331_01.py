a = 10
a_list = [1,2,3,4,5]

print("a : ",a)

a_list[0] = 100
print("a_list : ",a_list)

b = a
b = 1000
print("a : ", a) # 10
print("b : ", b) # 1000

# 새롭게 복사 : 깊은 복사
a_list = [1,2,3,4,5]
b_list = [*a_list] # 얕은 복사
b_list[1] = 200

print(a_list)
print(b_list)

# a_list = [1,2,3,4,5]
# sum = 0
# for i in a_list:
#     sum = sum + i

# 구구단
# for i in range(2,10):
#    for j in range(1,10):
#        print("[ {} 단 ]".format(i))
#        print("{} X {} = {}".format(i,j,i*j))
#    print()