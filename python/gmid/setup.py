from setuptools import setup, find_packages

setup(
    name="gmid",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["click"],
    entry_points={
        "console_scripts" : [
            "gmid=gmid.cli:cli",
        ],
    },
    description="A sample text",
    author="Jameel Jamous",
    author_email="jamjam5050@gmail.com",
)