dc = {
    1 : 'wink',
    10 : 'double blink',
    100 : 'close your eyes',
    1000 : 'jump'
    }
def handshake(what):
    if isinstance(what,int):
        if what<=0:
            return []
        what = bin(what)[2:]
    else:
        
        if(max([int(i) for i in what]))>1:
            return []
    print(what)
    for cnt,i in enumerate(reversed(what)):
        print(cnt,i)
        #print(bin(what)[2:])
    #print((what))

    
def code():
    pass


handshake(9)
handshake('100')
handshake(-3)
