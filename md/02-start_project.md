## Django Project 시작하기
 
- 가상환경 
~~~
lec_django_1.10 $ source ./bin/activate
(lec_django_1_10) lec_django_1.10 $ 
~~~

- 현재 패키지 설치 확인 
~~~
$ pip freeze 
>> Django==1.10
~~~

- 처음 프로젝트 시작 
    - lec_django_1.10 위치 내에서 
    - mysite 이름으로 프로젝트 생성 
~~~
lec_django_1.10 $  
$ django-admin.py startproject mysite 
~~~ 

- 설치하고 나면 
    - mysite 내에 아래와 같이 설치됨 
        - mysite 
        - manage.py  
    - 헛갈리는 것을 방지하기 위해서 
        - 상위의 mysite 를 source 로 변경 
~~~
lec_django_1.10 $ mv mysite source
~~~

- pycharm 에서 source 폴더에서 open  
    - READ.md 파일 만들기 
    
---

## Git hub 
- github.com 에서 개별 저장소 생성 
- lec_django_1_10
  
        
## Git 초기화  
- …or create a new repository on the command line

~~~
git init
~~~
- .gitignore 파일만들기 
    - 무시할 파일 리스트
        - http://dolfalf.tistory.com/58
        - https://www.gitignore.io/api/pycharm,python,django
        - https://stackoverflow.com/questions/3719243/recommended-gitignore-file-for-python-projects 
    - .idea/
- git status 
    - 현재 추가된 상태     
~~~    
git add .
git status 
~~~
~~~
git add .
git commit -m "first commit"
git remote add origin git@github.com:lux600/lec_django_1_10.git
git push -u origin master
~~~

- 이후 업데이트 

~~~
git add .
git commit -m "새로운 내용 업데이트 되었습니다."
git push -u origin master
~~~    

---

## Django Project DB 생성 
- mysite/settings.py
    - [setting.py](../mysite/settings.py)
    - database 내용 
~~~
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
~~~
    
- source 위치에서 실행 
    - makemigrations 
        - 새롭게 django 내에서 바뀐 내용에 대한 sql 문으로 변환 가능 파일 만들기
        - [ 참고문서 ](https://wayhome25.github.io/django/2017/03/20/django-ep6-migrations/)
        - SQLite 브라우저
            - http://sqlitebrowser.org/     
~~~
source $ python manage.py makemigrations
>> No changes detected
~~~

<br/>

- makemigrations 파일 내용을 DB 에 적용하기 
    - source/db.sqlite3 파일 생성 
~~~
$ python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying sessions.0001_initial... OK 
~~~

<br/>

---

## 슈퍼유저(관리자) 만들기
- ID: admin 
    - Email : thinkmentor@gmail.com
    - Password : admin1234

~~~
$ python manage.py createsuperuser
Username (leave blank to use 'cfe'): 
Email address : 
Password : 
Password (agin) : 
Superuser created successfully.
~~~

- 서버 실행
    - http://localhost:8000
    - http://127.0.0.1:8000 
~~~
$ python manage.py runserver

Performing system checks...

System check identified no issues (0 silenced).
November 23, 2017 - 08:31:57
Django version 1.10, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
~~~

- 관리자 
    - http://127.0.0.1:8000/admin
    - id : admin
    - password : admin1234
    
## 사용자 추가 
- http://127.0.0.1:8000/admin
    - id : admin
    - password : admin1234
- Site administration
    - Users  
        - 오른쪽 상단 : add users   
      



