from mitmproxy import ctx


# 打印请求信息
def request(flow):
    requests = flow.request

    info = ctx.log.info
    # warm.dir(requests)
    info(requests.url)

    info(str(requests.headers))

    info(str(requests.cookies))

    info(requests.host)

    info(str(requests.port))
