import configparser
import os
import re

import semver
from invoke import run
from pygit2 import Repository

DEFAULTS = {
    'major_tag': ':boom:',
    'minor_tag': ':sparkles:',
    'patch_tag': ':bug:',
}


def get_current_version():
    return run('python setup.py --version', hide=True).stdout.strip()


def get_new_version(current_version, level_bump):
    return getattr(semver, 'bump_{0}'.format(level_bump))(current_version)


def set_new_version(new_version):
    filename, variable = load_config().get('version_variable').split(':')
    variable = variable.strip()
    with open(filename, mode='r') as fr:
        content = fr.read()

    content = re.sub(
        r'{} ?= ?["\']\d+\.\d+(?:\.\d+)?["\']'.format(variable),
        '{} = \'{}\''.format(variable, new_version),
        content
    )

    with open(filename, mode='w') as fw:
        fw.write(content)
    return True


def load_config():
    config = configparser.ConfigParser()
    with open(os.path.join(os.getcwd(), 'setup.cfg')) as f:
        config.read_file(f)
    settings = {}
    settings.update(DEFAULTS)
    settings.update(config._sections['semantic_release'])
    return settings


def get_commit_log():
    repo = Repository('.git')
    for commit in repo.walk(repo.head.target):
        yield commit.message
