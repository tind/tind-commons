import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(name="tind-commons",
                 version="0.1",
                 author="TIND",
                 author_email="tech@tind.io",
                 description="Reusable Python libraries for TIND",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/tind/tind-commons",
                 packages=setuptools.find_packages(),
                 classifiers=["Programming Language :: Python",
                              "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent"],
                 python_requires=">=2.7")
