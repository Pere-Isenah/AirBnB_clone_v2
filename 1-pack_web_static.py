#!/usr/bin/python3
"""Generates a .tgz archive from the contents of web_static using fabric"""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static"""
    try:
        cdt = datetime.now()
        file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(cdt.year,
                                                                  cdt.month,
                                                                  cdt.day,
                                                                  cdt.hour,
                                                                  cdt.minute,
                                                                  cdt.second)
        if not os.path.isdir("versions"):
            local("mkdir versions")

        local("tar -cvzf {} web_static/*".format(file_name))
        return file_name
    except Exception:
        return None