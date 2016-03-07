# -*- coding: utf-8 -*-


import inspect
import os


def get_layer_path():
    return os.path.dirname(inspect.getfile(inspect.currentframe()))
