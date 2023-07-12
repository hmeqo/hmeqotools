from pathlib import Path
from setuptools import setup
from setuptools import find_packages

setup(
    name='hmeqotools',
    version='0.1.0',
    description='A simple toolkit for Python.',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
)
