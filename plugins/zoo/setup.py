from setuptools import setup

setup(
    name="zoo",
    version="0.1.0",
    packages=["zoo"],
    entry_points="""
        [absorb.plugins]
        zoo=zoo.cli:zoo
    """,
)
