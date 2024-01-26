# setup.py

from setuptools import setup

setup(
    name="econ-simulation",
    version="1.0.0",
    python_requires=">=3.6"
    author="Diego Armando Barquero Sanchez",
    author_email="barquerosanchezdiego@gmail.com",
    description="Una libreria simple en pre-alpha creada para facilitar la computacion y ploteo de ejercicio microeconomicos",
    url="https://github.com/barquerosanchezdiegoarmando/econ-simulation",
    packages=[",'pandas','numpy','scipy','scipy.optimize','matplotlib.pyplot'"],
    install_requires=["google-colab"],
)
