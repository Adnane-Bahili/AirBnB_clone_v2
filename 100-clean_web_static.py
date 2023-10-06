#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ["54.197.95.192", "34.207.120.158"]
"""host servers list"""


@runs_once
def do_pack():
    """archives files"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    time = datetime.now()
    t_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year, time.month, time.day, time.hour,
        time.minute, time.second)
    try:
        print("archiving web_static to {}".format(t_file))
        local("tar -cvzf {} web_static".format(t_file))
        size_arc = os.stat(t_file).st_size
        print("web_static archived: {} -> {} Bytes".format(t_file, size_arc))
    except Exception:
        t_file = None
    return t_file


def do_deploy(archive_path):
    """deploys files to host servers
    argument:
        archive_path (str): archived files path
    """
    if not os.path.exists(archive_path):
        return False
    fl_nm = os.path.basename(archive_path)
    fldr_nm = fl_nm.replace(".tgz", "")
    fldr_pth = "/data/web_static/releases/{}/".format(fldr_nm)
    done = False
    try:
        put(archive_path, "/tmp/{}".format(fl_nm))
        run("mkdir -p {}".format(fldr_pth))
        run("tar -xzf /tmp/{} -C {}".format(fl_nm, fldr_pth))
        run("rm -rf /tmp/{}".format(fl_nm))
        run("mv {}web_static/* {}".format(fldr_pth, fldr_pth))
        run("rm -rf {}web_static".format(fldr_pth))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(fldr_pth))
        print('files deployed')
        done = True
    except Exception:
        done = False
    return done


def deploy():
    """archives, then deploys files to host servers"""
    arch_pth = do_pack()
    return do_deploy(arch_pth) if arch_pth else False


def do_clean(number=0):
    """cleans out-of-date archives
    argument:
        number (Any): archives to keep count
    """
    archs = os.listdir('versions/')
    archs.sort(reverse=True)
    first = int(number)
    if not first:
        first += 1
    if first < len(archs):
        archs = archs[first:]
    else:
        archs = []
    for archive in archs:
        os.unlink('versions/{}'.format(archive))
    parts = [
        "rm -rf $(",
        "find /data/web_static/releases/ -maxdepth 1 -type d -iregex",
        " '/data/web_static/releases/web_static_.*'",
        " | sort -r | tr '\\n' ' ' | cut -d ' ' -f{}-)".format(first + 1)
    ]
    run(''.join(parts))
