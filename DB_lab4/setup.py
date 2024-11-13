from setuptools import setup, find_packages

setup(
    name='terminal_service',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'PyMySQL',
        'PyYAML'
    ],
)

