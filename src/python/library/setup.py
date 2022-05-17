from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="yocrypt",
      version="1.0.0",
      description="YoCrypt is a new way to encode and decode text symetrically.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="PetitPotiron",
      packages=["yocrypt"],
      license="MIT License",
      url='https://github.com/PetitPotiron/YoCrypt/blob/main/src/python/library/yocrypt'
      )
