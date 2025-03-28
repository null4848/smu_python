print("안녕하세요.")
print("안녕하세요.")
print("안녕하세요.")

# range -> 1,2,3
for i in range(3):
    print("안녕하세요.")

# range -> 1,2,3 
# range(n,m) n이상 m미만
for i in range(1,4):
    print("안녕하세요.", i)
    
for i in range(1,3+1):
    print("안녕하세요.", i)
    
# range(n,m,o) 
# -> n부터 m-1까지 o만큼의 간격으로 출력
for i in range(1,11,5):
    print("안녕",i)
    
# range() 자리에 list 타입 가능
a_list = [1,2,3,4,5]
for i in a_list:
    print("안녕",i)