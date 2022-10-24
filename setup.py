from setuptools import setup, find_packages

setup(
    name='engbricks',
    version='0.1.0',
    packages=find_packages(include=['engbricks', 'engbricks.*']),
    install_requires=[
        'selenium==4.5.0',
        'sympy==1.11.1',
    ]
)