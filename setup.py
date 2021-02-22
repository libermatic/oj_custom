# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in oj_custom/__init__.py
from oj_custom import __version__ as version

setup(
	name='oj_custom',
	version=version,
	description='Customizations for OJ',
	author='Libermatic LLP',
	author_email='info@libermatic.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
