# 파일입출력 : 파일열기 - 파일읽기, 파일쓰기 - 파일닫기
# 파일열기 - 3가지 모드 : r 읽기 모드, w 쓰기모드, a 추가모드

# f = open("a.txt","r") # 읽기
# f = open("a.txt","w") # 쓰기
# f = open("a.txt","a") # 추가

# 파일 읽기 - r 1줄 읽기
# f = open("a.txt","r", encoding="utf-8")
# print(type(f))
# print(type(f))
# for line in f:
#     print(line.strip())
# f.close()

# 파일읽기 - readlines(): 모두 읽어오기
# f = open("a.txt","r", encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     print(line.strip())
# f.close()

# 파일 읽어오기 - 절대경로
# f=open("C:/workspace/smu_python/a.txt","r",encoding="utf-8")
# f=open("py0404/b.txt","r",encoding="utf-8")
# for line in f:
#     print(line.strip())
# f.close()

# while True:
#     line = f.readline()
#     if not line: break
#     print(line.strip())
# f.close

# f=open("py0404/news.txt","r",encoding="utf-8")

# for line in f:
#     print(line.strip())
# f.close