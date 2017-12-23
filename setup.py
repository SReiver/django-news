from distutils.core import setup
from setuptools import find_packages

setup(
    name='news',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    long_description='Simple news module, with pure-pagination and djangocms-text-ckeditor'
)