from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='root-image-editor',
    version='0.1.0',
    description='A simple image editor to use classic filters',
    long_description=readme,
    author='Lucas Simao and Thais Amorim',
    url='https://github.com/thasmarinho/root-image-editor',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
