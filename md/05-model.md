## models.py 저장 
- save() 메소드 추가 
    - override 시킴 
~~~
class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15, unique=True, null=True)
    # shortcode = models.CharField(max_length=15, null=False, blank=False)
    # shortcode = models.CharField(max_length=15, null = True)
    # shortcode = models.CharField(max_length=15 , default='')

    updated     = models.DateTimeField(auto_now = True) # everytime the model is saved
    timestamp   = models.DateTimeField(auto_now_add = True) # when model was created

    # override
    def save(self, *args, **kwargs):
        super(KirrURL, self).save(*args, **kwargs)
        
    def __str__(self):
        return str(self.url)
~~~      

<br/>

- 커스텀하게 my_save() 만듬 
~~~
class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15, unique=True, null=True)
    # shortcode = models.CharField(max_length=15, null=False, blank=False)
    # shortcode = models.CharField(max_length=15, null = True)
    # shortcode = models.CharField(max_length=15 , default='')

    updated     = models.DateTimeField(auto_now = True) # everytime the model is saved
    timestamp   = models.DateTimeField(auto_now_add = True) # when model was created

    # override
    def save(self, *args, **kwargs):
        super(KirrURL, self).save(*args, **kwargs)

    def my_save(self):
        self.save()

    def __str__(self):
        return str(self.url)
~~~         

- shortcode 를 업데이트 할 때마다 랜덤하게 추출 가능 
    - import random 
    - def code_generator() 함수 생성 
    - def save() 메소드에 
        - self.shortcode = code_generator() 추가 
- 웹사이트에서 업데이트 할 때마다 
    - shortcode 이 알파벳의 6자로 자동변경 
~~~
from django.db import models
import random
# Create your models here.

def code_generator(size=6, chars='abcdefghijklmnopqrstuvwyxz'):
    new_code = ''
    for i in range(size):
        new_code += random.choice(chars)

    return new_code
    # return ''.join(random.choice(chars) for _ in range(size)) # 위의 코드와 같음

class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15, unique=True, null=True)
    # shortcode = models.CharField(max_length=15, null=False, blank=False)
    # shortcode = models.CharField(max_length=15, null = True)
    # shortcode = models.CharField(max_length=15 , default='')

    updated     = models.DateTimeField(auto_now = True) # everytime the model is saved
    timestamp   = models.DateTimeField(auto_now_add = True) # when model was created

    # override
    def save(self, *args, **kwargs):
        self.shortcode = code_generator()
        super(KirrURL, self).save(*args, **kwargs)

    # def my_save(self):
    #     self.save()

    def __str__(self):
        return str(self.url)
~~~         
- 알파벳 소문자 + 숫자로 랜덤하게 생성 
~~~
from django.db import models
import random
import string
# Create your models here.

# def code_generator(size=6, chars='abcdefghijklmnopqrstuvwyxz'):
def code_generator(size=6, chars=string.ascii_lowercase+string.digits):
    new_code = ''
    for i in range(size):
        new_code += random.choice(chars)

    return new_code
    # return ''.join(random.choice(chars) for _ in range(size)) # 위의 코드와 같음
~~~

<br/>

---

## uitls.py 파일 만들기 
- uitility 코드는 별도의 파일로 관리 
    - /shortener/uitls.py 
    - [utils.py](../shortener/utils.py)
~~~
import random
import string

# def code_generator(size=6, chars='abcdefghijklmnopqrstuvwyxz'):
def code_generator(size=6, chars=string.ascii_lowercase+string.digits):
    new_code = ''
    for i in range(size):
        new_code += random.choice(chars)

    return new_code
    # return ''.join(random.choice(chars) for _ in range(size)) # 위의 코드와 같음
~~~

<br/>

- models.py 는 import만 시킴 
    - from .utils import code_generator

~~~
from django.db import models
# Create your models here.

from .utils import code_generator

class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15, unique=True, null=True)
    # shortcode = models.CharField(max_length=15, null=False, blank=False)
    # shortcode = models.CharField(max_length=15, null = True)
    # shortcode = models.CharField(max_length=15 , default='')

    updated     = models.DateTimeField(auto_now = True) # everytime the model is saved
    timestamp   = models.DateTimeField(auto_now_add = True) # when model was created

    # override
    def save(self, *args, **kwargs):
        self.shortcode = code_generator()
        super(KirrURL, self).save(*args, **kwargs)

    # def my_save(self):
    #     self.save()

    def __str__(self):
        return str(self.url)
~~~  

<br/>

- dev save() 에서 
    - shortcode 의 값을 체크하여 
        - 존재하지 않을 경우 code_generator() 함수 실행 
~~~
    # override
    def save(self, *args, **kwargs):
        # shortcode 가 존재하지 않을 경우
        if self.shortcode is None or self.shortcode == "" :
            self.shortcode = code_generator()

        super(KirrURL, self).save(*args, **kwargs)
~~~

<br/>

## 자동으로 shortcode 업데이트 
- utils.py 변경 
    - [utils.py](../shortener/utils.py)
    - def create_shortcode() 함수 생성 
        - instance 
            - models.py 에서 자체 메소드에서 생성한 instance 입력 
            - 해당값이 존재하면 새로운 shortcode 를 생성을 위해 
                - 다시 create_shortcode() 함수를 부른다 
~~~
import random
import string

# def code_generator(size=6, chars='abcdefghijklmnopqrstuvwyxz'):
def code_generator(size=6, chars=string.ascii_lowercase+string.digits):
    new_code = ''
    for i in range(size):
        new_code += random.choice(chars)

    return new_code
    # return ''.join(random.choice(chars) for _ in range(size)) # 위의 코드와 같음

def create_shortcode(instance, size=6):
    # 기존 shortcode 값이 존재하면 다시 한번 더 실행
    new_code = code_generator(size=size)

    print(instance)  # http://www.google.com
    print(instance.__class__)  # <class 'shortener.models.KirrURL'>
    print(instance.__class__.__name__)  # KirrURL

    KClass = instance.__class__
    qs_exists = KClass.objects.filter(shortcode=new_code).exists()
    if qs_exists :
        return create_shortcode(size=size)
    return new_code
~~~   

<br/>
- shortcode 옵션 변경
    - blank = True  
    - shortcode = models.CharField(max_length=15, unique=True, blank=True)

- models.py 에서 
    - [models.py](../shortener/models.py)
    - 추가 : from .utils import create_shortcode
    - 추가 : self.shortcode = create_shortcode(self)
        - 새로운 shortcode를 생성하거나 
        - 기존 값이 존재하거나 없어도, 다른 shortcode 생성 
~~~
...

from .utils import code_generator
from .utils import create_shortcode

class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    # shortcode = models.CharField(max_length=15, null=False, blank=False)
    # shortcode = models.CharField(max_length=15, null = True)
    # shortcode = models.CharField(max_length=15 , default='')

    updated     = models.DateTimeField(auto_now = True) # everytime the model is saved
    timestamp   = models.DateTimeField(auto_now_add = True) # when model was created

    # override
    def save(self, *args, **kwargs):
        # shortcode 가 존재하지 않을 경우
        if self.shortcode is None or self.shortcode == "" :
            # self.shortcode = code_generator()
            self.shortcode = create_shortcode(self)

        super(KirrURL, self).save(*args, **kwargs)
        
...
        
~~~        

<br/>

---

## Manager 
- model manager 추가 
    - /shortener/models.py
    - 모든 값을 리턴할 수 있게 
~~~
class KirrURLManager(models.Manager):
    def all(self, *arg, **kwargs):
        qs = super(KirrURLManager, self).all(*args, **kwargs)
        return qs
       
        
class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    ...        
~~~

- class KirrURL에서 
    - 추가 : active = models.BooleanField(default=True)
~~~
class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated     = models.DateTimeField(auto_now = True) # everytime the model is saved
    timestamp   = models.DateTimeField(auto_now_add = True) # when model was created
    active      = models.BooleanField(default=True)
~~~    


- models.py 변경되었기 때문에 
~~~
$ python manage.py makemigrations
$ python manage.py migrate
~~~

<br/>

- queryset filter 연동
    - 추가 : qs = qs_main.filter(active=False)
~~~
class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=False)
        return qs

class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    ...
~~~    

- python shell 에서 확인 
    - 전체 확인 : KirrURL.objects.all()
    - 갯수 확인 : KirrURL.objects.count()
~~~
$ python manage.py shell

>>> from shortener.models import KirrURL

>>> KirrURL.objects.all()
<QuerySet [<KirrURL: http://www.daum.net>, <KirrURL: http://www.naver.com>, <KirrURL: http://www.facebook.com>, <KirrURL: http://www.djangoproject.com>, <KirrURL: http://www.abc.com>, <KirrURL: http://www.google.com>]>

>>> KirrURL.objects.count()
6

>>> KirrURL.objects.all().count()
6 
~~~

<br/>

- http://localhost:8000/admin 에서 
    - google.com 을 active를 체크박스 풀어서 False 로 설정 
    
- KirrURL에서 
    - 추가 : objects = KirrURLManager()
    - 추가 : some_random = KirrURLManager()
~~~
class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated     = models.DateTimeField(auto_now = True) # everytime the model is saved
    timestamp   = models.DateTimeField(auto_now_add = True) # when model was created
    active      = models.BooleanField(default=True)

    # shortcode = models.CharField(max_length=15, null=False, blank=False)
    # shortcode = models.CharField(max_length=15, null = True)
    # shortcode = models.CharField(max_length=15 , default='')

    objects = KirrURLManager()
    some_random = KirrURLManager()
~~~

- python shell 에서 빠져나와서, 다시 shell 모드 
    - 관리자에서 active를 false 로 만든 1개만 추출 
    - KirrURLManager() 의 영향 
        - objects = KirrURLManager()
        - some_random = KirrURLManager()
~~~
$ python manage.py shell

>>> from shortener.models import KirrURL

>>> KirrURL.objects.all()
<QuerySet [<KirrURL: http://www.google.com>]>

>>> KirrURL.objects.all().count()
1 

>>> KirrURL.some_random.all()
<QuerySet [<KirrURL: http://www.google.com>]>
~~~ 

- active=True 변경 
    - qs = qs_main.filter(active=True)
~~~
class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs
~~~

<br/>

- python shell 확인 
    - active 를 true 변경한 내용만 추출 
~~~
$ python manage.py shell

>>> from shortener.models import KirrURL

>>> KirrURL.objects.all()
<QuerySet [<KirrURL: http://www.daum.net>, <KirrURL: http://www.naver.com>, <KirrURL: http://www.facebook.com>, <KirrURL: http://www.djangoproject.com>, <KirrURL: http://www.abc.com>]>

>>> KirrURL.objects.all().count()
5
~~~

<br/>

- shortcode 를 다시 재지정 
    - 추가 : def refresh_shortcode(self): 
    - gte (greater than , equal) 
        - \>=
        - https://docs.djangoproject.com/en/1.11/ref/models/querysets/
~~~
class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self):
        qs = KirrURL.objects.filter(id__gte =1)
        new_codes = 0
        for q in qs :
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)
~~~   

<br/>

- python shell 로 확인 
    - KirrURL.objects.refresh_shortcodes()
    - 다시 shortcode가 재지정됨 
    - http://localhost:8000/admin에서 확인해보면 재지정 되어 있음 
~~~
$ python manage.py shell

>>> from shortener.models import KirrURL

>>> KirrURL.objects.refresh_shortcodes()
3fyram
e98tri
l7cl26
dpe2c6
nxmd1y
nsablc
'New codes made: 6'
~~~

##  마무리 주석 처리  
- /shortener/utils.py
    - print(instance)
    - print(instance.\_\_class\_\_)
    - print(instance.\_\_class\_\_.\_\_name\_\_)
~~~
def create_shortcode(instance, size=6):
    # 기존 shortcode 값이 존재하면 다시 한번 더 실행
    new_code = code_generator(size=size)

    # print(instance)  # http://www.google.com
    # print(instance.__class__) # <class 'shortener.models.KirrURL'>
    # print(instance.__class__.__name__)  # KirrURL

    KClass = instance.__class__
    qs_exists = KClass.objects.filter(shortcode=new_code).exists()
    if qs_exists :
        return create_shortcode(size=size)
    return new_code
~~~           
     
  