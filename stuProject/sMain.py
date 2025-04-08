# 1. sModule.py - class 2개
# 2. sMain.py
# - sModule.py 사용해서 프로그램 구현
# 3. sFunc.py 함수를 옮겨봄.

from sModule import Student,Students
from sFunc import *


while True:
    choice = tmenu_print()
    if choice == 1:
        stu_input()
    elif choice == 2:
        stu_output()
