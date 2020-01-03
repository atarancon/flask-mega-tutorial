import click 
import subprocess

@click.command()
@click.argument('path', default='app')
def cli(path):
    """
    Run a test  for coverage report

    :param path: Test coverage path 
    :return: Subprocess call result
    """
    cmd = 'py.test  --cov-report term-missing --cov {0}'.format(path)
    print(cmd)
    return subprocess.call(cmd, shell=True)

