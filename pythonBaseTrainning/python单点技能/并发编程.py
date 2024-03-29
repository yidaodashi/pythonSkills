# _*_ coding = utf-8 _*_
# @Date : 2022/1/6
# @Time : 13:33
# @NAME ：molin

'''
    一、并发涉及概念：并行、串行、并发、同步、异步、阻塞、非阻塞、线程、进程、协程
    并发是指在同一个处理器上通过时间片轮转的方式在多个线程之间频繁切换，由于切换速度极快，所以看似多个线程似乎被同时执行，但实际上每一个时刻都只有一个线程被执行，其他的线程出于阻塞状态。
　　 并行是指多个处理器在同一时刻同时处理了多个不同的线程，这才是真正意义的同时被执行。
    串行是指多个任务时，各个任务按顺序执行，完成一个之后才能进行下一个
    ****注意：
    所以，并发与并行是在某一时刻是否都在执行的区别。并行与串行是同时进行或一个结束才进行下一个的区别

    同步与异步的概念与消息的通知机制有关：
　　同步是指线程在访问某一资源时，获得了资源的返回结果之后才会执行其他操作，否则主动继续获取这一资源；
　　异步与同步相对，是指线程在访问某一资源时，无论是否取得返回结果，都进行下一步操作；当有了资源返回结果时，系统自会通知线程。

    阻塞是与非阻塞都是程序的一种运行状态。
　　线程在等待某个操作完成期间，自身无法继续执行别的操作，则称该线程在该操作上是阻塞的。
　　线程在等待某个操作完成期间，自身可执行别的操作，则称该线程在该操作上是非阻塞的

    进程和线程：
    线程是指进程内的一个执行单元,也是进程内的可调度实体。线程与进程的区别:
　　1) 地址空间:线程是进程内的一个执行单元，进程内至少有一个线程，它们共享进程的地址空间，而进程有自己独立的地址空间；
　　2) 资源拥有:进程是资源分配和拥有的单位,同一个进程内的线程共享进程的资源；
　　3) 线程是处理器调度的基本单位,但进程不是；
　　4) 二者均可并发执行
　　5) 每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口，但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。

    进程、线程和协程
    一个线程可以多个协程，一个进程也可以单独拥有多个协程，这样python中则能使用多核CPU。
　　2) 线程进程都是同步机制，而协程则是异步
　　3) 协程能保留上一次调用时的状态，每次过程重入时，就相当于进入上一次调用的状态。
'''
