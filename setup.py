# setup.py
from setuptools import setup, find_packages

setup(
    name='econsimulation',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'scipy',
        'numpy',
        'pandas',
        'google-colab'
    ],
    entry_points={
        'console_scripts': [
            # Puedes agregar scripts ejecutables aquí si es necesario
        ],
    },
)
