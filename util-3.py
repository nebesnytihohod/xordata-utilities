#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import json

'''
версия модуля без блочной записи - весь массив данных
хранится в памяти и после, целиком, записывается в файл на диске.
'''

all_file_list = []

module_name = sys.argv[0]

if sys.argv[1] is None:
    config_file_name = 'config3.json'
else:
    config_file_name = sys.argv[1]

with open(config_file_name, 'r') as config_file:
    config_param = json.loads(config_file.read())

name_res_file = config_param['name_res_file']

# TODO: реализовать функцию удаляющую или создающую новую версию результирующего файла

res_file = open(name_res_file, 'a')

for dir_path, subdir_list, files_list in os.walk(os.getcwd()):
    for f in files_list:
        full_name = os.path.join(os.path.abspath(os.path.normcase(dir_path)), f)
        size = os.path.getsize(full_name)
        row = full_name + '\t' + str(size) + '\n'
        res_file.write(row)