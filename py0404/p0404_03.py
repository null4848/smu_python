# 파일쓰기 - w

# f=open("aa.txt","w",encoding="utf-8")
# f.write("안녕하세요.\r\n")
# f.write("반가워요\n")
# f.close()

# f = open("py0404/aaa.txt","w",encoding="utf-8")
# for i in range(10):
#     f.write(f"{i+1}. 안녕하세요.\r\n")
# print("글쓰기 종료")

# f = open("py0404/memo.txt","w",encoding="utf-8")
# print("[ 메모장 ]")
# print("-------")

# while True:
#     line = input("저장하려는 글자를 입력하세요.(x.종료 )>> ")
#     if line.lower() == "x":break
#     f.write(line)
# f.close

# 파일 이어쓰기 - a
f = open("py0404/memo2.txt","w",encoding="utf-8")
f.write("1,홍길동,100,100,99\n")
f.close()

f = open("py0404/memo2.txt","w",encoding="utf-8")
f.write("2,유관순,50,50,50\n")
f.close()

