# 구구단 출력
# for i in range (2,10):
#     print(" [ {} 단 ]".format(i))
#     for j in range(1,10):
#         print("{} X {} = {}".format(i,j,i*j))
#     print()

# 3,5,7,9 홀수단만 출력하시오.
# for i in range(3,10,2):
#     print(" [ {} 단 ]".format(i))
#     for j in range(1,10):
#         print("{} X {} = {}".format(i,j,i*j))
#     print()

# for i in range(2,10):
#     if i%2==1:
#         print(" [ {} 단 ]".format(i))
#         for j in range(1,10):
#             print("{} X {} = {}".format(i,j,i*j))
#         print()

# 시작단과 끝단을 입력받아, 출력하시오.
# num1 = int(input("시작단을 입력하세요.>> "))
# num2 = int(input("끝단을 입력하세요.>> "))

# for i in range(num1, num2+1):
#     print(" [ {} 단 ]".format(i))
#     for j in range(2,10):
#         print("{} X {} = {}".format(i,j,i*j))
#     print()

# 입력받은 시작단, 끝단 크기 비교
num1 = int(input("시작단을 입력하세요.>> "))
num2 = int(input("끝단을 입력하세요.>> "))

if num1>num2:
    num1,num2 = num2,num1

for i in range(num1, num2+1):
    print(" [ {} 단 ]".format(i))
    for j in range(2,10):
        print("{} X {} = {}".format(i,j,i*j))
    print()


# 두 수를 입력받아, 두 수 사이의 합계를 구하시오
# num1 = int(input("숫자를 입력하세요.>> "))
# num2 = int(input("숫자를 입력하세요.>> "))
# print(num1,num2)

# if num1>num2: 
#     t = num1
#     num1 = num2
#     num2 = t

# sum = 0
# for i in range(num1,num2+1):
#     sum = sum + num1
#     print("i : {}, sum : {}".format(i,sum))

        
# print("합계 :", sum)
# print("{}에서 {}까지의 합계 : {} ".format(num1, num2, sum))