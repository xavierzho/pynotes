import requests
from urllib.parse import quote
from lxml import etree

lua = '''
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://www.baidu.com")
        return {
            html = treat.as_string(response.body),
            url = response.url,
            status = response.status
        }
end
'''
url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)

