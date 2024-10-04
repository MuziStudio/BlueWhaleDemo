#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    # 自动加载蓝鲸框架所需的环境变量
    load_dotenv(dotenv_path="test.env", verbose=True)
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
