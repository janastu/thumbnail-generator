import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
#README = open(os.path.join(here, 'README.rst')).read()
#CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'epeg-cffi',
    'click'
]

setup(name='thumbnail-generator',
      version='0.1',
      description='A script for generating thumbnails. Uses epeg-cffi to generate thumbnails.',
      license='BSD',
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Environment :: Command Line",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
      ],
      author='Arvind',
      url='https://github.com/janastu/thumbnail-generator',
      keywords='thumbnail, epeg',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires)
