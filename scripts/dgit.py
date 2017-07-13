#! /usr/bin/env python3

import os
import git
import click
import fullpath



@click.version_option()


@click.command()
@click.option('--repo', default=os.getcwd(), prompt= 'Repo Path?')
def get_repo(repo):
    click.echo('Repo selected: {} Path: {}'.format(repo, fullpath.fullpath(repo)))
    Config.repo = git.Repo(repo)
    print(Config.repo)
if __name__ == '__main__':
    get_repo()
