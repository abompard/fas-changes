from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="fedora-fas-changes",
    version="0.0.1",
    author="Aurélien Bompard",
    author_email="abompard@fedoraproject.org",
    description="A very basic app to get the last changed users from FAS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abompard/fas-changes",
    packages=find_packages(),
    install_requires=[
        "flask",
        "psycopg2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
