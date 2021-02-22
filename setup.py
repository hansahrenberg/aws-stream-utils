from setuptools import find_packages, setup

setup(
    name='awsutils',
    packages=find_packages(exclude=('build')),
    version='0.1.0',
    description='aws utilities for data development',
    author='Hans Ahrenberg',
    license='LICENSE',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.2'],
    test_suite='tests',
)