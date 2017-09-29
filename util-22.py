#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import json
import logging

"""
версия модуля с использованием контекстного менеджера with
для записи данных в файл.
основная версия кода модуля.
"""

# создаём объект-logger с именем = имени модуля 
logger = logging.getLogger(__name__) 
# задаём общий уровень логгирования для logger'a 
logger.setLevel(logging.DEBUG)
# задаем формат строки сообщения лога
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
# создаем обработчик лога для консоли
console_handler = logging.StreamHandler(sys.stderr) 
# задаем для конкретного обработчика формат строки лога
console_handler.setFormatter(formatter) 
# задаем минимальный приоритет логирования для конкретного обработчика
console_handler.setLevel(logging.DEBUG) 
# подключаем обработчик к логгеру
logger.addHandler(console_handler) 
# задаем обработчик лога для вывода в файл
file_handler=logging.FileHandler('util-2.log', 'w') 
# задаем минимальный приоритет логгирования для конкретного обработчика
file_handler.setLevel(logging.WARNING) 
# задаем для конкретного обработчика формат строки лога
file_handler.setFormatter(formatter) 
# подключаем обработчик к логгеру
logger.addHandler(file_handler)

logger.info("Start initialization...")
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

logger.info("...finish initialization")
logger.info("Start collecting data...")

for dir_path, subdir_list, files_list in os.walk(os.getcwd()):
    logger.info("Generation next pass")
    for f in files_list:
        logger.info("Create next row")
        full_name = os.path.join(os.path.abspath(os.path.normcase(dir_path)), f)
        size = os.path.getsize(full_name)
        row = full_name + '\t' + str(size) + '\n'
        all_file_list.append(row)
        if sys.getsizeof(all_file_list) >= list_size:
            logger.info("Start of writing data block into the file...")
            with open(name_res_file, 'a') as res_file:
                res_file.writelines(all_file_list)
                res_file.write('===================================\n\n')
            logger.info("...finish of writing data block into the file")
            del all_file_list[:]
            logger.info("List of collecting data is empty")
logger.info("...finish collecting data")