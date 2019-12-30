from setuptools import setup 
import sys 

for p in sys.path:
    print(p)

setup(
    name="microblog-CLI",
    version='1.0',
    packages=['cli'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points="""
    [console_scripts]
    cli_main=cli.cli_main:cli
    """,
)