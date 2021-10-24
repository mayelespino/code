class TestClass(object):
        def __init__(self):
                print 'object = TestClass() ran'
        def __getitem__(self,name):
                print 'var = TestClass[%s] ran' % name
                return 0
        def __setitem__(self,name,value):
                print 'TestClass[%s] = %s ran' % (name, value)
        def __call__(self,printwhat):
                print 'TestClass(%s) ran' % printwhat
                print printwhat
        def __getattr__(self,name):
                print 'var = TestClass.%s ran' % name
		return name
        def __setattr__(self,name,value):
                print 'TestClass.%s = var ran' % name
 
object = TestClass()
var = object['whatever']
object['woohoo'] = 0
object.attribute = 'abc'
print object.attribute
object('Hello, World!')
