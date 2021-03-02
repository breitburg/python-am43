from setuptools import setup, find_packages

setup(
    name='am43',
    version='1.1.0',
    author='Ilya Breitburg',
    author_email='me@breitburg.com',
    description='AM43 blinds motor API implementation written on Python',
    url='https://github.com/breitburg/python-am43',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=['bluepy>=1.3.0', 'munch>=2.5.0'],
    python_requires='>=3.6'
)
