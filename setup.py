#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

import humilis_streams.metadata as metadata


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError, RuntimeError):
    if os.path.isfile("README.md"):
        long_description = open("README.md").read()
    else:
        long_description = metadata.description

setup(
    name=metadata.project,
    include_package_data=True,
    packages=find_packages(),
    version=metadata.version,
    author=metadata.authors_string,
    author_email=metadata.emails[0],
    url=metadata.url,
    license=metadata.license,
    description=metadata.description,
    long_description=long_description,
    install_requires=[
        "humilis>=0.3.0"],
    classifiers=[
        "Programming Language :: Python :: 3"],
    zip_safe=False,
    entry_points={
        "humilis.layers": [
            "streams=humilis_streams.__init__:get_layer_path"]}
)
