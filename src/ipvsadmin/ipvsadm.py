from django.conf import settings
import os
from subprocess import call
import subprocess

__LVS_MODE = {'TCP':'-t','UDP':'-u','FWM':'-f'}
__RS_MODE = {'MASQ':'-m','ROUTE':'-g'}

def ipvadmin_exists():
    return os.path.exists(settings.IPVSADMIN)

def delete_virtual_server(mode,port):
    command = [settings.IPVSADMIN,]
    command.append('-D') 
    command.append(__LVS_MODE[mode])
    command.append(port)
    return call(command,stderr=subprocess.STDOUT)

    
def delete_real_server(mode,port,realserver):
    command = [settings.IPVSADMIN,]
    command.append('-d') 
    command.append(__LVS_MODE[mode])
    command.append(port)
    command.append('-r')
    command.append(realserver)  
    return call(command,stderr=subprocess.STDOUT)
    
def weight_real_server(mode,port,realserver,weight,realsmode):
    command = [settings.IPVSADMIN,]
    command.append('-e') 
    command.append(__LVS_MODE[mode])
    command.append(port)
    command.append('-r')
    command.append(realserver)
    command.append('-w')
    command.append(weight) 
    command.append(__RS_MODE[realsmode])    
    return call(command,stderr=subprocess.STDOUT)