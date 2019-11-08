# Django-debug-toolbar



>공부를 하던 중 웹의 성능에 있어서 데이터베이스가 많은 영향을 준다는 것을 봤다.
>
>SQL의 성능 및 처리 속도 최적화가 필요하다.
>
>
>
>그런데
>
>
>
>성능을 향상 시키려면 우선 현재 내가 어떤 상태인지 알아야 할 필요가 있다.
>
>
>
>그래서
>
>
>
>django-debug-toolbar를 활용해서 페이지 로딩 시 발생하는 쿼리의 수와 시간을 알아보자.
>
>







- Install

```
pip install django-debug-toolbar
```





- settings.py 에 내용 추가

```
INSTALLED_APPS = [
    
    ...
    'debug_toolbar',
]

# 미들웨어에 추가
MIDDLEWARE = [
    ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    ...
]

STATIC_URL = '/static/'

# 이 아이피에서만 디버그 툴바가 보인다.
INTERNAL_IPS = ('127.0.0.1',)
```





- urls.py

```
# from django.conf import settings
# from django.conf.urls import include, url

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] 
```





>???????????????
>
>
>
> 실행을 해보니 생각보다 쿼리를 많이 보내거나 하는것 같지는 않다.
>
>굳이 당장 SQL의 성능을 최적화 할 필요는 없어 보인다.





---

참고

https://django-debug-toolbar.readthedocs.io/en/stable/index.html

https://wayhome25.github.io/django/2017/06/20/selected_related_prefetch_related/

https://suspected.tistory.com/233

