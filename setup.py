from setuptools import setup, find_packages

setup(name='simple-python',
    version='0.0.1',
    description='Simpl Python Client',
    url='https://gitlab.com/fynd/simpl-python',
    author='Gofynd Ops Engineering Team',
    author_email='aggregators@gofynd.com',
    packages=find_packages(".", exclude="tests"),
    install_requires=[
        'certifi==2018.1.18', 'chardet==3.0.4', 'cookies==2.2.1', 'idna==2.6',
        'requests==2.18.4', 'responses==0.8.1', 'six==1.11.0', 'urllib3==1.22'
    ])
