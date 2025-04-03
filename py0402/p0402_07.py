
def cal(*a,b=10): # 가변 매개변수, 키워드 매개변수 함께 사용 
    result = b
    for i in a:
        result += i
    return result

print(cal(1,2,b=100))

# 키워드 매개변수
# def cal(a,b=10):
#     return a+b

# print(cal(1))

# print()함수는 매개변수가 가변매개변수임.
# print(1,2,3,4,5)
# print(1,2)

# 가변매개변수 사용
# def cal(*num):
#     result = 0
#     for n in num:
#         result += n
#     return result

# print("2개 합계 :", cal(1,2))
# print("3개 합계 :", cal(10,20,30))
# print("4개 합계 :", cal(20,40,60,80))


# def cal(n1,n2):
#     return n1+n2
# def cal2(n1,n2,n3):
#     return n1+n2+n3
# def cal3(n1,n2,n3,n4):
#     return n1+n2+n3+n4

# n1 = 10
# n2 = 20
# n3 = 30
# n4 = 40

# cal(n1,n2)
# cal2(n1,n2,n3)
# cal3(n1,n2,n3,n4)