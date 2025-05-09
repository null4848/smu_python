import oracledb
# db 연결
def connections():
    try: conn = oracledb.connect(user="ora_user", password="1111", dsn="localhost:1521/xe")
    except Exception as e: print(e)
    return conn

while True:
    print("[ 학생성적프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("0. 프로그램종료")
    print("-"*20)
    choice = int(input("원하는 번호를 입력하세요.>> "))