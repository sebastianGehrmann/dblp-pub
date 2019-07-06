from setuptools import setup

setup(
    name='dblp',
    version='0.1.0',
    author='Sebastian Gehrmann',
    author_email='gehrmann@seas.harvard.edu',
    packages=['dblp'],
    url='https://github.com/sebastianGehrmann/dblp-pub/tree/master',
    license='LICENSE.txt',
    description='Downloads and formats search results from dblp',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "beautifulsoup4>=4.3.2",
        "pandas>=0.16.2",
        "requests>=2.7.0"
    ],
)