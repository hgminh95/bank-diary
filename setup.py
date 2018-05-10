#!/usr/bin/env python

from distutils.core import setup

setup(name='bank-diary',
      version='1.0',
      author='hgminh',
      packages=[
          'bank_diary',
          'bank_diary.common',
          'bank_diary.classifier',
          'bank_diary.parser'],
      scripts=['bdiary']
     )
