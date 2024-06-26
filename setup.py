from setuptools import setup, find_packages

setup(
    name='eda',
    version='0.1',
    py_modules=['edabasic'],
    install_requires=[
        # Lista de dependencias si las tienes
    ],
    author='AImetrics IO',
    author_email='aimetricsio@gmail.com',
    description='Some functions for OHLC vol EDA and dataframe adjustment of eod data',
    url='https://github.com/AImetricsIO/eda',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
