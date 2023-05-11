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


def do_pack():
    """Create a tar gzipped archive of the directory web_static"""
    try:
        if not os.path.isdir("versions"):
                local("mkdir versions")

        local(f"tar -czvf versions/web_static_{year}{month}{day}{hour}{minutes}{second}.tgz web_static/*")
    except Exception:
        return None
