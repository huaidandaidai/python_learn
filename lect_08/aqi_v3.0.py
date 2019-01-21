"""
    作者：lsh
    日期：2019/01/16
    版本：v2.0
    功能：实现AQI计算
"""
import json
import csv
import os


def process_json_file(filepath):
    """
        解码json文件
    """
    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)


def process_csv_file(filepath):
    """
        解析csv文件
    """
    with open(filepath, mode='r', encoding='utf-8', newline='') as f:
        reader =csv.reader(f)
        for row in reader:
            print(','.join(row))


def main():
    """
        主函数
    """
    file_path = input('请输入json文件名称：')
    filename, file_ext = os.path.splitext(file_path)

    if file_ext == '.json':
        process_json_file(file_path)
    elif file_ext == '.csv':
        process_csv_file(file_path)
    else:
        print('不支持的文件格式！')


if __name__ == '__main__':
    main()