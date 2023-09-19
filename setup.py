
from setuptools import setup, find_packages

setup(
    name="FFup",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'FFup=ffup.FFup:main',
        ],
    },
    author="1e-2",
    description="A tool for batch updating WebUI1111 Extensions & ComfyUI Nodes",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/1e-2/FFup",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
