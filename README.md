# django_study

#### 장고
- 오픈소스 웹 애플리케이션 프레임워크
- 기본적으로 MTV 패턴으로 설계함
- urls.py : url파싱 후 view.py에 전달
- view : 모델로부터 데이터를 수집
- template : html, presentation layer 담당
- DB : 데이터 저장소
- __init.py__ : 해당 파일이 있는 폴더가 module이라는 의미
- setting.py : 장소 셋팅 파일
- url 정규표현식
    ^post/는 장고에게 url 시작점에 (오른쪽부터) post/가 있다는 것을 말해 줍니다.
    (\d+)는 숫자(한 개 또는 여러개) 가 있다는 뜻입니다. 내가 뽑아내고자 글 번호가 되겠지요.
    /는 장고에게 /뒤에 문자가 있음을 말해 줍니다.
    $는 URL의 끝이 방금 전에 있던 /로 끝나야 매칭될 수 있다는 것을 나타냅니다.
- mysite : 가장 바깥쪽의 디렉토리인 mysite는 Django와 아무 관련이 없는 디렉토리이며 다른 이름으로 바꿔도 상관없습니다.
- manage.py : Django의 다양한 명령어를 실행할 수 있게 해주는 커맨드라인 형태의 유틸리티입니다.
- mysite : 하위에 있는 mysite 디렉토리에 실질적인 프로젝트 파일들이 위치합니다.
- settings.py : 프로젝트의 환경 설정 파일입니다.
- urls.py : 프로젝트 레벨의 URL 패턴을 정의하는 URLConf입니다.
- wsgi.py : Apache 등과 같은 상용 웹 서버와 WSGI 규격으로 연동할 수 있게 해주는 파일입니다.
- init.py : 이 디렉토리가 Python 패키지임을 알려주는 빈 파일입니다.
- 최고권한 생성 : python manage.py createsuperuser

#### ORM 과 쿼리셋
쿼리셋 :  전달받은 모델의 객체 목록 
    Post.objects.all()
    Post.objects.create()
    Post.objects.filter(title__contains='title')
     ㄴ title와 contains 사이에 있는 밑줄(_)이 2개(__)입니다. 장고 ORM은 필드 이름("title")과 연산자과 필터("contains")를 밑줄 2개를 사용해 구분
    Post.objects.get(title="Sample title")
    ㄴ 게시물 인스턴스 얻기
    Post.objects.order_by('created_date')
    ㄴ 정렬하기
    


#### 모설계 필드 타입 종류
CharField	제한된 문자열 필드 타입. 최대 길이를 max_length 옵션에 지정해야 한다. 문자열의 특별한 용도에 따라 CharField의 파생클래스로서, 이메일 주소를 체크를 하는 EmailField, IP 주소를 체크를 하는 GenericIPAddressField, 콤마로 정수를 분리한 CommaSeparatedIntegerField, 특정 폴더의 파일 패스를 표현하는 FilePathField, URL을 표현하는 URLField 등이 있다.
TextField	대용량 문자열을 갖는 필드
IntegerField	32 비트 정수형 필드. 정수 사이즈에 따라 BigIntegerField, SmallIntegerField 을 사용할 수도 있다.
BooleanField	true/false 필드. Null 을 허용하기 위해서는 NullBooleanField를 사용한다.
DateTimeField	날짜와 시간을 갖는 필드. 날짜만 가질 경우는 DateField, 시간만 가질 경우는 TimeField를 사용한다.
DecimalField	소숫점을 갖는 decimal 필드
BinaryField	바이너리 데이타를 저장하는 필드
FileField	파일 업로드 필드
ImageField	FileField의 파생클래스로서 이미지 파일인지 체크한다.
UUIDField	GUID (UUID)를 저장하는 필드

##### 새항목 추가해줄ㄱ때 
₩₩₩ makemigrations
migrate --fake ₩₩₩

#### 유저모델
* 기존의 Users 모델 사용하는 방식
  기본 사용자 모델에서는, first name, last name, email, password, username, is_staff, is_admin 의 필드를 제공
- 모델변형
- auth.login 은 기본적으로 username과 password로 로그인하고 인증함 (게속 다른걸로 하다가 안되서 삽잘히고 있었음 ㅜㅜ
)
- 참고링크 :https://ssungkang.tistory.com/entry/Django-10-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%EB%A1%9C%EA%B7%B8%EC%9D%B8%EB%A1%9C%EA%B7%B8%EC%95%84%EC%9B%83-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0

* user모델 커스텀 사용
BaseUserManager 클래스 : User를 생성할때 사용하는 클래스이고 
AbstractBaseUser 클래스 : 상속받아 생성하는 클래스이다.
- 참고링크 :    https://coninggu.com/django-v2.2-3-%EC%9C%A0%EC%A0%80-%EB%AA%A8%EB%8D%B8-%EC%BB%A4%EC%8A%A4%ED%85%80%ED%95%98%EA%B8%B0/
            https://dev-yakuza.github.io/ko/django/custom-user-model/
             https://agent-night.tistory.com/4?category=648941