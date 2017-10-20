import time
import threading
PRODUCT_SPEED=1 #生产耗时
CONSUM_SPEED=4 #消费耗时
INIT_NUM=0 #仓库初始产品数量
TOTAL_NUM=10 #仓库最大产品容量
FLAG=1
num=INIT_NUM
li=["仓库："]+["*"]*INIT_NUM+["-"]*(TOTAL_NUM-INIT_NUM)
empty=threading.Semaphore(TOTAL_NUM-INIT_NUM)
full=threading.Semaphore(INIT_NUM)
mutex=threading.Semaphore(1)
print("初始化后! 仓库产品总数{0}".format(num))
print(li)
def product():
    time.sleep(PRODUCT_SPEED)
def add_to_lib():
    global num,li
    li[num+1]="*"
    num=num+1
    time.sleep(1)
    print("生产一件! 仓库产品总数{0}".format(num))
    print(li)
    return num
def consum():
    time.sleep(CONSUM_SPEED)
def sub_from_lib():
    global num,li
    li[num]="◻"
    num=num-1
    time.sleep(1)
    print("消费一件! 仓库产品总数{0}".format(num))
    print(li)
    return num
def producer():
    while(FLAG==1):
        empty.acquire()
        product()
        mutex.acquire()
        add_to_lib()
        mutex.release()
        full.release()
def consumer():
    while(FLAG==1):
        full.acquire()
        mutex.acquire()
        sub_from_lib()
        mutex.release()
        empty.release()
        consum()
t1=threading.Thread(target=producer,args=())
t2=threading.Thread(target=consumer,args=())
t1.start()
t2.start()
