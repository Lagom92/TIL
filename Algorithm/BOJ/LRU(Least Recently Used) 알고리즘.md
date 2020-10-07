

#  LRU(Least Recently Used) 알고리즘

<br/>

- 페이지 교체 알고리즘 중 하나
- 캐시에서 메모리를 다루기 위해 사용되는 알고리즘
- 한정된 메모리 공간 안에서 효율적인 사용을 하기 위해서 사용
- 가장 최근에 사용된 적이 없는 캐시의 메모리부터 새로운 데이터로 갱신시켜준다. 즉 가장 오랫동안 사용하지 않은것을 제거하는 알고리즘
- 이는 오래동안 사용 되지 않은 것은 앞으로도 사용될 가능성이 낮다고 보는것이다.



<br/>

**Cache Hit**

CPU가 참조하고자 하는 메모리가 캐시에 존재하고 있을 경우



<br/>

**Cache Miss**

CPU가 참조하고자 하는 메모리가 캐시에 존재하지 않은 경우



<br/>

![LRU 알고리즘](https://t1.daumcdn.net/cfile/tistory/998933375C7F78A428)





<br/><br/>

### 문제 추천

[프로그래머스_[1차] 캐시](https://programmers.co.kr/learn/courses/30/lessons/17680)

<br/>

**Python Code**

```python
def solution(cacheSize, cities):
    res = 0
    arr = [' '] * cacheSize
    
    for city in cities:
        city = city.lower()
        if city in arr:
            res += 1
            arr.remove(city)
            arr.append(city)
        else:
            res += 5
            arr.append(city)
            arr.pop(0)

    return res
```





<br/><br/>

-----------------------------

### Reference



- [페이지 교체 알고리즘 LRU blog](https://m.blog.naver.com/tlstjd436/221824813403)

- [[프로그래머스/Level2/파이썬3(python3)] [1차] 캐시 (2018 KAKAO BLIND RECRUITMENT)](https://this-programmer.com/entry/%EC%B9%B4%EC%B9%B4%EC%98%A42018%EB%B8%94%EB%9D%BC%EC%9D%B8%EB%93%9C-%EA%B3%B5%EC%B1%84%ED%8C%8C%EC%9D%B4%EC%8D%AC3python3-3-%EC%BA%90%EC%8B%9C)



<br/>



