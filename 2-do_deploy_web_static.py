#!/usr/bin/python3
"""Web application deployment using Fabric"""
import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once

"""host servers list"""
env.hosts = ["54.197.95.192", "34.207.120.158"]


@runs_once
def do_pack():
    """Archives files"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    cur_time = datetime.now()
    rslt = "versions/web_static_{}{}{}{}{}{}.tgz".format(
                                                            cur_time.year,
                                                            cur_time.month,
                                                            cur_time.day,
                                                            cur_time.hour,
                                                            cur_time.minute,
                                                            cur_time.second)
    try:
        print("Packing web_static to {}".format(rslt))
        local("tar -cvzf {} web_static".format(rslt))
        archize_size = os.stat(rslt).st_size
        print("web_static packed: {} -> {} Bytes".format(rslt, archize_size))
    except Exception:
        rslt = None
    return rslt


def do_deploy(archive_path):
    """Deploys files to host servers"""
    if not os.path.exists(archive_path):
        return False
    f1le = os.path.basename(archive_path)
    fldr_name = f1le.replace(".tgz", "")
    fldr_path = "/data/web_static/releases/{}/".format(fldr_name)
    good = False
    try:
        put(archive_path, "/tmp/{}".format(f1le))
        run("mkdir -p {}".format(fldr_path))
        run("tar -xzf /tmp/{} -C {}".format(f1le, fldr_path))
        run("rm -rf /tmp/{}".format(f1le))
        run("mv {}web_static/* {}".format(fldr_path, fldr_path))
        run("rm -rf {}web_static".format(fldr_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(fldr_path))
        print('New version deployed!')
        good = True
    except Exception:
        good = False
    return good


def deploy():
    """Archives and deploys the static files to the host servers.
    """
    arch_path = do_pack()
    return do_deploy(arch_path) if arch_path else False
