#!/usr/bin/env python
from distutils.core import setup

long_description = open('README.rst').read()

setup(name='OpenElections',
      version='0.1.0',
      description='Election results data for humans',
      long_description=long_description,
      author='Serdar Tumgoren',
      author_email='zstumgoren@gmail.com',
      url='https://github.com/zstumgoren/OpenElections',
      license='MIT License',
      packages=['openelections'],
      platforms=['any'],
      classifiers=[
          'Development Status :: 1 - Planning',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries',
      ]
)
