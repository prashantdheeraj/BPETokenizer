
from setuptools import find_packages, setup

setup(
    name='BPETokenizer',
    packages=find_packages(include=['BPETokenizer']),
    version='0.1.0',
    description='My first Python library',
    author='PD',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='Test',
)