from setuptools import setup 
import sys 
sys.path.append("/Users/at/Desktop/Home/flask-mega-tutorial/microblog/cli_package")

for p in sys.path:
    print(p)

setup(
    name="microblog-CLI",
    version='1.0',
    packages=['cli_package'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points="""
        [console_scripts]
        cli_main=cli_package.cli_main:hello
    """,
)