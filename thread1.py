import threading
import time
def func1(x,y):
    for i in range(x,y):
        print("func1",i)
        time.sleep(2)
def func2(a,b):
    for i in range(a,b):
        print("func2",i)
        time.sleep(1)
t1=threading.Thread(target=func1,args=(2,9))
t2=threading.Thread(target=func2,args=(15,18))
t1.start()
t2.start()
