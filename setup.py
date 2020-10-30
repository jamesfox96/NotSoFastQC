import io
from setuptools import setup

setup(name='NotSoFastQC',
      description='A tool to generate FastQC-like graphs from a FastQC file',
      long_description=io.open('README.md', encoding='utf-8').read(),
      long_description_content_type='text/markdown',
      version='1.0',
      url='https://github.com/jamesfox96/NotSoFastQC',
      packages=['NotSoFastQC'],
      install_requires=['tabulate>=0.8.7'],
      entry_points={'console_scripts': ['NotSoFastQC=NotSoFastQC.__main__:main']},
      )
