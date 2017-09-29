#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import json

"""
версия модуля с использованием контекстного менеджера with
для записи данных в файл.
основная версия кода модуля.
"""

all_file_list = []

module_name = sys.argv[0]

if sys.argv[1] is None:
    config_file_name = 'config.json'
else:
    config_file_name = sys.argv[1]

with open(config_file_name, 'r') as config_file:
    config_param = json.loads(config_file.read())

name_res_file = config_param['name_res_file']
chunk_dimension = config_param['chunk_size'][1]

# TODO: реализовать функцию удаляющую или создающую новую версию результирующего файла

if chunk_dimension.lower() == 'kb':
    list_size = config_param['chunk_size'][0] * 1024
elif chunk_dimension.lower() == 'mb':
    list_size = config_param['chunk_size'][0] * 1024 * 1024
elif chunk_dimension.lower() == 'b':
    list_size = config_param['chunk_size'][0]
else:
    list_size = 512

for dir_path, subdir_list, files_list in os.walk(os.getcwd()):
    for f in files_list:
        full_name = os.path.join(os.path.abspath(os.path.normcase(dir_path)), f)
        size = os.path.getsize(full_name)
        row = full_name + '\t' + str(size) + '\n'
        all_file_list.append(row)
        if sys.getsizeof(all_file_list) >= list_size:
            with open(name_res_file, 'a') as res_file:
                res_file.writelines(all_file_list)
                res_file.write('===================================\n\n')
            del all_file_list[:]