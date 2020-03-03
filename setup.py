import os

from setuptools import find_packages, setup

from trsmagnet2torrent import __version__

setup(
    name="trs-magnet2torrent",
    version=__version__,
    description="Turn a magnet link into a torrent",
    license="MIT",
    include_package_data=True,
    install_requires=["magnet2torrent>=1.0.2,<2.0.0",],
    packages=find_packages(),
    keywords=["tridentstream,plugin_type:magnetresolver"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
