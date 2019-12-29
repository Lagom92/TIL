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



- `queryset`

기본 뷰(View, Template, RedirecView) 3개를 제외하고 모든 제네릭 뷰에서  사용한다.

queryset을 사용하면 model 속성은 무시된다.



- `template_name`

TemplateView를 포함한 모든 제네릭 뷰에서 사용한다.

템플릿 파일명을 문자열로 지정한다.



- `context_object_name`

뷰에서 템플릿 파일에 전달하는 컨텍스트 변수명을 지정한다.



- `paginate_by`

ListView와 날짜 기반 뷰(ex) YearArchiveView)에서 사용한다.

페이징 기능이 활성화 된 경우 페이지당 출력 항목 수를 정수로 지정한다.



- `date_field`

날짜 기반 뷰에서 사용한다.

이 필드의 타입은 DateField 또는 DateTimeField 이다.



- `form_class`

FormView, CreateView, UpdateView에서 폼을 만드는데 사용할 클래스를 지정한다.



- `success_url`

FormView, CreateView, UpdateView, DeleteView에서 폼에 대한 처리가 성공한 후 redirect 할 URL 주소이다.



### 메소드 오버라이딩

- `def get_queryset()`

기본 뷰(View, Template, RedirectView) 3개를 제외하고 모든 제네릭 뷰에서 사용한다.

디폴트는 `queryset` 속성을 반환한다.

`queryset` 속성이 지정되지 않은 경우 모델 매니저 클래스의 all() 메소드를 호출해 QuerySet 객체를 생성해 반환한다.



- `def get_context_data(**kwargs)`

뷰에서 템플릿 파일에 넘겨주는 컨텍스트 데이터를 추가하거나 변경하는 목적으로 오버라이딩한다.



- `def form_valid(form)`



### 모델을 지정하는 방법 3가지

- model 속성 변수 지정
- queryset 속성 변수 지정
- `def get_queryset()` 메소드 오버라이딩









-------

### Reference

 https://wikidocs.net/9623 



