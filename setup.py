from setuptools import setup, find_packages

setup(
    name="econsimulation",
    version="0.0.2",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scipy",
        "matplotlib",
        "google-colab",
    ],
    py_modules=["econsimulation"],
)
