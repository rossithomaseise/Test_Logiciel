import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pastebin",
    version="0.0.1",
    author="Rossi Thomas",
    author_email="",
    description="Package to create data ingestion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #packages=setuptools.find_packages(),
    packages=['codePasteBin'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

