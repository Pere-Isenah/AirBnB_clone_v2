#!/usr/bin/python3
"""Generates a .tgz archive from the contents of web_static using fabric"""
import os
from datetime import datetime
from fabric.api import *

host_1 = os.getenv('WEB01_HOST') 
host_2 = os.getenv('WEB02_HOST') 
user = os.getenv('SVR_USER')
env.hosts = "54.166.128.87"
env.user = "ubuntu"

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
    
def do_deploy(archive_path):
    """deploys the archive to the servers and updates it"""
    if not os.path.isfile(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        # on the web server
        filename = os.path.basename(archive_path)
        fname = filename.split('.')[0]
        folder_name = '/data/web_static/releases/' + fname
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(filename, folder_name))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(filename))

        # Move content out of the sub-folder
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(fname, fname))

        # Delete the symbolic link /data/web_static/current from the web server
        run('rm -rf /data/web_static/current')

        # Create a new the symbolic link /data/web_static/current on the
        # web server linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        run('ln -s {} /data/web_static/current'.format(folder_name))

        return True
    except Exception:
        return False