import salt
import subprocess
import salt.config
import salt.loader


def hello():
  return "hello world"

def dirs():
   output = subprocess.Popen(["ls", "-l","/etc/salt"], stdout=subprocess.PIPE).communicate()[0]
   return(output)
def grain():
   __opts__ = salt.config.minion_config('/etc/salt/minion')
   __grains__ = salt.loader.grains(__opts__)
   return (__grains__['ip_interfaces'])
