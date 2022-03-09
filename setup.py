from setuptools import setup, find_namespace_packages

from cleaner_data import __version__


setup(
    name="cleaner_data",
    version=__version__,
    url="https://github.com/cleaner-bot/cleaner-data",
    author="Leo Developer",
    author_email="git@leodev.xyz",
    description="data of the cleaner",
    packages=find_namespace_packages(include=["cleaner_data*"]),
)
