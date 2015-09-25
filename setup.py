from distutils.core import setup

setup(
    name='dblp-pub',
    version='0.1.0',
    author='Sebastian Gehrmann',
    author_email='gehrmann@seas.harvard.edu',
    packages=['dblp-pub'],
    url='https://github.com/sebastianGehrmann/dblp-pub/tree/master',
    license='LICENSE.txt',
    description='Downloads and formats search results from dblp',
    long_description=open('README.md').read(),
    install_requires=[
        "beautifulsoup4>=4.3.2",
        "pandas>=0.16.2",
        "requests>=2.7.0"
    ],
)