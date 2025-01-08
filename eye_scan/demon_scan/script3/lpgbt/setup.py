#!/usr/bin/python3
"""Setuptools description for lpgbt_control_lib"""

import setuptools

setuptools.setup(
    name="lpgbt_control_lib",
    version="3.0.1",
    description="lpGBT ASIC driver library",
    author="lpGBT design team, CERN",
    packages=["lpgbt_control_lib"],
    include_package_data=True,
    install_requires=["numpy", "matplotlib"],
)
