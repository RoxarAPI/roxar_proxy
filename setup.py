import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="roxar_proxy",
    version="0.0.0",
    author="Havard Bjerke",
    author_email="havard.bjerke@emerson.com",
    description="Roxar mock library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RoxarAPI/roxar_proxy",
    project_urls={
        "Bug Tracker": "https://github.com/RoxarAPI/roxar_proxy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
    packages=["roxar_proxy"],
    python_requires=">=3.6",
)

