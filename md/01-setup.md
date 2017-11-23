## Django 장고 소개  
- https://www.djangoproject.com/

## 기본 설치 
- pip : python package installer 
    - [pip 설치](http://blog.colab.kr/11)
- virtualenv 
    - [가상환경설치](https://www.holaxprogramming.com/2017/07/15/python-virtual-environments/)
    - [가상환경 구축](http://pythoninreal.blogspot.kr/2013/12/virtualenv.html)
- python : version 3
    - [점프투파이썬](https://wikidocs.net/8)
    
---
    
## Django Setting 
~~~
mkdir lec_django_1_10
cd lec_lec_django_1_10
~~~

- virtualenv -p python3.4 .
- source ./bin/activate
    - 가상환경 상태 
        - [가상환경설치](https://www.holaxprogramming.com/2017/07/15/python-virtual-environments/)
    - 파이썬 설치 
        - [점프투파이썬](https://wikidocs.net/8)
        - [pip 설치](http://blog.colab.kr/11)
        - [가상환경 구축](http://pythoninreal.blogspot.kr/2013/12/virtualenv.html)

---
        
## virtualenv 설치 

- 가상환경을 설치한 이후 virtualenv -p python3.4 . 
    - 내부 폴더 :
        - bin/activate, pytho3.4  
        - lib/python3.4/site-packages 
        
- 가상환경 source ./bin/activate 실행 
    - deactivate 빠져나올 때 
~~~
lec_django_1.10 $ virtualenv -p python3.4 .
lec_django_1.10 $ source ./bin/activate
(lec_django_1_10) lec_django_1.10 $ deactivate
lec_django_1.10 $
~~~   

## Django 1.10 설치 

- 가상환경    
~~~
lec_django_1.10 $ source ./bin/activate
(lec_django_1_10) lec_django_1.10 $ 
~~~

- 가상환경 내에 
    - pip install 
    - lec_django_1.10/lib/python3.4/site-packages 설치된다 
    - pip freeze 
        - 장고 패키지 설치 및 확인 
~~~
$ pip install django==1.10
$ pip freeze 
>> Django==1.10
~~~

## Pycharm 에서 interpreter 연동 
- preferences (settings)
    - Project:source
        - Project Interpreter 
            - add local 
                - 컴퓨터의 해당하는 파이썬 버전 잡기 
                - lec_django_1.10/bin/python3

    
