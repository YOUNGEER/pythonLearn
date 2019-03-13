# 多线程
- thread包有问题，python3改成了_thread

## threading的使用
- 直接利用threading.Thread生成Thread实例
    - t=threading.Thread(target=xxx,args=(xxx,))
    - t.start(),启动多线程
    - t.join():等待多线程执行完成

- 守护线程
    - 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
    - 一般认为，守护线程不重要或者不允许离开主线程独立运行
    - 守护线程案例能否有效果和环境有关
- 线程常用属性
    - threading.currentThread：返回当前线程变量
    - threading.enumerate：返回一个包含正在运行的线程list
    - threading.activeCount:返回正在运行的线程list数量
    - thr.setName：给线程设置名字
    - thr.getName：得到线程的名字
- 直接继承自threading.Thread
    - 直接继承Thread
    - 重写run函数
    - 类实例可以直接运行

- 共享变量
    - 共享变量：当多个线程同时访问一个变量的时候，会产生共享变量的问题
    - 解决：锁，信号灯
    - lock：
        - 是一个标志，表示一个线程在占用一些资源
        - 使用方法
            - 上锁
            - 使用资源
            - 释放锁           
        
    