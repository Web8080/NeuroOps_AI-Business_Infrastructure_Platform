# Shared package not installed via pip in Docker; services add shared to path or copy.
# For local dev: pip install -e ./shared (if using setuptools).
from setuptools import setup, find_packages

setup(name="neuroops_common", version="0.1.0", packages=find_packages())
