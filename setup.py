"""
A Pretty Project Framework

Author: SF-Zhou
Date: 2016-09-21

See:
https://github.com/sf-zhou/prett
"""

from setuptools import setup, find_packages

setup(
    name='prett',
    version='0.0.1',
    description='A Pretty Project Framework',

    url='https://github.com/sf-zhou/prett',

    author='SF-Zhou',
    author_email='sfzhou.scut@gmail.com',

    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='qt ui',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=['PySide', 'typing']
)
