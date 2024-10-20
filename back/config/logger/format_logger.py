#!/usr/bin/python
# -*- encoding: utf-8 -*-
import sys
import os
from os.path import abspath, dirname, join

base_dir = abspath(dirname("."))
parent_dir = abspath(join(base_dir, ".."))
logs_dir = join(parent_dir, "logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)
logs_target = join(logs_dir, "main_logs.log")

logging_config = {
    "version": 1,
    "formatters": {
        "simple": {
            "class": "logging.Formatter",
            "format": "%(asctime)s - [%(name)s] - [%(levelname)s]:%(message)s",
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "stream": sys.stderr,
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "simple",
            "level": "DEBUG",
            "filename": logs_target,
            "mode": "a",
            "encoding": "utf-8",
            "maxBytes": 500000,
        },
    },
    "root": {"level": "DEBUG", "handlers": ["console", "file"], "propagate": True},
}

