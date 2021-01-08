"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/6
"""
import flask
import math
import json
from multiprocessing.pool import Pool
from concurrent.futures import ProcessPoolExecutor

app = flask.Flask(__name__)


def is_prime(number):
    """判断是否为素数"""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    sqrt_num = int(math.floor(math.sqrt(number)))
    for i in range(3, sqrt_num + 1, 2):
        if number % i == 0:
            return False
    return True


@app.route('/is_prime/<numbers>')
def api_is_prime(numbers):
    # 方式一：使用multiprocessing.pool方式
    pool = Pool()
    num_list = [int(x) for x in numbers.split(',')]
    results = [pool.apply_async(is_prime, (x,)).get() for x in num_list]
    pool.close()
    pool.join()

    # 方式二--使用ProcessPoolExecutor
    # results = pool.map(is_prime, num_list)
    # return json.dumps(results)
    return json.dumps(dict(zip(num_list, results)))


if __name__ == '__main__':
    # pool = ProcessPoolExecutor()
    app.run()
