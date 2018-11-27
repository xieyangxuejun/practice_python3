#!usr/bin/env python
# encoding:utf-8

"""
@author: silen
@contact: xieyangxuejun@gmail.com
@file: file_operation.py
@time: 2018/11/28 0:07
@desc: excel转换成text并保存
@software: 
@license: 
"""

import pandas as pd
import os


class OfficeFile:

    def __init__(self, path=os.getcwd()):
        self.path = path

    def excel_to_txt(self):
        print(self.path)


if __name__ == '__main__':
    excel_name = 'month7.xlsx'
    txt_name = 'month7.txt'
    res_dir_path = os.path.abspath('..') + '\\res\\'
    office_file = OfficeFile(res_dir_path + excel_name)
    d = pd.read_excel(office_file.path, sheet_name=None)
    # 转换 方式1
    # with open(res_dir_path + txt_name, 'w', encoding='UTF-8') as out_file:
    #     d['Sheet1'].to_string(out_file)
    # 方式2
    d['Sheet1'].to_csv(res_dir_path + txt_name, sep='\t', index=False)
