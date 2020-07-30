import os

from setuptools import find_packages, setup

from explorer import __version__

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="django-sql-explorer",
    version=__version__,
    author="Chris Clark",
    author_email="chris@untrod.com",
    description=(
        "A pluggable app that allows users (admins) to execute SQL,"
        " view, and export the results."
    ),
    license="MIT",
    keywords="django sql explorer reports reporting csv database query",
    url="https://github.com/uktrade/django-sql-explorer",
    packages=find_packages(),
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'Django>=1.11.0',
        'sqlparse>=0.1.18',
        'unicodecsv>=0.14.1',
        'six>=1.10.0',
        'django-dynamic-models-readonly>=0.1.1',
        'sqlalchemy>=1.3.15',
        'geoalchemy2>=0.8.4',
    ],
    include_package_data=True,
    zip_safe=False,
)
