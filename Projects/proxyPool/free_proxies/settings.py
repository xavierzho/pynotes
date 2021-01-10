# redis数据库地址

REDIS_HOST = '127.0.0.1'

# Redis端口号
REDIS_PORT = 6379

# Redis密码，如果无填None
REDIS_PASSWORD = None

REDIS_KEY = 'proxies_pool'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
# 状态码的范围
VALID_STATUS_CODES = [200, 302]

# 代理池限制
POOL_UPPER_THRESHOLD = 100

# cycle 运行周期
TESTER_CYCLE = 1

GETTER_CYCLE = 1

API_CYCLE = 1

DB_CYCLE = 60
# 推送端口或者网页接口
API_HOST = '127.0.0.1'

API_PORT = 5000


TESTER_ENABLED = True

GETTER_ENABLED = True

API_ENABLED = True

DB_ENABLED = True
