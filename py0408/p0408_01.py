title = ['번호','이름', '국어', '영어', '수학', '총합', '평균','등수']

while True:
    print("1. 국어입력")
    print("2. 영어입력")
    print("3. 수학입력")
    choice = int(input("원하는 번호를 입력하세요.>> "))
    
    if choice == 1:
        print("[ 국어성적입력 ]")
    elif choice == 2:
        print("[ 영어성적입력 ]")
    else:
        print("[ 수학성적입력 ")