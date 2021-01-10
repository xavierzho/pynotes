from mitmproxy import http


def request(flow: http.HTTPFlow):
    # redirect to different host
    if flow.request.pretty_host == "example.com":
        flow.request.host = "mitmproxy.org"
    # answer from proxy
    elif flow.request.path.endswith("/brew"):
        flow.response = http.HTTPResponse.make(
            418, b"I'm a teapot",
        )
