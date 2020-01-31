#!/usr/bin/env python
import os
from setuptools import setup, find_packages

base = os.path.dirname(os.path.abspath(__file__))

setup(
    name="pelican-export",
    setup_requires=["vcver"],
    vcver={"path": base},
    description="",
    long_description="",
    install_requires=["python-wordpress-xmlrpc", "pelican"],
    author="Yusuke Tsutsumi",
    author_email="yusuke@tsutsumi.io",
    url="https://github.com/toumorokoshi/pelican-to-wordpress",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={},
)
