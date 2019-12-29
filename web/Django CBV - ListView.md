# Django CBV - ListView

## Class Based View - ListView

- 특정 DB table의 모든 record를 가져와서 List로 표시하기
- ex) 게시판 글 목록 전체

<br/>

- board/models.py
- app name = board

```python
# models.py
from django.db import models

class Paper(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    contents = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
```



<br/>

### FBV로 글 목록 만들기

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('listFBV/', views.listFBV),
]
```

```python
# views.py
from django.shortcuts import render
from .models import Paper

def listFBV(request):
    papers = Paper.objects.all()
    return render(request, 'board/index.html', {'papers':papers})
```

```html
<!-- board/templates/board/index.html -->
{% extends 'base.html' %}
{% block bodyblock %}

    <p>Function Based View - List</p>
    {{papers}}

{% endblock bodyblock %}
```



<br/>

### CBV로 글 목록 만들기

- 글 목록 전체를 표시하거나, 특정 DB table의 record 전체(혹은 일부)를 List로 표시할 때 활용할 수 있다.
- List가 테이블의 모든 레코드인 경우 모델 클래스만 지정하면 된다.

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('listCBV/', views.listCBV.as_view()),
]
```

```python
# views.py
from django.views.generic import ListView
from .models import Paper

class listCBV(ListView):
    model = Paper
```

- ListView의 default 지정 속성
  - 컨텍스트 변수: object_list
  - 템플릿 파일: paper_list.html(모델명소문자_list.html)

```html
<!-- board/templates/board/paper_list.html -->
{% extends 'base.html' %}
{% block bodyblock %}

    <p>Class Based View - List</p>
    {{object_list}}

{% endblock bodyblock %}
```

<br/>

- Default 설정 변경

```python
# views.py
from django.views.generic import ListView
from .models import Paper

class listCBV(ListView):
    template_name = 'board/index.html'
    context_object_name = 'papers'
    model = Paper
```

디폴트로 설정된 템플릿과 컨텍스트 변수명을 변경 하여 사용 할 수 있다.

<br/>

- 컨텍스트 오버라이딩

```python
# views.py
from django.views.generic import ListView
from .models import Paper

class listCBV(ListView):
    def get_queryset(self):
        return Paper.objects.all()
```

디폴트 설정을 사용하면서 컨텍스트 오버라이딩을 할 경우 위와 같이 작성 할 수 있다.









<br/><br/>

--------------

### Reference

 https://docs.djangoproject.com/ko/2.2/topics/class-based-views/generic-display/ 

 https://www.slideshare.net/spinlai/django-class-based-views-for-beginners 

 https://wayhome25.github.io/django/2017/05/02/CBV/ 