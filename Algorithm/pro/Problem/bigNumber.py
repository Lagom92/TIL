# 가장 큰 수
'''
1's 시도
숫자들을 문자로 바꾼 후 sort reverse 한 후 join 한 결과를 리턴
=> 답이 틀리는 경우 발생함

2's 시도
itertools의 permutations 사용
=> 시간 초과가 발생함

3's 시도
숫자 두개를 뽑아서 하나로 만듦
합쳐진 숫자 두개중 큰것에 따라서 순서가 정해짐
=> 오답이 몇개 발생함, 이유 모르겠음, 나중에 수정!


입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"
'''


def solution(numbers):
    if sum(numbers) == 0:
        return "0"*len(numbers)
    
    while True:
        flag = True
        for i in range(len(numbers)-1):
            if len(str(numbers[i])) == len(str(numbers[i+1])):
                if numbers[i] < numbers[i+1]:
                    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                    flag = False

            else:
                a = str(numbers[i]) + str(numbers[i+1])
                b = str(numbers[i+1]) + str(numbers[i])

                if int(a) < int(b):
                    numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                    flag = False
        if flag:
            break
        
    return ''.join(map(str, numbers))

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))

# new_numbers = [5, 546]
# print(solution(new_numbers))



# 다른 사람 코드
'''
주어진 숫자들을 문자열로 변환
sort로 정렬하는데 key를 이용해 조건 설정
주어진 숫자를 세자리로 만들어 내림 차순으로 정렬

! 원리에 대한 이해가 좀 더 필요함
'''
def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


numbers = [233, 23]
print(solution2(numbers))
