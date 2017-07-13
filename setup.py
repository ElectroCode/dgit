from distutils.core import setup

version_file = open('VERSION', 'r')
version = version_file.read()

setup(
    name = 'dgit',
    version = version,
    packages = [''],
    url = 'https://github.com/ElectroCode/dgit',
    license = 'MIT',
    author = 'Ken Spencer',
    author_email = 'ken@electrocode.net',
    description = '',
    install_requires = [
        'click>=6.7',
        'gitpython>=2.1.5',
        'fullpath',
    ],
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        
    ]
)
