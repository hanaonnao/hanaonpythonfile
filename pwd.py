import threading
from unrar import rarfile
import os
import itertools as its
import time
from concurrent.futures import ThreadPoolExecutor


def get_password(min_digits, max_digits, words): # 用於生成密碼
    while min_digits <= max_digits:
        pwds = its.product(words, repeat=min_digits)
        for pwd in pwds:
            yield ''.join(pwd)
    min_digits += 1

def extract(): # 用於嘗試破解密碼
    global flag
    flag = True # 用於線程的標識
    while flag:
        pwd = next(pwds)
        try:
            file = rarfile.RarFile(file_path,mode="r",pwd=pwd)
            print('\n=======================================\n'+'Find password is "{}"'.format(pwd)+'\n=======================================\n')
            flag = False
            break
        except:
            print(pwd)

def mainStep():# 用於線程設置
    for pwd in range(100):
        t = threading.Thread(target=extract)
        t.start()

if __name__ == '__main__':
    try:
        words = '0123456789'  # 密碼涉及的字符
        file_path = 'j:\\01.rar'# 檔案
        pwds = get_password(4, 4,words)# 用於確定密碼格式
        mainStep()
    except:
        pass
