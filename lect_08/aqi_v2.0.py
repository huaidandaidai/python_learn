"""
    作者：lsh
    日期：2019/01/16
    版本：v2.0
    功能：实现AQI计算
"""
import json


def process_json_file(filepath):
    """
        解码json文件
    """
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    """
        主函数
    """
    file_path = input('请输入json文件名称：')
    city_list = process_json_file(file_path)
    city_list.sort(key=lambda city: city['aqi'])
    top5_list = city_list[:5]

    # 写入前五个到文件
    f = open('top5_aqi.json', mode='w',encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()
    print(city_list)


if __name__ == '__main__':
    main()