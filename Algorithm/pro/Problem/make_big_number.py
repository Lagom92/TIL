# 큰 수 만들기
'''
앞 자리 숫자가 커야 큰 숫자이다.

문자열도 비교할 수 있다.(ex) '1' < '3')


입출력 예
number	k	return
1924	2	94
1231234	3	3234
4177252841	4	775841

hidden testcase
number = "1111"
K = 2
'''

'''
1's code
testcase 8 & 10 fail
'''
def solution1(number, k):
    box = ""

    for n in number:
        box += n

        if k == 0:
            pass

        if len(box)>1:
            for _ in range(len(box)-1):
                if k == 0:
                    break
                if box[-2] < box[-1]:
                    box = box[:-2] + box[-1]
                    k -= 1
                
    if k != 0:
        n = len(box) - k
        box = box[:n]

    return ''.join(box)



'''
2's code

다른사람 코드를 보고 작성함
1's code와 개념은 비슷함
'''
def solution2(number, k):
    box = []

    for i, num in enumerate(number):
        while box and box[-1] < num and k > 0:
            box.pop()
            k -= 1

        if k == 0:
            box += number[i:]
            break
        
        box.append(num)

    if k > 0:
        box = box[:-k]

    return ''.join(box)



number = "1924"
K = 2

print(solution2(number, K))
