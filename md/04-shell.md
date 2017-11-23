## Python Shell
- shell 에서 작업하기 
~~~
source $ python manage.py shell

Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 19 2015, 20:38:52) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
~~~

- shell 
    - KirrURL 모든 값 가져오기 
~~~
>>> from shortener.models import KirrURL
>>> KirrURL.objects.all()
<QuerySet [<KirrURL: http://www.daum.net>, <KirrURL: http://www.naver.com>]>
~~~

- 새로운 값 입력하기 
    - KirrURL()
~~~
>>> from shortener.models import KirrURL

>>> new_obj = KirrURL()
>>> new_obj.url = 'http://www.facebook.com'
>>> new_obj.shortcode = 'facebook'
>>> new_obj.save()
~~~

- 다른 방식으로 새로운 값 입력 
    - KirrURL.objects.create()
~~~
>>> from shortener.models import KirrURL

>>> new_obj2 = KirrURL.objects.create()
>>> new_obj2.url = 'http://www.djangoproject.com'
>>> new_obj2.shortcode ='django'
>>> new_obj2.save()
~~~
- 바로 입력 
    - KirrURL.objects.create(url='http://www.abc.com', shortcode='abc')
~~~
>>> from shortener.models import KirrURL

>>> new_obj3 = KirrURL.objects.create(url='http://www.abc.com', shortcode='abc')
~~~

- 가져오거나 새롭게 생성 
    - KirrURL.objects.get_or_create(url='http://www.abc.com')
~~~
>>> from shortener.models import KirrURL

>>> obj4, created = KirrURL.objects.get_or_create(url='http://www.abc.com')
>>> print(obj4)
http://www.abc.com
>>> print(created)
False
>>> obj4.shortcode
'abc'
~~~

<br/>

- 값이 존재하지 않을 경우 
    - KirrURL.objects.get(url='http://www.google.com')
~~~
>>> from shortener.models import KirrURL

>>> obj5 = KirrURL.objects.get(url='http://www.google.com')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/sangjunpark/Documents/Dropbox/pythonproject/dev_lec/lec_django_1_10/lib/python3.4/site-packages/django/db/models/manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/Users/sangjunpark/Documents/Dropbox/pythonproject/dev_lec/lec_django_1_10/lib/python3.4/site-packages/django/db/models/query.py", line 385, in get
    self.model._meta.object_name
shortener.models.DoesNotExist: KirrURL matching query does not exist.
>>>
~~~

- 새로운 값 생성 
    - 리턴값은 2개 
    - 새롭게 만들면, 만들고 True
    - 기존 값 존재하면 False 
~~~
>>> from shortener.models import KirrURL

>>> obj6 = KirrURL.objects.get_or_create(url='http://www.google.com', shortcode='google')
>>> print(obj6)
(<KirrURL: http://www.google.com>, True)

>>> obj7 = KirrURL.objects.get_or_create(url='http://www.google.com',shortcode='google')
>>> print(obj7)
(<KirrURL: http://www.google.com>, False)
~~~