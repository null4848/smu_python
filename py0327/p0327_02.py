## 달러를 입력하면, 원화 환산해서 출력하시오.
# 1 -> 1467원 환산
# 120 -> 120*1467

# money = int(input("달러를 입력하세요.>> "))
# won = money*1467
# # .2f = 소수점자리 출력, 천단위 출력 :,d
# print("입력한 달러 : {:,d} / 한화 : {:,d}".format(money,won))

# 1779원 -> 동전으로 변경을 하려고 합니다.
# 500원 3개, 100원 2개, 50원 1개, 10원 2개, 1원 9개
# money = int(input("동전으로 변경할 금액을 입력하시오.>> "))
# ch500 = money//500
# ch100 = (money%500)//100
# ch50 = ((money%500)%100)//50
# ch10 = (((money%500)%100)%50)//10
# ch1 = (((money%500)%100)%50)%10
# print("500원-{}개, 100원-{}개, 50원-{}개, 10원-{}개, 1원-{}개".format(ch500,ch100,ch50,ch10,ch1))

# 반지름을 입력받아, 원의 넓이를 구하는 프로그램을 구현하시오.
# len_input = int(input("원의 반지름을 입력하세요.>> "))

# 원의 넓이 : 3.14 x 반지름 x 반지름
# in_dim = 3.14 * (len_input ** 2)
# 원의 둘레 : 2 x 3.14 x 반지름
# in_circum = 2 * 3.14 * len_input

# 출력 : 원의 넓이 : 100 cm2 원의 둘레 : 50cm
# print("원의 넓이 {:.2f} cm2".format(in_dim))
# print("원의 둘레 {:.2f} cm".format(in_circum))

## 직사각형 가로, 세로 길이를 입력받아 넓이와 둘레를 구하시오.
rec1 = int(input("직사각형의 가로 길이를 입력하세요.>> "))
rec2 = int(input("직사각형의 세로 길이를 입력하세요.>> "))
result1 = rec1 * rec2
resutl2 = ((rec1 + rec2) * 2)
print("직사각형의 넓이 {} cm2".format(result1))
print("직사각형의 둘레 {} cm".format(resutl2))



