from setuptools import setup, find_packages


setup(
    name="Bucket",
    version="0.1dev",
    license="MIT License",
    author="Angus S. Hilts",
    author_email="grimeyjr@gmail.com",
    long_description=open('README.md').read(),
    packages=find_packages(),
    tests_require=['pytest', 'pytest-cov'],
    test_suite="tests",
    install_requires=[
        'pyfastx',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': ['aminocount=aminocount:main', 'aminodist=aminodist:main'],
    }
)
