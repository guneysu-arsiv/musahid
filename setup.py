# from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='musahid',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='BSD3',
    author='Ahmed Seref Guneysu',
    author_email='g.seref@yahoo.ca',
    description='',
    install_requires=[
        'tweepy==3.6.0',
    ],

)
