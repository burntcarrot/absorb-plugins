from setuptools import setup

setup(
    name="myext",
    version="0.1.0",
    packages=["myext"],
    entry_points="""
        [absorb.plugins]
        myext=myext.core:mycommand
    """,
)
