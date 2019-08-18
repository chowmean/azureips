#!/usr/bin/env python
#
# Python installation script
# Author - @chowmean

from __future__ import print_function
import os.path
import sys
import setuptools

# Project variables
VER_PROP_FILE = os.path.join(os.path.dirname(__file__), 'version.properties')
REQUIREMENTS_FILE = os.path.join(os.path.dirname(__file__), 'requirements.txt')
CLASSIFIERS = [
    "Programming Language :: Python",
    "Operating System :: OS Independent",
    "Intended Audience :: Developers",
    "Development Status :: 4 - Beta",
    "Environment :: Plugins",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "License :: Other/Proprietary License",
    "Natural Language :: English",
]


# Read version properties file and extract version number.
def get_version():
    try:
        with open(VER_PROP_FILE) as f:
            for line in f.readlines():
                if line.startswith("version="):
                    version = line.lstrip('version=').strip()
                    return version
    except IOError as ioe:
        print(ioe, file=sys.stderr)



# Read requirements.txt file and extract the list of dependency.
def get_install_requirements():
    # read requirements
    requires = []
    try:
        with open(REQUIREMENTS_FILE) as f:
            requires = list(map(lambda l: l.strip(), f.readlines()))
    except IOError as ioe:
        print(ioe, file=sys.stderr)
        sys.exit(1)
    return requires


if __name__ == '__main__':

    with open('README.md', 'r') as f:
        readme = f.read()

    setuptools.setup(
        name="azureips",
        version=get_version(),
        description="azureIPs: Gives unallocated Azure ips. ",
        author="chowmean",
        author_email="gaurav.dev.iiitm@gmail.com",
        url="https://github.com/chowmean/azureips",
        keywords=["azureips","azure","network_interface_ips"],
        install_requires=get_install_requirements(),
        packages=["azureips","azureips.utilities"],
        package_data={'': ['LICENSE','requirements.txt','version.properties']},
        classifiers=CLASSIFIERS,
        long_description=readme,
        long_description_content_type="text/markdown",
        license="Apache-2.0"
    )