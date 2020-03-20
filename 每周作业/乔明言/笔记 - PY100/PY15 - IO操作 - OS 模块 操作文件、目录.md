---
title: 15 - IO操作 - `OS 模块` 操作文件、目录
tags: os,os.path,文件,查看,创建,删除,IO
renderNumberedHeading: true
grammar_cjkRuby: true
---

Author:  Qiao My
Create_Time: 2020-3-11

[toc]


# 一、OS 模块方法

| 方法 | 描述 |
| --- | --- |
| os.access(path, mode) | 检验权限模式 |
| os.chdir(path) | 改变当前工作目录 |
| os.chflags(path, flags) | 设置路径的标记为数字标记。 |
| os.chmod(path, mode) | 更改权限 |
| os.chown(path, uid, gid) | 更改文件所有者 |
| os.chroot(path) | 改变当前进程的根目录 |
| os.close(fd) | 关闭文件描述符 fd |
| os.closerange(fd_low, fd_high) | 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略 |
| os.dup(fd) | 复制文件描述符 fd |
| os.dup2(fd, fd2) | 将一个文件描述符 fd 复制到另一个 fd2 |
| os.fchdir(fd) | 通过文件描述符改变当前工作目录 |
| os.fchmod(fd, mode) | 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。 |
| os.fchown(fd, uid, gid) | 修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。 |
| os.fdatasync(fd) | 强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。 |
| os.fdopen(fd[, mode[, bufsize]]) | 通过文件描述符 fd 创建一个文件对象，并返回这个文件对象 |
| os.fpathconf(fd, name) | 返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。 |
| os.fstat(fd) | 返回文件描述符fd的状态，像stat()。 |
| os.fstatvfs(fd) | 返回包含文件描述符fd的文件的文件系统的信息，像 statvfs() |
| os.fsync(fd) | 强制将文件描述符为fd的文件写入硬盘。 |
| os.ftruncate(fd, length) | 裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。 |
| os.getcwd() | 返回当前工作目录 |
| os.getcwdu() | 返回一个当前工作目录的Unicode对象 |
| os.isatty(fd) | 如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。 |
| os.lchflags(path, flags) | 设置路径的标记为数字标记，类似 chflags()，但是没有软链接 |
| os.lchmod(path, mode) | 修改连接文件权限 |
| os.lchown(path, uid, gid) | 更改文件所有者，类似 chown，但是不追踪链接。 |
| os.link(src, dst) | 创建硬链接，名为参数 dst，指向参数 src |
| os.listdir(path) | 返回path指定的文件夹包含的文件或文件夹的名字的列表。 |
| os.lseek(fd, pos, how) | 设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效 |
| os.lstat(path) | 像stat(),但是没有软链接 |
| os.major(device) | 从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。 |
| os.makedev(major, minor) | 以major和minor设备号组成一个原始设备号 |
| os.makedirs(path[, mode]) | 递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。 |
| os.minor(device) | 从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。 |
| os.mkdir(path[, mode]) | 以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。 |
| os.mkfifo(path[, mode]) | 创建命名管道，mode 为数字，默认为 0666 (八进制) |
| os.mknod(filename[, mode=0600, device]) | 创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。 |
| os.open(file, flags[, mode]) | 打开一个文件，并且设置需要的打开选项，mode参数是可选的 |
| os.openpty() | 打开一个新的伪终端对。返回 pty 和 tty的文件描述符。 |
| os.pathconf(path, name) | 返回相关文件的系统配置信息。 |
| os.pipe() | 创建一个管道. 返回一对文件描述符(r, w) 分别为读和写 |
| os.popen(command[, mode[, bufsize]]) | 从一个 command 打开一个管道 |
| os.read(fd, n) | 从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。 |
| os.readlink(path) | 返回软链接所指向的文件 |
| os.remove(path) | 删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。 |
| os.removedirs(path) | 递归删除目录。 |
| os.rename(src, dst) | 重命名文件或目录，从 src 到 dst |
| os.renames(old, new) | 递归地对目录进行更名，也可以对文件进行更名。 |
| os.rmdir(path) | 删除path指定的空目录，如果目录非空，则抛出一个OSError异常。 |
| os.stat(path) | 获取path指定的路径的信息，功能等同于C API中的stat()系统调用。 |
| os.stat_float_times([newvalue]) | 决定stat_result是否以float对象显示时间戳 |
| os.statvfs(path) | 获取指定路径的文件系统统计信息 |
| os.symlink(src, dst) | 创建一个软链接 |
| os.tcgetpgrp(fd) | 返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组 |
| os.tcsetpgrp(fd, pg) | 设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。 |
| os.tempnam([dir[, prefix]]) | 返回唯一的路径名用于创建临时文件。 |
| os.tmpfile() | 返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。 |
| os.tmpnam() | 为创建一个临时文件返回一个唯一的路径 |
| os.ttyname(fd) | 返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。 |
| os.unlink(path) | 删除文件路径 |
| os.utime(path, times) | 返回指定的path文件的访问和修改的时间。 |
| os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]]) | 输出在文件夹中的文件名通过在树中游走，向上或者向下。 |
| os.write(fd, str) | 写入字符串到文件描述符 fd中. 返回实际写入的字符串长度 |

# 二、`os.path` 模块
以下方法均为os.path模块内部方法，调用时需加`os.path.`，如：`os.path.abspath(path)`

| 方法 | 描述 |
| --- | --- |
| abspath(path) | 返回path规范化的绝对路径（但这个路径不一定是真实的路径），如果path仅是一个文件名，使用该函数后返回的路径是当前工作目录路径连接改文件名后所组成的新的路径名。 |
| basename(path) | 返回一个目录的基名(文件名)，如果path以`/`或`\`结尾，就会返回空值。即`os.path.split(path)`的第二个元素。 |
| commonpath(paths) | 接受包含多个路径的序列 paths，返回 paths 的最长公共子路径。如果 paths 同时包含绝对路径和相对路径，或 paths 在不同的驱动器上，或 paths 为空，则抛出 ValueError 异常。与 commonprefix() 不同，本方法返回有效路径。 |
| commonprefix(list) | 返回list中所有path共有的最长的路径，从左向右，逐字符比较。如果 列表 为空，则返回空字符串 ('')。 |
| dirname(path) | 返回一个目录的目录名，其实就是`os.path.split(path)`的第一个元素 |
| exists(path) | 测试指定文件是否存在 |
| lexists(path) | 如果 path 指向一个已存在的路径，返回 True。对于失效的符号链接，也返回 True。在缺失 `os.lstat()` 的平台上等同于 `exists()`。 |
| expanduser(path) | 在 Unix 和 Windows 上，将参数中开头部分的 `~` 或 `~user` 替换为当前 用户 的家目录并返回。 |
| expandvars(path) | 输入带有环境变量的路径作为参数，返回展开变量以后的路径。`$name` 或 `${name}`形式的子字符串被环境变量 name 的值替换。格式错误的变量名称和对不存在变量的引用保持不变。在 Windows 上，除了 `$name` 和 `${name}` 外，还可以展开 `%name%`。 |
| getatime(path) | 得到指定文件最后一次的访问时间 |
| getctime(path) | 返回浮点数的文件或目录的创建时间，在类Unix系统上是文件最近更改的时间，在Windows上是文件或目录的创建时间。 |
| getmtime(path) | 得到指定文件最后一次的修改时间 |
| getsize(path) | 得到得到文件的大小（字节），如果filename为目录返回0L |
| isabs(path) | 测试参数是否是绝对路径 |
| isdir(path) | 测试指定参数是否是目录名 |
| isfile(path) | 测试指定参数是否是一个文件 |
| islink(path) | 测试指定参数是否是一个软链接 |
| ismount(path) | 测试指定参数是否是挂载点 |
| `join(path, *paths)` | 合理地拼接一个或多个路径部分。返回值是 path 和 *paths 所有值的连接，每个非空部分后面都紧跟一个目录分隔符 (os.sep)，除了最后一部分。这意味着如果最后一部分为空，则结果将以分隔符结尾。如果参数中某个部分是绝对路径，则绝对路径前的路径都将被丢弃，并从绝对路径部分开始连接。 |
| normcase(path) | 在Linux下，该函数会原样返回path，在Windows平台上会将路径中所有的字符转换为小写，并将所有斜杠转换为反斜杠，同时将路径规范化。 |
| normpath(path) | 规范path字符串形式（规范文件路径） |
| realpath(path) | 返回指定文件的标准路径，而非软链接所在的路径 |
| relpath(path, start=os.curdir) | 返回从当前目录或 start 目录（可选）到达 path 之间要经过的相对路径。这仅仅是对路径的计算，不会访问文件系统来确认 path 或 start 的存在性或属性。start 默认为 `os.curdir`。 |
| samefile(path1, path2) | 测试两个路径是否指向同一个文件 |
| sameopenfile(fp1, fp2) | 如果文件描述符 fp1 和 fp2 指向相同文件，则返回 True。 |
| samestat(stat1, stat2) | 如果 stat 元组 stat1 和 stat2 指向相同文件，则返回 True。这些 stat 元组可能是由 os.fstat()、os.lstat() 或 os.stat() 返回的。本函数实现了 samefile() 和 sameopenfile() 底层所使用的比较过程。 |
| split(path) | 分割目录名，返回由其文件名和目录给成的元组 |
| splitdrive(path) | 拆分驱动器和路劲，主要对win，对Linux元组第一个总是空的。 |
| splitext(path) | 分割文件名，返回由文件名和扩展名组成的元组；默认返回（fname, fextension）元组，可做分片操作，以” . “为分隔符。 |
| supports_unicode_filenames | 如果（在文件系统限制下）允许将任意 Unicode 字符串用作文件名，则为 True。 |
| walk(top, func, arg) | 列出目录树下的目录路径和文件路劲\n参数说明：\n `top`：表示需要遍历的目录树的路径\n `func`：表示回调函数，对遍历路径进行处理。所谓回调函数，是作为某个函数的的参数使用，当某个时间触发时，程序将调用定义好的回调函数处理某个任务。回调函数必须提供3个参数：第1个参数为walk()的参数tag，第2个参数表示目录列表，第3个参数表示文件列表。\n `arg`：是传递给回调参数func的元组.回调函数的一个参数必须是arg，为回调函数提供处理参数.参数arg可以为空。 |


# 三、OS 模块 重点方法使用
## 1. 环境变量
在操作系统中定义的环境变量，全部存储在`os.environ`变量中。
查看
```python
>>> os.environ
environ({'VERSIONER_PYTHON_PREFER_32_BIT': 'no', 'TERM_PROGRAM_VERSION': '326', 'LOGNAME': 'michael', 'USER': 'michael', 'PATH': '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin', ...})
```
获取某个环境变量的值，调用os.environ.get('key')
```python
>>> os.environ.get('PATH')
'/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin'
>>> os.environ.get('x', 'default')
'default'
```
## 2. 操作文件、目录
操作文件和目录的函数一部分放在 os模块，一部分放在 `os.path` 模块中。
例：
查看、创建、删除目录
```python
# 查看当前目录的绝对路径:
os.path.abspath('.')
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')
```
注意：把两个路径合成一个时，不要直接拼接字符串，而要通过`os.path.join()`函数，这样可以 正确处理不同操作系统的路径分隔符。
同理，拆分路径时使用`os.path.split()` 函数。


# 参考
【(官档)os.path --- 常用路径操作】https://docs.python.org/zh-cn/3/library/os.path.html
【Python os.path 模块介绍】 https://blog.csdn.net/SeeTheWorld518/article/details/47982985
【python os.path模块用法详解】 https://www.cnblogs.com/onemorepoint/p/9132976.html











