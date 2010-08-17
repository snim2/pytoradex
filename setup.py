from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pytoradex',
      version=version,
      description="Python wrappers to the Oak series of sensors sold by Toradex",
      long_description="""Python wrappers to the Oak series of sensors sold by toradex.com.

Requires python-hid which can be found here: http://libhid.alioth.debian.org/

This code is kept on Github: http://github.com/snim2/pytoradex
Please read the README for more details.
""",
      classifiers=["Topic :: System :: Hardware :: Hardware Drivers",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   "Topic :: Software Development :: Embedded Systems"], 
      keywords='sensor toradex oak',
      author='Sarah Mount',
      author_email='s.mount@wlv.ac.uk',
      url='http://snim2.org',
      license='GPL2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools'
        # 'hid' NOT IN CHEESE SHOP!
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
