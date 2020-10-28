import io
from setuptools import setup

setup(name='NotSoFastQC',
      description='',
      long_description=io.open('README.md', encoding='utf-8').read(),
      long_description_content_type='text/markdown',
      version='1.0',
      packages=['NotSoFastQC'],
      entry_points={'console_scripts': ['NotSoFastQC=NotSoFastQC.__main__:main']},
)