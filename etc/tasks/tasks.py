import os
import yaml
from invoke import Collection, task
from utils import get_config, get_path
from shutil import copyfile


@task
def build(ctx, token):
    config = get_config(token)
    path = get_path()
    token = config['token']

    f = open(
        os.path.join(path + '/token_templates/' + token['template'] + '.sol'),
        'r'
    )
    filedata = f.read()
    f.close()

    newdata = filedata.replace(
        "{contract_name}",
        token['contract_name']
    )
    newdata = newdata.replace(
        "{version}",
        token['version']
    )
    for key, value in token['metadata'].items():
        newdata = newdata.replace(
            "{" + key + "}",
            str(value)
        )
    f = open(
        './contracts/' + token['contract_name'] + '.sol',
        'w'
    )
    f.write(newdata)
    f.close()


@task()
def deploy(ctx, environment, token):
    build(token)
    
    ctx.run('truffle deploy ' + environment)
