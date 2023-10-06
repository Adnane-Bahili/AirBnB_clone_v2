#!/usr/bin/python3
"""Generates a .tgz archive using Fabric"""
import os
from datetime import datetime
from fabric.api import local, runs_once


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
