from pathlib import Path

from setuptools import find_namespace_packages, setup  # type: ignore

from cleaner_data import __version__

setup(
    name="cleaner_data",
    version=__version__,
    url="https://github.com/cleaner-bot/cleaner-data",
    author="Leo Developer",
    author_email="git@leodev.xyz",
    description="data of the cleaner",
    install_requires=Path("requirements.txt").read_text().splitlines(),
    packages=find_namespace_packages(include=["cleaner_data*"]),
    package_data={"cleaner_data": ["py.typed"]},
)
