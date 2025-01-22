class Test: 
    def __init__(self, foo): 
        self.foo = foo 
    
    def resetFoo(self, foo): 
        self.foo = foo 


T = Test('hi') 
print(T.foo) 

T.resetFoo('ho') 
print(T.foo)