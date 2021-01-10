import json
import csv


# json 文件遍历，换行转成csv文件
def load_json():
    # with open('itbook.json', 'r', encoding='utf-8') as f:
    #     json_data = json.load(f)
    #
    #     for data in iter(json_data):
    #         print('book_name:%s\n'
    #               'book_url:%s\n'
    #               'book_author:%s\n'
    #               'book_introduction:%s'
    #               % (
    #                   data['book_name'],
    #                   data['book_url'],
    #                   data['book_author'],
    #                   data['book_introduction']
    #               ))
    json_fp = open('itbook.json', 'r', encoding='utf-8')
    csv_fp = open('itbook.csv', 'w', encoding='utf-8')

    # 打开json文件
    data_list = json.load(json_fp)
    # 提取表头
    sheet_title = data_list[0].keys()
    # 将内容遍历进列表
    sheet_data = []
    for data in data_list:
        sheet_data.append(data.values())

    # 创建csv写入器
    writer = csv.writer(csv_fp)
    # 写入表头
    writer.writerow(sheet_title)
    # 写入表内容
    writer.writerows(sheet_data)
    # 关闭文件
    json_fp.close()
    csv_fp.close()


load_json()




