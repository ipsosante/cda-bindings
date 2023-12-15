from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cda-bindings",
    version="0.0.3",
    author="ipso santé",
    author_email="contact@ipsosante.fr",
    description="Python bindings for the CDA R2 document format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ipsosante/cda-bindings",
    project_urls={"Bug Tracker": "https://github.com/ipsosante/cda-bindings/issues"},
    license="MIT",
    packages=find_packages(),
    install_requires=[],
)
