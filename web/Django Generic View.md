# Django Generic View

## Generic View

웹 프로그램 개발 시 공통적으로 사용되는 로직을 미리 개발해 놓은 기본 클래스

제네릭 뷰를 상속받아서 필요한 속성과 메소드를 오버라이딩하여 사용 할 수 있다.



<br/>

## Generic View's 종류

### Base View

- View

  - 가장 기본이 되는 최상위 Generic View

  - 다른 모든 Generic View들은 View의 하위 클래스

  - 모든 클래스형 뷰의 기본이 되는 최상위 뷰

  - 원하는 로직에 맞는 제네릭 뷰가 없는 경우 이 뷰를 상속받아서 새로 운 클래스형 뷰를 작성할 수도 있음



- TemplateView

  - 템플릿이 주어지면 해당 템플릿을 렌더링

  - 화면에 보여줄 템플릿 파일을 처리하는 정도의 간단한 뷰



- RedirectView

  - URL이 주어지면 해당 URL로 리다이렉트

  - 주어진 URL로 리다이렉트 시켜주는 제네릭 뷰

  - 만일 URL을 알 수 없다면, 410 error 응답 발생

  - 복잡한 로직 없이 리다이렉트만을 원할 때 사용



<br/>

### Generic Display View

- DetailView

  - 객체 하나에 대한 상세 정보를 보여줌

  - ListView와 함께 가장 많이 사용됨

  - 특정 객체 하나에 대한 상세 정보를 보여준다.

  - URLconf의 URL 정의를 이용하여 특정 테이블의 특정 컬럼 값을 기준으로 레코드를 찾을 수 있음

  - 즉, 테이블은 뷰 클래스에서 지정하고 레코드 검색용 키는 URLconf에서 지정

  - 레코드 검색용 키는 보통 기본키(pk) 사용



- ListView

  - 조건에 맞는 여러 객체를 보여줌

  - 자주 사용하는 제네릭 뷰

  - 여러 객체의 리스트를 보여줌

  - 테이블의 모든 레코드를 리스팅해줌



<br/>

### Generic Edit View

- FormView

  - 폼이 주어지면 해당 폼을 보여줌

  - 폼을 보여주기 위한 제네릭 뷰

  - 폼을 지정해주는 form_class와 폼을 렌더링하는 데에 필요한 template_name 속성이 주요 속성

  - 추가적으로 폼 처리가 성공한 후에 리다이렉트 목적지 URL을 지정하는 success_url 속성도 사용 가능함

  - get() 메소드와 post() 메소드 구분해 처리

  - form_valid() 메소드 오버라이딩을 통한 폼 입력 데이터 유효성 검사

  - 처리 완료 후 페이지 이동 등의 복잡한 과정을 FormView 가 알아서 처리해줌



- CreateView

  - 객체를 생성하는 폼을 보여줌

  - 새로운 레코드를 생성해서 테이블에 저장해주는 뷰

  - CreateView는 FormView의 기능을 포함함

  - 모델 정의로 부터 폼을 자동으로 만들어주는 기능과 데이터베이스에 레코드를 저장하는 기능이 더 추가됨

  - 작업 대상 테이블을 model 속성으로 지정

  - 폼을 만들 때 사용할 필드를 fields 속성으로 정의

  - 처리 성공 후 이동할 URL을 success_url 속성으로 지정

  

- UpdateView

  - 기존 객체를 수정하는 폼을 보여줌

  - 테이블에 이미 있는 레코드를 수정해주는 제레릭 뷰

  - 작업 대상 테이블로부터 폼을 만들어주며, 최종적으로는 수정된 레코드를 테이블에 저장

  - DetatilView와 동일하게 수정할 레코드를 URLconf에서 지정



- DeleteView

  - 기존 객체를 삭제하는 폼을 보여줌

  - 기존 객체를 삭제하기 위한 제네릭 뷰

  - 삭제 처리는 내부에서 이뤄지고 코드에 나타나는 것은 삭제 확인 화면

  - DeleteView는 삭제 확인용 폼만 필요하므로 입력 항목이 불필요하고 모델 정의를 참조하지도 않음

  - 삭제할 레코드를 URLconf에서 지정



<br/>

### Generic Date View

- ArchiveIndexView

  - 여러 객체를 대상으로 날짜를 기준으로 리스팅해주는 제네릭 뷰

  - 날짜 기반 제네릭 뷰의 최상위 뷰

  - 날짜 기준 내림차순으로 정렬

  - 어느 필드를 기준으로 정렬할지를 결정하는 date_field 속성이 가장 중요



- YearArchiveView

  - 년도가 주어지면 그 년도에 해당하는 객체들을 보여줌

  - 연도가 주어지면 여러 객체를 대상으로 가능한 월을 알려주는 제네릭 뷰

  - 기본 동작은 객체들을 출력해주는 것이 아니라 객체의 날짜 필드를 조사해 월을 추출한다는 점을 유의

  - 만일 주어진 연도에 해당하는 객체들을 알고 싶으면 make_object_list 속성을 True로 지정

  - model 속성이나 date+field 속성은 ArchiveIndexView와 동일

  - 마찬가지로 인자를 URLconf 에서 추출

  - 템플릿으로 넘겨주는 컨텍스트 변수 중에서 object_list는 인자로 주어진 연도에 해당하는 객체들의 리스트, date_list는 그 객체들의 월을 담고 있음 

  - make_object_list 속성이 False이면 object_list는 None

  

- MonthArchiveView

  - 연, 월이 주어지면 그에 해당하는 객체들을 보여줌

  - 주어진 연/월에 해당하는 객체를 보여주는 제네릭 뷰

  - 인자는 URLconf에서 추출

  - model 속성이나 date_field 속성은 ArchiveIndexView와 동일

  - make_object_list 속성은 없음

  - 템플릿 컨텍스트 변수 중에서 object_list는 인자로 주어진 연/월에 해당하는 객체들의 리스트를 담고 있고, date_list는 그 객체들의 일을 담고 있음



- WeekArchiveView

  - 연도와 주차가 주어지면 그에 해당하는 객체들을 보여줌

  - 연도와 주(week)가 주어지면 그에 해당하는 객체를 보여주는 제네릭 뷰

  - 인자는 URLconf 

  - 주 인자는 1년을 주차로 표현하므로 1부터 53까지의 값을 가짐

  - model , date_field 속성을 가짐

  - 템플릿 컨텍스트 변수 중에서 object_list 는 인자로 주어진 연/주에 해당하는 객체들의 리스트를 담고 있고, date_list 는 그 객체들의 연도를 담고 있음



- DayArchiveView

  - 연, 월, 일이 주어지면 그 날짜에 해당하는 객체들을 보여줌

  - 연/월/일이 주어지면 그에 해당하는 객체를 보여주는 제네릭 뷰

  - 인자는 URLconf 에서 지정

  - model, date_field 속성을 가짐

  - 템플릿 컨텍스트 변수 중에서 object_list는 인자로 주어진 연/월/일에 해당하는 객체들의 리스트를 담고 있고, date_list는 그 객체들의 연도를 담고 있음

  

- TodayArchiveView

  - 오늘 날짜에 해당하는 객체들을 보여줌

  - 오늘 날짜에 해당하는 객체를 보여주는 제네릭 뷰

  - 인자가 불필요함

  - 해당하는 URLconf 로 들어오면 뷰 내부에서 datetime.date.today() 함수로 오늘 날짜를 알아내서 처리

  - 템플릿 컨텍스트 변수 중에서 object_list는 오늘 날짜에 해당하는 객체들의 리스트를 담고 있고, date_list는 그 객체들의 연도를 담고 있음



- DateDetailView

  - 연, 월, 일, 기본 키(또는 슬러그)가 주어지면 그에 해당하는 특정 객체 하나에 대한 상세 정보를 보여줌

  - 날짜 기준으로 특정 객체를 찾아서 그 객체의 상세정보를 보여주는 제네릭 뷰

  - 객체를 찾는데 사용하는 인자로 기본키 또는 slug 인자와 함께 연/월/일 정보를 받음

  - URLconf에서 인자 지정

  - 다른 날짜 기반의 제네릭 뷰들은 복수의 객체를 출력하나 DateDetailView는 특정 객체 하나만을 다름

  - 따라서 템플릿 컨텍스트 변수는 object가 있으며 object_list 및 date_list는 사용하지 않음











<br/>

---------------------

### Reference

 https://www.slideshare.net/JoongHyeonKim/django-view-1 

