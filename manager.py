# -*- coding: utf8 -*-
import json
import sys
import os
import shutil

from cpbox.tool import file
from cpbox.tool import functocli
from cpbox.tool import template
from cpbox.tool import utils
from cpbox.tool import http

from cpbox.app.devops import DevOpsApp

APP_NAME = 'serverless-thirty'

class App(DevOpsApp):

    def __init__(self):
        DevOpsApp.__init__(self, APP_NAME)

    def send_cmd_to_container(self, container, cmd):
        cmd = 'docker exec -it %s %s' % (container, cmd)
        self.shell_run(cmd)

    def link_node_moduels(self, dir) :
        if (os.path.exists(dir)) {
            rm_dir_cmd = 'rm %s/node_modules' % (dir)
            self.shell_run(rm_dir_cmd)
        }
        ln_cmd = 'ln -sf /opt/node_npm_data/node_modules %s' % (dir)
        self.shell_run(ln_cmd)

    def remove_container(self, container_name):
        cmd = 'docker rm -f %s' % (container_name)
        self.shell_run(cmd)

    def build(self):
        self.shell_run('yum update')

        packages = ['git', 'docker', 'epel-release', 'python2', 'python-pip']
        for package in packages:
            self.shell_run('sudo yum install %s' % (package))

if __name__ == '__main__':
   functocli.run_app(App)
