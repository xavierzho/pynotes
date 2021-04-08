from django.test import TestCase

# Create your tests here.
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite04.settings")
    import django
    django.setup()
    from django.core import signing
    # 加密
    value = signing.dumps({'foo': 'bar'})
    print(value)
    # 解密
    src = signing.loads(value)
    print(src)
