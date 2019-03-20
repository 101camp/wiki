# -*- coding: utf-8 -*-

import time
import os

from invoke import task
#from fabric.context_managers import cd
env = {'deploy_path':'docs'
    ,'static_path': '_static'
} 


@task 
def bu(c):
    c.run('pwd')
    c.run('markdoc build', hide=False, warn=True)
    c.run('rsync -avzP4 {static_path}/media/ {deploy_path}/media/ '.format(**env))

@task 
def pu(c):
    _ts = '{}.{}'.format(time.strftime('%y%m%d %H%M %S')
                     , str(time.time()).split('.')[1][:3] )

    c.run('pwd')
    c.run('git st', hide=False, warn=True)
    c.run('git add .', hide=False, warn=True)
    c.run('git ci -am '
          '"inv(loc) MkDocs upgraded by DAMA (at %s)"'% _ts
                    , hide=False, warn=True)
    c.run('git pu', hide=False, warn=True)

@task 
def ccname(c):
    c.run('cp CNAME docs/', hide=False, warn=True)
    c.run('ls docs/', hide=False, warn=True)
    c.run('pwd')

#@task 
def gh(c):
    _ts = '{}.{}'.format(time.strftime('%y%m%d %H%M %S')
                     , str(time.time()).split('.')[1][:3] )

    os.chdir('site')
    #with cd('site/'):
    c.run('pwd')
    c.run('ls')
    c.run('git st', hide=False, warn=True)
    c.run('git add .', hide=False, warn=True)
    c.run('git ci -am '
          '"pub(site) gen. by MkDocs as invoke (at %s)"'% _ts
                    , hide=False, warn=True)
    c.run('git pu', hide=False, warn=True)

@task 
def pub(c):
    bu(c)
    ccname(c)
    pu(c)
    #gh(c)

#@task()
def hollo(c):
    c.run('echo hello', hide=False, warn=True)
    c.run('whoami')

