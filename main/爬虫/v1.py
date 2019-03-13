'''
使用urllib.request解析一个网页，打印内容
'''


from urllib import request

if __name__ == '__main__':
    urls="https://sou.zhaopin.com/?jl=664&kw=android&kt=3"
    rsp=request.urlopen(urls)
    # 读取出来的内容shibuytes
    html=rsp.read()

    # 利用chardet自动检测编码
    cs=chardet.detect(html)

    # 解码成字符串
    html=html.decode()

    print(html)