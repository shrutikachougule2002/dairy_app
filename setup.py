from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dairy_app/__init__.py
from dairy_app import __version__ as version

setup(
	name="dairy_app",
	version=version,
	description="Dairy milk products.",
	author="Shruti",
	author_email="chouguleshruti@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
