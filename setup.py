import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="old-norwegian-dictionary",
    version="0.9.0",
    author="stscoundrel",
    description="Old Norwegian/Norse Dictionary for Python. From 'Dictionary of the Old Norwegian Language'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stscoundrel/old-norwegian-dictionary-py",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    package_data={"": ["**/*.json"]},
)
