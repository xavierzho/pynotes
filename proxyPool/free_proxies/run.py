from proxyPool.free_proxies.scheduler import Scheduler

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF-8')


def main():
    try:
        s = Scheduler()
        s.run()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
