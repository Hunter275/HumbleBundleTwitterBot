# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='HumbleBundleTwitterBot',
    version='0.1.0',
    description='A twitter bot that attempts to redeem HumbleBundle keys from Tweets',
    long_description=readme,
    author='Hunter Thornsberry',
    author_email='hunter@hunterthornsberry.com',
    url='https://github.com/Hunter275/HumbleBundleTwitterBot',
    license=license,
    install_requires=['mechanize', 'ssl', 'urllib'],
    install_requires=["twitter"],
    dependency_links=["git+ssh://git@github.com/bear/python-twitter.git"]
)
