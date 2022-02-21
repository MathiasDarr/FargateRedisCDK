from setuptools import setup, find_packages


setup(
    name="nardis",
    version="0.0.1",
    author="Mathias Darr",
    author_email="mddarr@gmail.com",
    packages=find_packages(),
    entry_points={
        "nardis.init": [],
        "console_scripts": ["nardis = nardis.manage:cli"],
    }
)