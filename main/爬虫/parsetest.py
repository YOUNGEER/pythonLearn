from urllib import request,parse

if __name__ == '__main__':
    url='https://www.baidu.com/s?'

    wd=input('input your searach：')

    qs={
        'wd':wd
    }
    qs=parse.urlencode(qs)

    fullurl=url+qs
    resp=request.urlopen(fullurl)
    html=resp.read()
    print(html)