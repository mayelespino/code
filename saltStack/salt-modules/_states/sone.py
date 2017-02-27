import salt

def printargs(*args, **kwargs):
    return(__salt__['eone.printargs'] (*args, **kwargs))
def hi():
    return(__salt__['eone.hello']
