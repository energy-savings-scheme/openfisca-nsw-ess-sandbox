# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="openfisca_nsw_ess_sandbox",
    version="0.0.1",
    author="Department of Planning Industry and Environment - NSW Government",
    author_email = 'liam.mccann@environment.nsw.gov.au',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Information Analysis",
        ],
    description="An OpenFisca extension that adds some variables to an already-existing tax and benefit system",
    keywords = 'benefit microsimulation social tax',
    license="http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    url = "https://github.com/Openfisca-NSW/openfisca_nsw_ess_sandbox",
    include_package_data = True,  # Will read MANIFEST.in
    data_files = [
        ("share/openfisca/openfisca_nsw_ess_sandbox", ["CHANGELOG.md", "LICENSE", "README.md"]),
        ],
    install_requires = [
        "OpenFisca-Core[web-api] >= 29.0",
        ],
    extras_require = {
        "dev": [
            "autopep8 == 1.4.0",
            "flake8 >= 3.5.0, < 3.6.0",
            "flake8-print",
            "pycodestyle >= 2.3.0, < 2.4.0",  # To avoid incompatibility with flake
            ]
        },
    packages=find_packages(),
    )
