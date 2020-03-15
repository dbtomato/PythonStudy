---
title: 13 - IO操作 - 文件读写
tags: open,file-like,close(),StringIO,BytesIO,with open,with,read,write
renderNumberedHeading: true
grammar_cjkRuby: true
---

Author:  Qiao My
Create_Time: 2020-3-11

[toc]


在磁盘上读写文件的功能是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象(文件描述符)，然后，通过操作系统提供的接口从这个文件的对象中读取数据(读文件)，或者把数据写入这个文件对象(写文件)。


# 一、`open` 函数
语法格式：
```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。
```python
open(file, 'r')
open(file, 'r', encoding='utf-8')
```
`open()`函数打开文件成功，返回一个 类文件对象`file-like Object`，失败则报错。
`open()`函数操作的传入参数，可以是**file、内存的字节流、网络流、自定义流**等等

类文件对象`file-like Object`，open()打开的文件在Python中的抽象表示，不需要从特定类继承。
`StringIO`就是在内存中创建的file-like Object，常用作临时缓冲。

**注意：==使用 open() 函数一定要保证关闭文件对象，即调用 close() 函数。 #ff0000==**

## 1. 参数说明

- `file`: 必需，文件路径（相对或者绝对路径）。
- `mode`: 可选，文件打开模式
- `buffering`: 设置缓冲
- `encoding`: 一般使用utf8，默认为None，使用操作系统默认编码
- `errors`: 报错级别
- `newline`: 区分换行符
- `closefd`: 传入的file参数类型
- `opener`:

### mode 参数
下面这张图来自于菜鸟教程网站，它展示了如果根据应用程序的需要来设置操作模式。
![](./images/1583923460719.png)

| 模式 | 描述 |
| --- | --- |
|t   |文本模式 (默认)。|
|x   |写模式，新建一个文件，如果该文件已存在则会报错。|
|b   |二进制模式。|
|+   |打开一个文件进行更新(可读可写)。|
|U   |通用换行模式（不推荐）。|
|r   |以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。|
|rb  |以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。|
|r+  |打开一个文件用于读写。文件指针将会放在文件的开头。|
|rb+ |以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。|
|w   |打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被覆盖删除。如果该文件不存在，创建新文件。|
|wb  |以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。|
|w+  |打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。|
|wb+ |以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。|
|a   |打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。|
|ab  |以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。|
|a+  |打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。|
|ab+ |以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。|
默认为文本模式，如果要以二进制模式打开，加上 `b` 。


### buffering 参数
0 : 表示buffer关闭(只适用于二进制模式)
1 : 表示line buffer (只适用于文本模式)
>1: 表示初始化的 buffer 大小

### errors 参数
strict : 字符编码出现问题时会报错
ignore : 字符编码出现问题时程序会忽略而过，继续执行下面的程序

### closefd
True : 传入的file 参数为文件的文件名
False: 传入的file 参数只能是文件描述符
Ps : 文件描述符，非负整数，在Unix内核的系统中，打开一个文件，便会返回一个文件描述符


# 二、File(file-like Object) 方法
file(file-like Object 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：

| 方法 | 描述 |
| --- | --- |
| file.close() | 关闭文件。关闭后文件不能再进行读写操作。 |
| file.flush() | 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。 |
| file.fileno() | 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的 read方法等一些底层操作上。 |
| file.isatty() | 如果文件连接到一个终端设备返回 True，否则返回 False。 |
| file.next() | 返回文件下一行。 |
| file.read([size]) | 从文件读取指定的字节数，如果未给定或为负则读取所有。 |
| file.readline([size]) | 读取整行，包括 `\n` 字符。 |
| file.readlines([sizehint]) | 读取所有行并返回列表，若给定`sizehint>0`，返回总和大约为 sizehint 字节的行, 实际读取值可能比 sizehint 较大, 因为需要填充缓冲区。 |
| file.seek(offset[, whence]) | 设置文件当前位置
| file.tell() | 返回文件当前位置。 |
| file.truncate([size]) | 截取文件，截取的字节通过 size指定，默认为当前文件位置。 |
| file.write(str) | 将字符串写入文件，返回的是写入的字符长度。 |
| file.writelines(sequence) | 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。 |

## 1. read()、readline()、readlines() 读文件

| 方法 | 读取机制|
| - | - |
| read() | 一次读取全部内容 |
| readline() | 每次读取一行 |
| readlines() | 一次读取全部内容，并返回`list` |
| read(size) | 一次读取size 个字节 |
### read()
`read()`方法一次读取文件全部内容到内存中，用一个`str`对象表示。

```python
f=open('/Users/michael/notfound.txt', 'r')
f.read()
```
由于read()方法会一次性读取文件全部内容，当文件较大时内存吃不消，因此，如果不确定文件的大小，**反复调用read(size) 方法比较安全**

### readline()
调用 readline() 可以每次读取一行内容
例：
```python
f=open('/Users/michael/notfound.txt', 'r')
f.read()
```

### readlines()
调用 readlines() 一次读取全部内容，并按行返回 list。
例：
```python
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
```

## 2. write() 写文件
调用open()函数时，传入标识符`w`或者`wb`表示写文本文件或写二进制文件。
例：
```python
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()
```

## 3. try...finally
文件读写时可能产生`IOError`，一旦出错，后面的close()方法就不会调用，无法正确关闭文件。
try...finally 可以解决这个问题
例：
```python
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
```

## 4. with open() as
通过with 关键字指定对象的上下文环境，并在离开上下文环境时自动释放文件资源。
`try...finally`未免繁琐，且存在漏写finally的情况，通过`with as` 实现更简便、安全。
```python
with open('/path/to/file', 'r') as f:
    print(f.read())
```

# 三、StringIO 和 BytesIO
数据读写不一定是文件，也可以在内存中读写。

## 1. StringIO
StringIO 表示在内存中读写 str。
把str写入StringIO，需要先创建一个 StringIO，然后像文件一样写入即可。
例：
```python
from io import StringIO
>>> f = StringIO()
>>> f.write('hello')
5
>>> f.write(' ')
1
>>> print(f.getvalue())
hello world!
```
`getvalue()` 方法用于获得写入后的str。

读取 StringIO，像读取文件一样读取即可。
```python
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
```

## 2. BytesIO
StringIO只能操作str，BytesIO用来操作二进制数据。
BytesIO实现了再内存中读写bytes。
例：
```python
>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))
6
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'
```
读取 BytesIO
例：
```python
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
b'\xe4\xb8\xad\xe6\x96\x87'
```

# 四、file() 函数
python2中可以通过file函数生成文件对象的方式操作文件，但不建议使用。Python3中移除了file函数。










