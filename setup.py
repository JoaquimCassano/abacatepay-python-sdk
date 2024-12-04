#!/usr/bin/python
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

requirements = [
    "pydantic",
    "requests"
]

setuptools.setup(
    name="abacatepay",
    version="0.1.0",
    author="Joaquim Cassano",
    license='MIT',
    author_email="joaquim@cassano.com.br",
    description='Python library for communication with the abacatepay api',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    keywords=["api", "abacatepay", "payments", "pix"],
    url="https://github.com/AbacatePay/Python-SDK",
    packages=["abacatepay", "abacatepay.src"],
    package_dir={"abacatepay": "abacatepay", "abacatepay.src": "abacatepay/src"},
    python_requires=">=3.7",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)