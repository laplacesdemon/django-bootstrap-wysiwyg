# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-bootstrap-wysiwyg',
    version='0.1',
    author=u'Suleyman Melikoglu',
    author_email='suleyman@melikoglu.info',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/laplacesdemon/django-bootstrap-wysiwyg.git',
    license='MIT licence, see LICENCE',
    description='A django app that allows you to integrate `bootstrap-wysiwyg` easily.',
    long_description=open('README.md').read(),
    zip_safe=False,
)
