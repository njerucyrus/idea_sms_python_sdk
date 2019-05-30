import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='idea_sms_skd',
    version='0.1',
    scripts=['idea_sms_skd'],
    author="Njeru Cyrus",
    author_email="njerucyrus5@gmail.com",
    description="Python package for sending sms with idea sms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/njerucyrus/idea_sms_python_sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)
