from setuptools import find_packages, setup

setup(
    name='aws-utils',
    packages=find_packages(include=['kinesis']),
    version='0.1.0',
    description='AWS utils',
    author='Hans Ahrenberg',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.2'],
    test_suite='tests',
)