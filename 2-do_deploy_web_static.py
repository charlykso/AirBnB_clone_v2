#!/usr/bin/python3
from fabric.api import *
from os.path import exists
from datetime import datetime
from fabric.api import local
from sys import os

env.hosts = ['18.206.207.45', '100.26.217.196']


def do_pack():
    '''
    Fabric script that generates a .tgz archive from the
    contents of the web_static
    '''
    try:
        filepath = 'versions/web_static_' + datetime.now().\
                   strftime('%Y%m%d%H%M%S') + '.tgz'
        local('mkdir -p versions')
        local('tar -zcvf versions/web_static_$(date +%Y%m%d%H%M%S).tgz\
        web_static')
        print('web_static packed: {} -> {}'.
              format(filepath, os.path.getsize(filepath)))
    except:
        return None


def do_deploy(archive_path):
        """
        Depploy to yoru webs server
    """
        if exists(archive_path) is False:
            return False
        file_name = archive_path.split('/')[1]
        file_path = '/data/web_static/releases'
        try:
            put(archive_path, '/tmp/')
            run('mkdir -p {}{}'.format(file_path, file_name[:-4]))
            run('tar -xzf /tmp/{} -C {}{}/'.format(file_name,
                                                   file_path, file_name[:-4]))
            run('rm /tmp/{}'.format(file_name))
            run('mv {}{}/web_static/* {}{}/'.format(file_path, file_name[:-4],
                                                    file_path, file_name[:-4]))
            run('rm -rf {}{}/web_static'.format(file_path, file_name[:-4]))
            run('rm -rf /data/web_static/current')
            run('ln -s {}{}/ /data/web_static/current'.format(file_path,
                                                              file_name[:-4]))
            return True
        except:
            return False
