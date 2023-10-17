from fabric import *

env.hosts=["test@192.168.15.46"]
env.password='test'

#def dir():
    #run('mkdir fabric')
    #print('Directory named fabric has been created on your host network')

def diskspace():
    run('df')