from django.test import TestCase

# Create your tests here.
import os


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite05.settings')
    import django
    django.setup()
    # from pathlib import Path
    # BASE_DIR = Path(__file__).resolve().parent

    # print(os.path.dirname(os.path.dirname(__file__)))
    # print(Path(BASE_DIR).joinpath('templates'))
    from django.core import signing
    from time import time
    from hashlib import md5
    from django.core.cache import cache
    HEADER = {'username': 'jones', 'value':'pwt'}
    KEY = 'jones'
    SALT = 'www.jones.com'
    TIMEOUT = 30 * 60  #30min


    def encrypt(obj):
        # 加密
        value = signing.dumps(obj, key=KEY, salt=SALT)
        value = signing.b64_encode(value.encode()).decode()
        # print(value)
        return value

    def decrypt(src):
        # 解密
        src = signing.b64_decode(src.encode()).decode()
        raw = signing.loads(src, key=KEY, salt=SALT)
        # print(raw)
        return raw

    def create_token(username):
        # 生成token
        # 1.加密头信息
        header = encrypt(HEADER)
        print(header)
        # 2.构造Payload
        payload = {'username': username, 'iat': time()}
        payload = encrypt(payload)
        print(payload)
        # 3.生成签名
        md5_dig = md5()
        md5_dig.update(f'{header}.{payload}'.encode())
        signature = md5_dig.hexdigest()
        token = f'{header}.{payload}.{signature}'
        print(token)
        # 存储到缓存中
        cache.set(username, token, TIMEOUT)
        return token

    def get_payload(token):
        payload = str(token).split('.')[1]
        payload = decrypt(payload)
        print(payload)
        return payload

    def get_username(token):
        payload = get_payload(token)
        return payload['username']


    def check_token(token):
        username = get_username(token)
        last_token = cache.get(username)
        if last_token:
            print(last_token == token)
            return last_token == token
        return False


    # tokens = create_token('jones')
    #
    # create_token(tokens)

