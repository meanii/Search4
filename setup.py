from setuptools import setup

setup(
    name="search4",
    version="1.0.0",
    packages=["search4"],
    package_data={'search4': ['search4/*.yml']},
    include_package_data = True,
    url="https://github.com/kisestu/Search4",
    license="GPL-3.0",
    author="0xknown",
    description="Sweet OSINT tool to find people on the social media.",
    entry_points={"console_scripts": ["search4=search4.search4:main"]},
    install_requires=['requests', 'colorama', 'pyyaml', 'jinja2'],
    data_files=[('search4', ['search4/search4.yml'])]
)
