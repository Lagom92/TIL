# KoNLPy



형태소

의미를 가지는 가장 작은 단위로서 더 쪼개면 의미를 상실한다.



형태소 분석

의미를 가지는 단위를 기준으로 문장을 확인하는것











- 형태소 분석기 마다 성능과 결과가 다르게 나온다. 그러므로 필요한 용도가 무엇인지에 따라서 적절한 형태소 분석기를 선택하여 사용해야 한다.



- 속도를 중시한다면 메캅을 사용 할 수 있다.



- 





## 형태소 분석기 목록

- Hannanum

  한나눔, KAIST Semantic Web Research Center 개발

  

- Kkma

  꼬꼬마, 서울대학교 IDS 연구실 개발

  

- Komoran

  코모란, Shineware에서 개발

  

- Mecab

  메카브, 일본어용 형태소 분석기를 한구어를 사용할 수 있도록 수정

  

- Open Korean Text

  OKt, 오픈 소스 한국어 분석기, 옛날 트위터 형태소 분석기(0.5.0버전 이후부터 변경됨)

  



  자소 분리나 오탈자에 대해서도 어느 정도 분석 품질이 보장되야 한다면 KOMORAN 사용을 고려

출처: https://iostream.tistory.com/144 [Almost Baseball, CSE and Diary]  









### Okt()













참고

http://konlpy.org/en/latest/api/konlpy.tag/



https://devtimes.com/bigdata/2019/04/18/konlpy/



https://iostream.tistory.com/144



---------





# 형태소 분석기를 변경하거나 옵션을 변경하여 정확도를 올려보자



- 

```
def tokenize(doc):
    okt = Okt()
    # norm은 정규화, stem은 근어로 표시하기를 나타냄
    return ['/'.join(t) for t in okt.pos(doc)]

# train_docs, test_docs : 토큰화된 트레이닝, 테스트  문장에 label 정보를 추가한 list
train_docs = [tokenize(row[1]) for row in train_data]
test_docs = [tokenize(row[1]) for row in test_data]
```

0.84



- 

```
def tokenize(doc):
    okt = Okt()
    # norm은 정규화, stem은 근어로 표시하기를 나타냄
    return ['/'.join(t) for t in okt.pos(doc)]

# train_docs, test_docs : 토큰화된 트레이닝, 테스트  문장에 label 정보를 추가한 list
train_docs = [tokenize(row[1]) for row in train_data]
test_docs = [tokenize(row[1]) for row in test_data]
```

0.85





## pyeunjeon



>  okt는 속도가 너무 느린것같다
>
> 형태소 분석기 중에서 속도가 빠른게 Mecab이라고 하는데 window에서는 사용이 않된다고 한다.
>
> 그래서 더 찾아보던 중 koshort라는 프로젝트에서 pyeunjeon 라는 것을 찾았다.
>
> 
>
> 실재로 실행해보니 속도가 매우 향상되었다.





```
pip install eunjeon
```



```
from eunjeon import Mecab
```



```
tagger = Mecab()

# 명사만 분류
tagger.nouns()

# 형태소 단위로 분류
tagger.morphs()

# 형태소 단위로 분류하고 형태소 마다 품사 분석
tagger.pos()
```



- ex)

```
from eunjeon import Mecab
tagger = Mecab()

tagger.pos("텍스트 데이터를 받아 형태소 분석기로 토크하자.")
```

```
[('텍스트', 'NNG'),
 ('데이터', 'NNG'),
 ('를', 'JKO'),
 ('받', 'VV'),
 ('아', 'EC'),
 ('형태소', 'NNG'),
 ('분석기', 'NNG'),
 ('로', 'JKB'),
 ('토크', 'NNG'),
 ('하', 'XSA'),
 ('자', 'EF'),
 ('.', 'SF')]
```













참고

https://m.blog.naver.com/PostView.nhn?blogId=aul-_-&logNo=221557243190&proxyReferer=https%3A%2F%2Fwww.google.com%2F