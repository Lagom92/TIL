# 백준 10930번 SHA-256
# https://www.acmicpc.net/problem/10930
'''
문자열을 SHA-256으로 변환

hashlib를 이용함
'''


import hashlib

word = input()

result = hashlib.sha256(word.encode())

print(result.hexdigest())