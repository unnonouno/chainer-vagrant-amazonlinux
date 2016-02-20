from fabric.api import sudo


def install_chainer():
    sudo('pip install chainer')
