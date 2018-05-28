class D:
    pass 
class A(object):
    """docstring for A"""
    def __init__(self):
        super(A, self).__init__()
        print('A的构造方法正在被调用')
        

class B(A):
    def __init__(self):
        print('B的构造方法正在被调用')
     
class C(B):
    """docstring for C"""
    def __init__(self,name='py'):
        super(C, self).__init__()
        print('C的构造方法正在被调用')
        self.name=name
        
class D:
    pass    
c=C()
c1=c
print(type(c),type(A),)
print(help(property))