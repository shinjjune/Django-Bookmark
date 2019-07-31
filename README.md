# Django

## 장고란 무엇일까???

* django 실행

다음 명령어를 입력해 가상 환경 내에 장고를 설치합니다.

$ pip install django

장고 설치를 마치면 다음 명령어를 입력해 장고 프로젝트를 만듭니다.

$ django-admin startproject config .

데이터베이스를 초기화 하기 위해 migrate 명령을 실행합니다.

$ python manage.py migrate

데이터베이스를 초기화 했으니 관리자 계정을 생성합니다.
$ python manage.py createsuperuser


장고실행

$ python manage.py runserver

127.0.0.1:80000
