# 문자열 다루기 기본
'''
문자열 s의 길이가 4 혹은 6이고, 숫자로만 되어있어야 함

try구문과 int함수를 이용해서 
에러가 발생하지 않으면 True
에러가 발생하면 False

입출력 예
s	return
a234	false
1234	true
'''


def solution(word):
    try:
        if len(word) == 4 or len(word) == 6:
            n = int(word)
            return True
    except:
        return False

    return False


word = "12"
res = solution(word)
print(res)


# 다른사람 코드
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)


# 함수 테스트
# False
print( alpha_string46("") )
print( alpha_string46("a") )
print( alpha_string46("a234") )
print( alpha_string46("1") )
print( alpha_string46("12345") )
print( alpha_string46("1234567") )

# True
print( alpha_string46("1234") )
print( alpha_string46("123456") )
