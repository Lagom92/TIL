# Serializer

- queryset과 모델 인스턴스와 같은 복잡한 데이터를 json, xml 또는 다른 콘텐츠 유형으로 쉽게 변환할 수 있다.
- 받은 데이터의 유효성을 검사한 다음, 복잡한 타입으로 형 변환할 수 있도록 serializeation을 제공한다.

<br/>

- API 통신의 데이터 타입은 주로 JSON으로 한다.
- 하지만, Django에서 Model 데이터는 보통 Queryset 이라는 복잡한 타입으로 되어 있다.
- 이런 타입을 JSON으로 바꾸기 위해선, 파이썬 네이티브타입으로 변환해주는 직렬화(Serializer)라는 작업이 필요하다.

<br/>

- Django가 Form 과 ModelForm 클래스를 제공하는것 처럼 REST Framework도 Serializer 와 ModelSerializer를 제공한다.
- 

<br/>

- serializers.py

```python
from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


```



- MovieSerializer 클래스 사용

```
movie = Movie.objects.get(pk=1)
serializer = MovieSerializer(movie)
serializer.data
```

모델 인스턴스를 파이썬 내부 데이터 타입으로 출력



```
from rest_framework.renders import JSONRenderer

json = JSONRenderer().render(serializer.data)
json
```

JSON으로 출력





--ing