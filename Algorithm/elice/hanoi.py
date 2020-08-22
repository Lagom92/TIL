# 하노이의 탑 - 재귀이용
'''
예를 들어 

2가 입력으로 들어왔다면
[ (1, 2), (1, 3), (2, 3)]

3이 입력으로 들어왔다면 
[ (1, 3), (1, 2), (3, 2), (1, 3), (2, 1), (2, 3), (1, 3)] 
'''

def hanoi(height) :
    result = []
    
    def move(height, begin, tmp, end):
    # 여기에 재귀 알고리즘을 구현 해 봅시다.
        if height:
        # 마지막 제외 원판을 모두 끝을 이용해서 중간으로
            move(height - 1, begin, end, tmp)
            result.append((begin, end))
            # 중간에 있는 원판을 모두 시작을 거쳐서 끝으로
            move(height - 1, tmp, begin, end)
            
    move(height, 1, 2, 3)
    
    return result


def main():
    print(hanoi(3))

if __name__ == "__main__":
    main()