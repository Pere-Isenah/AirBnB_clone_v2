#!/usr/bin/python3

from fabric.api import local
import datetime
import os


current_datetime = datetime.datetime.now()

year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
minutes = current_datetime.minute
seconds = current_datetime.second
file_name = "versions/web_static_{year}{month}{day}{hour}{minutes}{second}.tgz"


def do_pack():
    """Create a tar gzipped archive of the directory web_static"""
    try:
        if not os.path.isdir("versions"):
                local("mkdir versions")

        local(f"tar -cvzf {file_name}  web_static/*")
        return file_name
    except Exception:
        return None
