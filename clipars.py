#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse

__version__ = "1.3"

def ini():
    # Создать объект парсера c возможностью вывода справки –h|--help и номера версии –v|--version
    cli_parser = argparse.ArgumentParser(description='Great Description To Be Here', add_help=True, version=__version__)
    # добавить в парсер параметры – аргументы комм.строки
    cli_parser.add_argument('-i', '--interactive', action='store', dest='interact', help='Interactive mode - specifying the parameters of the utility operator')
    cli_parser.add_argument('-c', '--config', action='store', dest='create_config_file', help='Create configuration file')
    cli_parser.add_argument('-ncf', '--not_config', action='store', dest='not_use_config_file', help='Not use existing configuration file')
    cli_parser.add_argument('configuration', help='Specifying')
    cli_parser.add_argument('result', help='A file with the result of program using')

    return cli_parser.parse_args()

args = ini()
print(args.interact)
print(args.configuration)
print(args.result)
