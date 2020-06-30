__all__ = ['add', 'get', 'getname', 'geturl', 'rm']


import os
import subprocess


"""
https://github.com/owner/repo

git@github.com:owner/repo.git           ssh
https://github.com/owner/repo.git       https

multiple ssh key:
git@owner.github.com:owner/repo.git
git@owner-github.com:owner/repo.git
git@github-owner:owner/repo.git
"""


def _remotes():
    result = []
    for l in os.popen("git remote -v").read().splitlines():
        name, url, role = l.split()
        if "fetch" in role:
            result.append([name, url])
    return result


def add(name, url):
    """`git remote add name url`"""
    args = ["git", "remote", "add", name, url]
    subprocess.check_call(args)


def get():
    """return git remote tuple (name, url)"""
    for name, url in _remotes():
        if "git@" in url and "github" in url.split("@")[1]:
            return name, url
        if "https://" in url and "github" in url.split("/")[2]:
            return name, url


def getname():
    """return git remote name"""
    name, url = get() or (None, None)
    return name


def geturl():
    """return git remote url"""
    name, url = get() or (None, None)
    return url


def rm():
    """`git remote rm name`"""
    name = getname()
    if name:
        args = ["git", "remote", "rm", name]
        subprocess.check_call(args)
