# REST

### Representational State Transfer



### FBV로 CRUD 만들기

- 작업 순서

1. App생성

```
django-admin startapp <엡이름>
```



2. urls.py 파일 생성

   serializers.py 파일 생성



3. model.py에 모델 작성하기

```python
# models.py
from django.db import models

class Post(models.Model):
	contents = models.TextField()
```



4. serializers 작성하기

```python
# serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = '__all__'
			
```



5. views.py 작성하기

@api_view 데코레이터를 이용

```python
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

@api_view(['GET', 'POST'])
def post_list(request):
    # Read
    if request.method == 'GET':
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
    # Create
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
	# Detail
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    # Edit
    elif request.method == 'PUT':
        serializer = PostSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```



6. 테이블 생성

```
python mamage.py makemigrations
python manage.py migrate
```



7. url 맵핑하기

```python
# post/urls.py
from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list),
	paht('<int:pk>/', views.post_detail),
]
```



8. 프로젝트 폴더의 urls.py 작성하기

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	...
	path('post/', include('post.urls')),
]
```



9. 제대로 됬는지 확인!!

END



### ???이것은 무엇?

- status

```python
from rest_framework import status
```





- api_view

```python
from rest_framework.decorators import api_view
```



- Response

```python
from rest_framework.response import Response
```





### DRF

- DRF를 이용해 API를 만드는 방법들

FBV : 가장 자유도가 높다.

CBV : 재사용성에 초점을 맞춰 개발 할 수 있다.

viewSet : 쉽고 빠르게 API를 만들 수 있다.

mixin

generics













참고

https://inma.tistory.com/89