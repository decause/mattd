from setuptools import setup, find_packages
import sys, os

version = '0.1.05'

f = open('README.rst')
lines = f.readlines()
f.close()
long_description="\n".join(lines).split('.. split here')[1]

setup(name='mattd',
      version=version,
      description="Matt Daemon",
      long_description=long_description,
      classifiers=[
          'Environment :: No Input/Output (Daemon)',
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Ralph Bean',
      author_email='ralph.bean@gmail.com',
      url='http://github.com/ralphbean/mattd',
      license='GPLv3+',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "fabulous",
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      scripts=[
          "scripts/mattd"
      ]
      )
