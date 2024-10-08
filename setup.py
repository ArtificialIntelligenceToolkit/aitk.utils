# -*- coding: utf-8 -*-
# **************************************************
# aitk.utils: general purpose functions for AI
#
# Copyright (c) 2021 ArtificialIntelligenceToolkit
#
# https://github.com/ArtificialIntelligenceToolkit/
#
# **************************************************

import setuptools

name = "aitk.utils"
version = "2.0.0"
long_description = """
# aitk.utils

DEPRECATED PACKAGE: use `aitk` instead.
"""
print(long_description)
setup_args = dict(
    name=name,
    version=version,
    url="https://github.com/ArtificialIntelligenceToolkit/%s" % name,
    author="Douglas Blank",
    description="A set of generic tools for AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["aitk"],
    python_requires=">=3.6",
    license="BSD-3-Clause",
    platforms="Linux, Mac OS X, Windows",
    keywords=["robot", "simulator", "jupyter", "python"],
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Framework :: Jupyter",
    ],
)

if __name__ == "__main__":
    setuptools.setup(**setup_args)
