from setuptools import setup

setup(
    name="search4",
    version="1.0.0",
    packages=["search4"],
    url="https://github.com/7rillionaire/Search4",
    license="GPL-3.0",
    author="7rillionaire",
    description="A tool to search a particular username on almost every social platform and tell,"
    " whether the user with that username exists on that site or not.",
    entry_points={"console_scripts": ["search4=search4.search4:main"]},
    install_requires=['requests', 'colorama', 'pyyaml', 'jinja2'],
    data_files=[('search4', ['search4/search4.yml'])]
)
