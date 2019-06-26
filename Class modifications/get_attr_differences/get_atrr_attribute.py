class C(object):
   x = None
   def __getattr__(self, name):
       print('__getattr__', name)
       #raise AttributeError
   def __getattribute__(self, name):
       print('__getattribute__',name)
       if name == 'whoops':
           raise AttributeError
       return object.__getattribute__(self, name)
   def metoda(self): pass

c = C()
c.x
print
c.metoda()
print
c.a
print
c.whoops
print

