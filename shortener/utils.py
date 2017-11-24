import random
import string

from django.conf import settings

SHORTCODE_MIN = getattr(settings , "SHORTCODE_MIN", 6 )

# def code_generator(size=6, chars='abcdefghijklmnopqrstuvwyxz'):
def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase+string.digits):
    new_code = ''
    for i in range(size):
        new_code += random.choice(chars)

    return new_code
    # return ''.join(random.choice(chars) for _ in range(size)) # 위의 코드와 같음

def create_shortcode(instance, size=SHORTCODE_MIN):
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
