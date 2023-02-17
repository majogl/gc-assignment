from setuptools import setup, find_packages

setup(
    name='assignment',
    version='0.1.0',
    author='Marian Glatzner',
    author_email='glatzner@gmail.com',
    package_dir={'':'assignment'},
    packages=find_packages('assignment'),
    description='Marian Glatzner programming assignment.',
    long_description=open('README.md').read(),
    install_requires=[
        "requests==2.28.2"
    ],
)