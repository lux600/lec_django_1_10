## django-admin commmands
- django-admin commands
    - https://docs.djangoproject.com/en/1.11/howto/custom-management-commands/
~~~
polls/
    __init__.py
    models.py
    management/
        __init__.py
        commands/
            __init__.py
            _private.py
            closepoll.py
    tests.py
    views.py
~~~

<br>

- 폴더 구조 만들기 
    - /shortener/ 구조 아래 
        - management 폴더 생성
            - \_\_init\_\_.py 파일 생성
            - commands 폴더 생성 
                -  \_\_init\_\_.py 파일 생성
                - refreshcodes.py 파일 생성 
- django-admin commands
    - 복사 : https://docs.djangoproject.com/en/1.11/howto/custom-management-commands/
~~~                    
from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for poll_id in options['poll_id']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
~~~  

- 복사한 내용을 수정 
    - poll 대신에 
        -  from shortener.models import KirrURL
    - 주석처리 
        - def add_arguments(self, parser):
    - 이후 삭제 
        - def handle(self, *args, **options):

~~~
from django.core.management.base import BaseCommand, CommandError
from shortener.models import KirrURL

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        pass
~~~  

- 수정 
    - /shortener/management/commands/refreshcodes.py
        - help 
        - return 
~~~
from django.core.management.base import BaseCommand, CommandError
from shortener.models import KirrURL

class Command(BaseCommand):
    help = 'Refreshed all KirrURL shortodes'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        return KirrURL.objects.refresh_shortcodes()
~~~      
- python commands 파일 실행
    - python shell 에서 실행했던 shortcode 재지정이 실행된다  
~~~ 
source $ python manage.py refreshcodes

cygjau
xkbyvc
m9wk9o
beqhcw
bopv3x
z3hq73
New codes made: 6
~~~   

- 수정 
    - argument 설정 
        - def add_arguments(self, parser) 수정 
    - 옵션 출력
        - print(options)
~~~
class Command(BaseCommand):
    help = 'Refreshed all KirrURL shortodes'

    def add_arguments(self, parser):
        parser.add_argument('number', type=int)

    def handle(self, *args, **options):
        print(options)
        return KirrURL.objects.refresh_shortcodes()
~~~  

-  python manage.py refreshcodes 실행 
~~~
source $ python manage.py refreshcodes

usage: manage.py refreshcodes [-h] [--version] [-v {0,1,2,3}]
                              [--settings SETTINGS] [--pythonpath PYTHONPATH]
                              [--traceback] [--no-color]
                              number
manage.py refreshcodes: error: the following arguments are required: number
~~~

- 옵션 추가 실행 
~~~
source $ python manage.py refreshcodes 10

{'settings': None, 'traceback': False, 'number': 10, 'verbosity': 1, 'pythonpath': None, 'no_color': False}
1543lg
mu0fka
kdfrej
rbxl2d
0qq8a8
k0xreu
New codes made: 6
~~~

- 옵션 수정 
    - number1
    - number2
    - number3
~~~
class Command(BaseCommand):
    help = 'Refreshed all KirrURL shortodes'

    def add_arguments(self, parser):
        parser.add_argument('number1', type=int)
        parser.add_argument('number2', type=int)
        parser.add_argument('number3', type=int)
    ...
~~~

- 옵션 추가 실행 
~~~
source $ python manage.py refreshcodes 10

usage: manage.py refreshcodes [-h] [--version] [-v {0,1,2,3}]
                              [--settings SETTINGS] [--pythonpath PYTHONPATH]
                              [--traceback] [--no-color]
                              number1 number2 number3
manage.py refreshcodes: error: the following arguments are required: number2, number3
~~~

- 옵션 3개 설정 
~~~
source $ python manage.py refreshcodes 10 11 12

{'settings': None, 'number3': 12, 'number1': 10, 'traceback': False, 'no_color': False, 'pythonpath': None, 'verbosity': 1, 'number2': 11}
9ljtp7
stjvt4
rp6b78
mvdxnt
s30u8r
bktnnh
New codes made: 6
~~~

<br/>

---

## items 

- /shortener/models.py
    - KirrURLManager
        - 인수변경 : def refresh_shorcodes(self, items=100)
            - items=100
        - 출력 확인 
            - print(items) 
~~~    
class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=100):
        print(items)
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

- /shorten/management/commands/refreshcodes.py
    - def add_arguments()
        - 인수전달 items 변경 
            - parser.add_argument('items',type=int)
    - def handle()
        - return 인자로 (items=options['items'])
~~~
class Command(BaseCommand):
    help = 'Refreshed all KirrURL shortodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        print(options)
        return KirrURL.objects.refresh_shortcodes(items=options['items'])
~~~        
       
- commands 실행 
    - items 가 10으로 받음 
~~~
$ python manage.py refreshcodes 10 

{'verbosity': 1, 'traceback': False, 'pythonpath': None, 'no_color': False, 'settings': None, 'items': 10}
10
xs1nvs
gozscv
ef8cy9
ukamnh
n9xeql
e225k2
New codes made: 6
~~~

- /shortener/management/commands/refreshcodes.py
    - def handle()
        - print(options) 삭제 
~~~
class Command(BaseCommand):
    help = 'Refreshed all KirrURL shortodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return KirrURL.objects.refresh_shortcodes(items=options['items'])
~~~ 

- commands 실행 
~~~
$ python manage.py refreshcodes 10

10
cc0549
d5jua7
zvvefu
kgimbm
cfqqsa
aj5gz1
New codes made: 6
~~~

<br/>

---

## 존재하는 갯수만 command 
- /shortener/models.py
    - def refresh_shortcodes()
        - 전달인수 : itmes=None 변경
        - print(items) 삭제  
        - 해당 items 갯수만 가져옴 
            - if items is not None and isinstance(items, int):
                - order_by 정렬 기준 
~~~
class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        #print(items)
        qs = KirrURL.objects.filter(id__gte =1)

        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]

        new_codes = 0
        for q in qs :
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)
~~~  

- commands 실행
    - 존재하는 갯수 내에서 실행  
~~~
$ python manage.py refreshcodes 10

o79nhz
a60kkj
ut2t41
cov70r
2xnrb2
amqkh3
New codes made: 6
~~~

<br/>

---

- /shortener/management/commands/refreshcodes.py
    - def add_arguments()
        - 전달인수 items 에 \-\- 추가  
~~~
class Command(BaseCommand):
    help = 'Refreshed all KirrURL shortodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return KirrURL.objects.refresh_shortcodes(items=options['items'])
~~~ 

- /shortener/models.py
    - def refresh_shortcodes()
        - for 문에서 
            - print(q.shortcode) 대신에 
                - q.id로 출력확인  
~~~
class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        #print(items)
        qs = KirrURL.objects.filter(id__gte =1)

        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]

        new_codes = 0
        for q in qs :
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)
~~~  

- commands 실행
    - 아무 인자 없이
        - id 인덱스 순서대로 재지정됨    
~~~
$ python manage.py refreshcodes 

1
2
3
4
5
6
New codes made: 6
~~~   

- commands 실행
    - 전달인자 : --items 갯수 
        - 역으로 정렬됨     
~~~
$ python manage.py refreshcodes --items 10

6
5
4
3
2
1
New codes made: 6
~~~      

       
                                           
        