"""
ABC Library - Sample Python Library
A sample Python library template for demonstration purposes.
"""
# -----------------------------------------------------------
### !!! This file is not needed if pyproject.toml is used
# -----------------------------------------------------------
from setuptools import setup, find_packages

setup(
    name='abc_library',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    url='https://github.com/shadhini/python-tryouts',
    license='MIT',
    author='Shadhini Jayatilake',
    author_email='shadhini.jayatilake@gmail.com',
    description='Sample Python library template for demonstration purposes',
    long_description=open('README.md').read() if __name__ == '__main__' else '',
    long_description_content_type='text/markdown',
    python_requires='>=3.8',
    install_requires=[
        'pandas>=1.5.0',
        'numpy>=1.23.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'black>=22.0.0',
            'flake8>=5.0.0',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.14',
    ],
    zip_safe=True,
    # tells setuptools that the package can be safely installed and run directly from a zipped archive (an \*.egg)
    #   instead of being unpacked to the filesystem.
    #
    # - True: package code and resources do not rely on being real files on disk
    #           (no C extensions, no runtime file access via filesystem paths,
    #           no data files read with open\(\) using package-relative paths)
    # - False: package must be extracted to a directory at install time
    #           (use this if you read package files with normal file APIs or include compiled extensions).
    #
    # Note: modern wheels (\*.whl) are typically installed unzipped,
    #   so this flag mainly affects older egg-based installations.
    include_package_data = True  # to add non-code files specified in "MANIFEST.in" file
)

