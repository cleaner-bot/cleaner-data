from setuptools import setup, find_namespace_packages  # type: ignore

from cleaner_data import __version__


def parse_requirements_file(path):
    with open(path) as file:
        lines = file.read().splitlines()
    dependencies = (x.strip() for x in lines)
    return [x for x in dependencies if x and not x.startswith("#")]


setup(
    name="cleaner_data",
    version=__version__,
    url="https://github.com/cleaner-bot/cleaner-data",
    author="Leo Developer",
    author_email="git@leodev.xyz",
    description="data of the cleaner",
    requires=parse_requirements_file("requirements.txt"),
    packages=find_namespace_packages(include=["cleaner_data*"]),
    package_data={"cleaner_data": ["py.typed"]},
)
