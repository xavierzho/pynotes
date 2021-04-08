from flask import Flask, request

app = Flask(__name__)


@app.route('/index/', methods=['GET', 'POST'])  # 当url即可以支持GET也支持POST请求
def index():
    print(request.form)  # 获取form 表单提交过来的非文件数据
    print(request.files)  # 获取文件的内容
    # 保存文件
    file_obj = request.files.get('myfile')
    file_obj.save(file_obj.name)
    return 'OK'


app.run()
