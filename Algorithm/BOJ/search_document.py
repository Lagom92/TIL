# 백준 1543번 문서 검색
# https://www.acmicpc.net/problem/1543
'''
문자열 documents 가 있을 때, 문자열 word 가 몇 개 있는지 출력

split() 함수를 사용
문자열을 구간 단위로 만든다는 개념으로 알고리즘을 구현함
'''

documents = input()
word = input()
cnt = 0

documents_list = list(documents.split(word))

print(len(documents_list)-1)




# 다른 사람 코드
'''
문서에서 단어가 있는지 앞에서 부터 차례대로 검사

문서의 남은 길이가 단어의 길이보다 작으면 멈춤
해당 단어가 찾는 단어일 경우 단어의 길이 만큼 인덱스를 이동
해당 단어가 찾는 단어가 아닐 경우 앞으로 한칸 이동
'''
document = input()
word = input()

index = 0
result = 0

while len(document) - index >= len(word):
    if document[index:index+len(word)] == word:
        result += 1
        index += len(word)
    else:
        index += 1

print(result)