# one-hot encoding



- 텍스트를 구별하기 위해서 번호를 매겨줌



- 단점

'강아지' 와 '멍멍이' 사이에 유사한 부분이나 다른점을 알수가 없음

그냥 '강아지'와 '멍멍이'는 전현 다른 단어임

단어의 의미나 개념의 차이를 벡터안에 담지 못함



즉, one-hot encoding은 어떤 단어가 서로 유사한 의미를 갖고 어떤 단어가 서로 다른 의미를 갖는지 알 수 없다.





## Word Embedding

단어 임베딩은 벡터 안에 단어의 의미를 포함 시키는 방법이다.



## Sparse와 Dense Representations



- 예를들어 강아지에 대한 모델을 만든다고 한다면 색, 크기, 모양, 길이 등과 같은 `속성`을 이용해서 강아지를 판별하는 모델을 만들 수 있을 것 이다. 



- 대상의 속성을 표현하는 방식을 feature representation이라 한다.



- 언어의 속성을 표현하는 방법에는 대표적으로 Sparse representation과 dense representation이 있다.



- sparse representation => one-hot encoding



- dense representation => word2vec





## Sparse representation



- one-hot encoding은 해당 속성이 가질 수 있는 모든 경우의 수를 각각 독립적인 차원으로 표현한다.



- 단어의 총 개수가 N이라면 이 속성이 가질 수 있는 경우의 수는 총 N개 이다.



- 예를들어 '강아지'라는 단어가 있다면 N차원의 벡터 중 '강아지'에 해당하는 요소만 1 이고 나머지는 전부 0인 것이다.



- one-hot encoding으로 만들어진 표현을 sparse representation이라고 한다.



- 벡터나 행렬이 sparse하다는 것은 벡터나 행렬의 값 중 대부분이 0이라는 의미이다.



- Sparse representation은 가장 단순하고 자주 사용되어온 오래된 방법이다.





## Dense representation



- 각각의 속성을 독립적인 차원으로 나타내지 않고 임의로 정한 개수의 차원으로 대응시켜 표현한다.



- 이렇게 대응시키는 것을 임베딩(embedding)이라고 하고 임베딩하는 방식은 머신 러닝을 통해 학습하게 된다.



- 예를들어 5차원일때, '강아지' 를 임베딩 한다면 [0.13, 0.23, - 0.34, 0.94, -0.22] 와 같이 나타내게 된다.



- 입베딩된 벡터는 모든 차원이 각각의 값을 가지고 있으므로 sparse하지 않는다. 그래서 sparse의 반대말인 dense를 사용해서 dense representation 표현이라고 부른다.



- Dense representation은 하나의 정보가 여러 차원에 나누어져서 표현되기 때문에 Distributed representation이라고도 불린다.



- Dense representation은 하나의 차원이 하나의 속성을 명시적으로 표현하는 것이 아니라 여러 차원들이 조합되어 나타내고자 하는 속성들을 표현한다.



- 여러 차원이 어떤 의미를 가지고 있는지는 알 수 없다. 하지만 '강아지'를 표현하는 벡터와 '댕댕이'를 표현하는 벡터가 얼마나 비슷한지 혹은 다른지를 알 수 있다.

   

- 이런 벡터의 값들을 학습하는 방법 중 하나가 word2vec 이다.



## Dense representation의 장점



1. 적은 양의 차원으로 대상을 표현할 수 있다.

sparse representation으로 대상을 표현하면 단어의 개수 만큼 차원이 필요하기 때문에 엄청 많은 차원이 필요하다. 그리고 그 벡터의 값은 대부분 0이다.



차원의 저주(curse of dimensionality)



보통 Dense representation으로 단어를 표현할때는 20 ~ 200차원 정도로 sparse representation에 비해 매우 적은 양의 차원을 사용하게 된다.



2. Generalization power(일반화 능력)을 갖고 있다.

'강아지'와 '댕댕이'가 서로 비슷한 벡터로 표현이 된다면, '강아지'에 대한 정보가 '댕댕이'에도 일반화 될 수 있다.



'강아지'라는 단어를 통해 배운 지식을 '댕댕이'라는 단어에 적용 할 수 있다.



## word2vec



단어 임베딩을 학습하는 알고리즘에는 GloVe, FastText 등이 있는데 가장 자주 쓰이고 유명한것으로 word2vec가 있다.



word2vec의 핵심 아이디어는 

유유상종

또는

You shall know a word by the company it keeps.   -언어학자 J.R Firth(1957)



빈칸이 하나 있는 어떠한 문장이 하나 있다고 해보자.

우리는 일반적으로 빈칸의 앞 또는 뒤를 보고 그 빈칸에 어떤 단어가 들어갈지 예측을 할 수 있을것이다.



예측이 되는 단어들에게 비슷한 벡터들을 주는것이 word2vec의 predictive method 방식이다.



word2vec은 비지도학습 알고리즘으로 어떤 단어와 어떤단어가 비슷한지 알려주지 않아도 알아서 찾을 수 있다.



- word2vec에는 두가지 방식이 있다.



### CBOW(Continuous Bag of Words) 방식



### Skip-Gram 방식







# word2vec 사용



```
pip install gensim
```





- 여기서 Word2Vec의 하이퍼파라미터값은 다음과 같습니다.

**size** = 워드 벡터의 특징 값. 즉, 임베딩 된 벡터의 차원.
**window** = 컨텍스트 윈도우 크기
**min_count** = 단어 최소 빈도 수 제한 (빈도가 적은 단어들은 학습하지 않는다.)
**workers** = 학습을 위한 프로세스 수
**sg** = 0은 CBOW, 1은 Skip-gram.













---------

참고

https://dreamgonfly.github.io/machine/learning,/natural/language/processing/2017/08/16/word2vec_explained.html



https://wikidocs.net/33520



https://pythonkim.tistory.com/92





