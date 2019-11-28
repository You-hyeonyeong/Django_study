# django_study

#### 장고
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


#### 모뎅설계 필드 타입 종류
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
- 기존의 AbstractBaseUser 모델 사용하는 방식
  기본 사용자 모델에서는, first name, last name, email, password, username, is_staff, is_admin 의 필드를 제공
- 모델변형