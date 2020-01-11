#!/usr/bin/python3
# Fabric script

from datetime import datetime
from os.path import isfile
from fabric.api import env, local, put, run


env.user = 'ubuntu'
env.hosts = ['35.237.207.79', '34.74.214.218']


def do_pack():
    """Converts web_static into a .tgz file"""
    time = datetime.now()
    file = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second
    )
    local('mkdir -p versions')
    command = local('tar -cvzf ' + file + ' web_static')
    if command.succeeded:
        return file
    return None


def do_deploy(archive_path):
    """ Distribute an archive to the web servers  """""
    if not isfile(archive_path):
        return False
    put(archive_path, '/tmp/')
    archive = archive_path.replace('.tgz', '')
    archive = archive.replace('versions/', '')
    run('mkdir -p /data/web_static/releases/{}/'.format(archive))
    run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'
        .format(archive, archive))
    run('rm /tmp/{}.tgz'.format(archive))
    run('mv /data/web_static/releases/{}/web_static/* '.format(archive) +
        '/data/web_static/releases/{}/'.format(archive))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(archive))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
        .format(archive))
    print('New version deployed!')
    return True


def deploy():
    """Deploy to all servers"""""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
