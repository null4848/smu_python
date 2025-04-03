# txt = "파이썬 공부가쉬워요~ 너무 쉬워요. 파이썬은 재미있어요."
# a_list = [1,2,3,4,5]

# 문자열 인덱스 번호를 가짐 
# print(txt[1])
# print(a_list[1])

# print(a_list[1:3])
# print(txt[1:3])
# print(txt[2:])
# print(txt[:3])

# print(txt*3)
# print("-"*50)
# print(len(txt)) # 글자길이

# print(txt[::-1])

# print(txt.upper()) # 대문자 출력
# print(txt.lower()) # 소문자
# print(txt.swapcase()) # 대문자는 소문자로, 소문자는 대문자로
# print(txt.title()) # 단어 첫글자 대문자

# print(txt.count("파이썬")) # 문자열의 검색하려고하는 글자 개수
# print(txt.count("요")) 

# print(txt.find("공부"))

# txt = "   안녕하  세요   "
# print(txt)

# 공백제거
# print(txt.strip()) # 앞뒤 공백제거 - rstrip(), lstrip() 왼, 오 공백제거

# 다른문자로취환
# print(txt.replace(" ",""))

# txt2 = "파이썬 공부가쉬워요~ 너무 쉬워요. 파이썬은 재미있어요."
# print(txt2.replace("파이썬","자바"))

# 특정글자제거
# txt3 = "----파이---썬----"
# print(txt3.strip("-"))
# print(txt3.replace("-","")) 

# txt = "a,b,c,d,안녕,반가워"
# txt_list = txt.split(",")
# print(txt_list)

# 데이터베이스는 리스트를 저장할수 없음.
# txt="1,홍길동,100,100,100,300,100.0,1"
# txt_list = txt.split(",")
# print(txt_list)
# txt_list[1] = "유관순"
# print(txt_list)

txt = ","
txt2 = txt.join("안녕하세요")
print(txt2)

# map (함수, 데이터값)
score = ['100','99','90']
def cal(x):
    return int(x)*100

s_list = list(map(int,score))
print(s_list)

# sum = 0
# for s in score:
#     sum = sum + int(s) # 형변환 
# print("합계 :",sum)

# a = "1234"
# if a.isdigit(): # 숫자로 변환가능
#     print("숫자로 가능합니다.")
    
    
# my = int(input("숫자를 입력하세요.>> "))


# while True:
#     my_input = input("숫자를 입력하세요.>. ")
#     if my_input.isdigit():
#         my_input = int(my_input)
#     else:
#         print("숫자가 아닙니다. 숫자를 입력하셔야 합니다.")
        
print('1234'.isdigit()) # 숫자인지 확인
print('abc'.isalpha()) # 알파벳인지 확인
print('abc123'.isalnum()) # 글자 및 숫자인지 확인 abc, a1, 123 모두 가능
print('ABC'.islower()) # 모두 소문자인지 확인
print('abc'.isupper()) # 모두 대문자인지 확인


        
