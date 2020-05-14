# 백준 1302번 베스트셀러
# https://www.acmicpc.net/problem/1302
'''
collections 모듈 사용
개수를 세어주는 Counter를 사용
데이터의 개수가 많은 순으로 정렬된 배열을 출력하는 most_common() 사용

추가 test case
2
a
ab
'''
from collections import Counter

n = int(input())
books = []
for _ in range(n):
    books.append(input())

books.sort()        # 문자열을 사전 순으로 정렬
cnt = Counter(books)

print(cnt.most_common(n=1)[0][0])   # 가장 많은 개수의 데이터의 key 출력



# 다른 사람 코드
# 딕셔너리 이용
n = int(input())

books = {}

for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

target = max(books.values())
array = []

for book, number in books.items():
    if number == target:
        array.append(book)

print(sorted(array)[0])