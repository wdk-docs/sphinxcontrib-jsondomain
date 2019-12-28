#!/usr/bin/env python

import os.path

import setuptools
from setuptools import setup, find_packages

with open('README.rst', 'r') as f_readme:
    long_desc = f_readme.read()


def read_requirements(name):
    requirements = []
    with open(os.path.join('requires', name)) as req_file:
        for line in req_file:
            if '#' in line:
                line = line[:line.index('#')]
            line = line.strip()
            if line.startswith('-r'):
                requirements.extend(read_requirements(line[2:].strip()))
            elif line and not line.startswith('-'):
                requirements.append(line)
    return requirements


setuptools.setup(
    name='sphinxcontrib-jsondomain',
    version='2.0.19',
    url='https://github.com/wdk-docs/sphinxcontrib-jsondomain',
    download_url='',
    license='BSD',
    author='Band Cap',
    author_email='bandcap@d3f.pw',
    maintainer='Band Cap',
    maintainer_email='bandcap@d3f.pw',
    description='Sphinx "jsondomain" extension: Describe JSON document structures in sphinx',
    long_description=long_desc,
    zip_safe=False,
    install_requires=read_requirements('installation.txt'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Framework :: Sphinx :: Extension',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=['sphinxcontrib'],
)
