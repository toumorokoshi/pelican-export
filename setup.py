#!/usr/bin/env python
import os
from setuptools import setup, find_packages

base = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base, "README.md")) as fh:
    long_description = fh.read()

setup(
    name="pelican-export",
    setup_requires=["vcver"],
    vcver={"path": base, "is_release": True},
    description="Pelican plugin to export articles to other platforms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
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
