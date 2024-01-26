# setup.py
from setuptools import setup, find_packages

setup(
    name='econsimulation',
    version='0.1.0',
    packages=find_packages(),
    py_modules=['econsimulation.py']
    install_requires=[
        'matplotlib',
        'scipy',
        'numpy',
        'pandas',
        'google-colab'
    ])
