# -*- coding: utf-8 -*-
#
# pyutils setup script
#
# Copyright (C) 2018 Sathya Kuppuswamy
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# @Author  : Sathya Kupppuswamy(sathyaosid@gmail.com)
# @History :
#            @v0.0 - Initial update
# @TODO    :
#
#

from setuptools import setup


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='pyutils',
      version='0.2',
      description='Python utility scripts for automation',
      long_description=readme,
      classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='python git autotesting test scripts shell linux',
      url='https://github.com/knsathya/pyutils.git',
      author='Kuppuswamy Sathyanarayanan',
      author_email='sathyaosid@gmail.com',
      license='GPLv2',
      packages=['pyutils'],
      install_requires=[
          'pyshell',
          'jsonparser',
          'pyyaml'
      ],
      dependency_links=[
          'git+https://github.com/knsathya/pyshell.git#egg=pyshell',
          'git+https://github.com/knsathya/jsonparser.git#egg=jsonparser'
      ],
      test_suite='tests',
      tests_require=[
          ''
      ],
      entry_points={
          'console_scripts': [''],
      },
      include_package_data=True,
      zip_safe=False)
