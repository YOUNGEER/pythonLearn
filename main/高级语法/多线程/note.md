# 多线程
- thread包有问题，python3改成了_thread

## threading的使用
- 直接利用threading.Thread生成Thread实例
    - t=threading.Thread(target=xxx,args=(xxx,))
    - t.start(),启动多线程
    - t.join():等待多线程执行完成