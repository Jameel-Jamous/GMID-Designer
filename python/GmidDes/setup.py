from setuptools import setup, find_packages

setup(
    name="GmidDes",    
    version="0.0",
    packages=find_packages(),
    install_requires=[],  
    test_suite='nose.collector',
    tests_require=['nose'],
)