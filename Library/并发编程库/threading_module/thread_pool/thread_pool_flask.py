"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/6
"""
import flask
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

app = flask.Flask(__name__)

pool = ThreadPoolExecutor()


def read_file():
    time.sleep(0.1)
    return "file_result"


def read_db():
    time.sleep(0.2)
    return "db_result"


def read_api():
    time.sleep(0.3)
    return "api_result"


@app.route('/')
def index():
    result_file = pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)
    return json.dumps({
        'result_file': result_file.result(),
        'result_db': result_db.result(),
        'result_api': result_api.result()
    })


if __name__ == '__main__':
    app.run()
