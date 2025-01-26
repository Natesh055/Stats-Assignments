from setuptools import setup,find_packages

setup(
    name='Topsis',
    version='0.1',
    description='A Python package implementing TOPSIS technique.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Natesh Subgh Pundir',
    author_email='npundir_be2@thapa.edu',
    url='https://github.com/Natesh055/Statistics-Assignments',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)