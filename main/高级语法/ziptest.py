import zipfile

# 压缩文件实例对象
zf=zipfile.ZipFile('p0.py')

# 解压缩
zf2=zf.extractall('dd')