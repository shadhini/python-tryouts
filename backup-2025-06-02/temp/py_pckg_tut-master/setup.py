# the build script for setuptools. It tells setuptools about your package (such as the name and version) as well as which code files to include

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_package_sapm",
    # the distribution name of your package. This can be any name as long as only contains letters, numbers, _ , and -. It also must not already be taken on pypi.org.
    version="0.0.1",
    author="Shadhini Jayatilake",
    author_email="shadhini.jayatilake@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shadhini/py_pckg_tut",
    # the URL for the homepage of the project. For many projects, this will just be a link to GitHub, GitLab, Bitbucket, or similar code hosting service.
    packages=setuptools.find_packages(),
    # list of all Python import packages that should be included in the distribution package. Instead of listing each package manually, we can use find_packages() to automatically discover all packages and subpackages.
    # In this case, the list of packages will be example_package as that’s the only package present.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # gives the index and pip some additional metadata about your package.
    python_requires='>=3.6',
    install_requires=['pymysql',
                      'PyYAML'],
    zip_safe=False,
    include_package_data=True  # to add non-code files specified in "MANIFEST.in" file
)
