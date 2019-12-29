# Django CBV - 오버라이딩

### 클래스형 뷰(CBV)

상속과 믹스인 기능을 이용하여 코드를 재사용하고 뷰를 체계적으로 구성할 수 있다.



<br/>

### Generic Display View(제네릭 보기 뷰)

객체의 목록 또는 하나의 객체 상세 정보를 보여주는 뷰

- ListView : 조건에 맞는 객체 목록 출력

- DetailView : 조건에 맞는 하나의 객체를 출력



<br/>

## Generic View 오버라이딩

### 속성 변수 오버라이딩

- `model`

기본 뷰(View, Template, RedirecView) 3개를 제외하고 모든 제네릭 뷰에서  사용한다.

뷰가 출력할 데이터가 들어 있는 모델 지정



- `queryset`

기본 뷰(View, Template, RedirecView) 3개를 제외하고 모든 제네릭 뷰에서  사용한다.

출력 대상이 되는 QuerySet 객체를 지정

queryset을 사용하면 model 속성은 무시된다.



- `template_name`

TemplateView를 포함한 모든 제네릭 뷰에서 사용한다.

템플릿 파일명을 문자열로 지정한다.



- `context_object_name`

기본 뷰를 제외하고는 모든 제네릭 뷰에서 사용한다.

뷰에서 템플릿 파일에 전달하는 컨텍스트 변수명을 지정한다.



- `paginate_by`

ListView와 날짜 기반 뷰(ex) YearArchiveView)에서 사용한다.

페이징 기능이 활성화 된 경우 페이지당 출력 항목 수를 정수로 지정한다.



- `date_field`

날짜 기반 뷰에서 사용한다.

이 필드를 기준으로 연/월/일을 검사한다.

이 필드의 타입은 DateField 또는 DateTimeField 이어야 한다.



- `form_class`

FormView, CreateView, UpdateView에서 폼을 만드는데 사용할 클래스를 지정한다.



- `success_url`

FormView, CreateView, UpdateView, DeleteView에서 폼에 대한 처리가 성공한 후 redirect 할 URL 주소이다.



- `make_object_list`

YearArchiveView 사용 시 해당 년에 맞는 객체들의 리스트 생성 여부를 지정한다.

True 이면 객체들의 리스트를 만들고 템플릿에서 사용할 수 있다.

False 이면 queryset 속성에 None이 할당 된다.



- `initial`

FormView, CreateView, UpdateView에서 사용한다.

폼에 사용할 초기 데이터를 딕셔너리로 지정한다.



- `fields`

CreateView, UpdateView에서 사용한다.

폼에 사용할 필드를 지정한다.

ModelForm 클래스의 Meta.fields 속성과 동일한 의미이다.



### 메소드 오버라이딩

- `def get_queryset()`

기본 뷰(View, Template, RedirectView) 3개를 제외하고 모든 제네릭 뷰에서 사용한다.

출력 객체를 검색하기 위한 대상 QuerySet 객체 또는 출력 대상인 객체 리스트를 반환한다.

디폴트는 `queryset` 속성을 반환한다.

`queryset` 속성이 지정되지 않은 경우 모델 매니저 클래스의 all() 메소드를 호출해 QuerySet 객체를 생성해 반환한다.



- `def get_context_data(**kwargs)`

모든 제네릭 뷰에서 사용

템플릿에서 사용할 컨텍스트 데이터를 반환

뷰에서 템플릿 파일에 넘겨주는 컨텍스트 데이터를 추가하거나 변경하는 목적으로 오버라이딩한다.



- `def form_valid(form)`

FormView, CreateView, UpdateView 에서 사용

get_success_url 메소드가 반환하는 URL로 리다이렉트를 수행



### 모델을 지정하는 방법 3가지

- model 속성 변수 지정
- queryset 속성 변수 지정
- `def get_queryset()` 메소드 오버라이딩









-------

### Reference

 https://wikidocs.net/9623 



