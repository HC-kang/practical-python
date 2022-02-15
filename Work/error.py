def grok():
    pass
    raise RuntimeError('Whoa')

def spam():
    grok()
    
def bar():
    try:
        spam()
    except RuntimeError as e:
        print(e)
        
def foo():
    try:
        bar()
    except RuntimeError as e:
        print(e)
        
foo()

grok()

spam()

bar()

foo()