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
