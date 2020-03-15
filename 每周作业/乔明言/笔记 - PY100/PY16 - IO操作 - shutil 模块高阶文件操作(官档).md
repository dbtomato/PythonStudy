---
title: 16 - IO操作 - `shutil 模块` 高阶文件操作(官档)
tags: shutil,copy,拷贝,复制,归档,压缩,zip,tar,IO,官档,3.8
renderNumberedHeading: true
grammar_cjkRuby: true
---

Author:  Qiao My
Create_Time: 2020-3-11

[toc]

>shutil 模块提供了一系列对文件和文件集合的高阶操作。 特别是提供了一些支持**文件拷贝**和删除的函数。 对于单个文件的操作，请参阅 os 模块。
[【(官档) shutil --- 高阶文件操作】](https://docs.python.org/zh-cn/3/library/shutil.html)

# 一、shutil 模块方法
| 方法 | 描述 |
| --- | --- |
| copyfileobj(fsrc, fdst[, length]) | 将文件类对象 fsrc 的内容拷贝到文件类对象 fdst。 整数值 length 如果给出则为缓冲区大小。 特别地， length 为负值表示拷贝数据时不对源数据进行分块循环处理；默认情况下会分块读取数据以避免不受控制的内存消耗。 请注意如果 fsrc 对象的当前文件位置不为 0，则只有从当前文件位置到文件末尾的内容会被拷贝。 |
| `copyfile(src, dst, *, follow_symlinks=True)` | 将名为 src 的文件的内容（不包括元数据）拷贝到名为 dst 的文件并以尽可能高效的方式返回 dst。 src 和 dst 均为路径类对象或以字符串形式给出的路径名。dst 必须是完整的目标文件名；对于接受目标目录路径的拷贝请参见 copy()。 如果 src 和 dst 指定了同一个文件，则将引发 SameFileError。目标位置必须是可写的；否则将引发 OSError 异常。 如果 dst 已经存在，它将被替换。 特殊文件如字符或块设备以及管道无法用此函数来拷贝。如果 follow_symlinks 为假值且 src 为符号链接，则将创建一个新的符号链接而不是拷贝 src 所指向的文件。 |
| exception shutil.SameFileError | 此异常会在 copyfile() 中的源和目标为同一文件时被引发。 |
| `copymode(src, dst, *, follow_symlinks=True)` | 从 src 拷贝权限位到 dst。 文件的内容、所有者和分组将不受影响。 src 和 dst 均为路径类对象或字符串形式的路径名。 如果 follow_symlinks 为假值，并且 src 和 dst 均为符号链接，copymode() 将尝试修改 dst 本身的模式（而非它所指向的文件）。 此功能并不是在所有平台上均可用；请参阅 copystat() 了解详情。 如果 copymode() 无法修改本机平台上的符号链接，而它被要求这样做，它将不做任何操作即返回。 |
| `copystat(src, dst, *, follow_symlinks=True)` | 从 src 拷贝权限位、最近访问时间、最近修改时间以及旗标到 dst。 在 Linux上，copystat() 还会在可能的情况下拷贝“扩展属性”。 文件的内容、所有者和分组将不受影响。 src 和 dst 均为路径类对象或字符串形式的路径名。如果 follow_symlinks 为假值，并且 src 和 dst 均指向符号链接，copystat() 将作用于符号链接本身而非该符号链接所指向的文件 — 从 src 符号链接读取信息，并将信息写入 dst 符号链接。 |
| `copy(src, dst, *, follow_symlinks=True)` | 将文件 src 拷贝到文件或目录 dst。 src 和 dst 应为字符串。 如果 dst 指定了一个目录，文件将使用 src 中的基准文件名拷贝到 dst。 返回新创建文件的路径。如果 follow_symlinks 为假值且 src 为符号链接，则 dst 也将被创建为符号链接。 如果 follow_symlinks 为真值且 src 为符号链接，dst 将成为 src 所指向的文件的一个副本。copy() 会拷贝文件数据和文件的权限模式 (参见 os.chmod())。 其他元数据，例如文件的创建和修改时间不会被保留。 要保留所有原有的元数据，请改用 copy2() 。 |
| `copy2(src, dst, *, follow_symlinks=True)` | 类似于 copy()，区别在于 copy2() 还会尝试保留文件的元数据。当 follow_symlinks 为假值且 src 为符号链接时，copy2() 会尝试将来自 src 符号链接的所有元数据拷贝到新创建的 dst 符号链接。 但是，此功能不是在所有平台上均可用。 在此功能部分或全部不可用的平台上，copy2() 将尽量保留所有元数据；copy2() 一定不会由于无法保留文件元数据而引发异常。copy2() 会使用 copystat() 来拷贝文件元数据。 |
| `ignore_patterns(*patterns)` | 这个工厂函数会创建一个函数，它可被用作 copytree() 的 ignore 可调用对象参数，以忽略那些匹配所提供的 glob 风格的 patterns 之一的文件和目录。 |
| copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False) | 将以 src 为根起点的整个目录树拷贝到名为 dst 的目录并返回目标目录。 dirs_exist_ok 指明是否要在 dst 或任何丢失的父目录已存在的情况下引发异常。目录的权限和时间会通过 copystat() 来拷贝，单个文件则会使用 copy2() 来拷贝。 |
| rmtree(path, ignore_errors=False, onerror=None) | 删除一个完整的目录树；path 必须指向一个目录（但不能是一个目录的符号链接）。 如果 ignore_errors 为真值，删除失败导致的错误将被忽略；如果为假值或是省略，此类错误将通过调用由 onerror 所指定的处理程序来处理，或者如果此参数被省略则将引发一个异常。 |
| rmtree.avoids_symlink_attacks | 指明当前平台和实现是否提供防御符号链接攻击的 rmtree() 版本。 目前它仅在平台支持基于 fd 的目录访问函数时才返回真值。 |
| move(src, dst, copy_function=copy2) | 递归地将一个文件或目录 (src) 移至另一位置 (dst) 并返回目标位置。 |
| disk_usage(path) | 返回给定路径的磁盘使用统计数据，形式为一个 named tuple，其中包含 total, used 和 free 属性，分别表示总计、已使用和未使用空间的字节数。 path 可以是一个文件或是一个目录。 |
| chown(path, user=None, group=None) | 修改给定 path 的所有者 user 和/或 group。user 可以是一个系统用户名或 uid；group 同样如此。 要求至少有一个参数。 |
| which(cmd, mode=os.F_OK | os.X_OK, path=None) | 返回当给定的 cmd 被调用时将要运行的可执行文件的路径。 如果没有 cmd 会被调用则返回 None。mode 是一个传递给 os.access() 的权限掩码，在默认情况下将确定文件是否存在并且为可执行文件。当未指定 path 时，将会使用 os.environ() 的结果，返回 "PATH" 的值或回退为 os.defpath。 |
| exception shutil.Error | 此异常会收集在多文件操作期间所引发的异常。 对于 copytree()，此异常参数将是一个由三元组 (srcname, dstname, exception) 构成的列表。 |


# 二、shutil 归档(压缩) 方法
shutil 模块提供了用于创建和读取压缩和归档文件的高层级工具。 它们依赖于 zipfile 和 tarfile 模块。

| 方法 | 描述 |
| --- | --- |
| make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]]) | 创建一个归档文件（例如 zip 或 tar）并返回其名称。 |
| get_archive_formats() | 返回支持的归档格式列表。 所返回序列中的每个元素为一个元组 (name, description)。 |
| register_archive_format(name, function[, extra_args[, description]]) | 为 name 格式注册一个归档器。 |
| unregister_archive_format(name) | 从支持的格式中移除归档格式 name。 |
| unpack_archive(filename[, extract_dir[, format]]) | 解包一个归档文件。 filename 是归档文件的完整路径。 |
| register_unpack_format(name, extensions, function[, extra_args[, description]]) | 注册一个解包格式。 name 为格式名称而 extensions 为对应于该格式的扩展名列表，例如 Zip 文件的扩展名为 .zip。 |
| unregister_unpack_format(name) | 撤销注册一个解包格式。 name 为格式的名称。 |
| get_unpack_formats() | 返回所有已注册的解包格式列表。 所返回序列中的每个元素为一个元组 (name, extensions, description)。 |

## 1. 归档格式
默认情况下 shutil 提供以下格式(format):
- **zip**: ZIP 文件（如果 zlib 模块可用）。
- **tar**: 未压缩的 tar 文件。 对于新归档文件将使用 POSIX.1-2001 pax 格式。
- **gztar**: gzip 压缩的 tar 文件（如果 zlib 模块可用）。
- **bztar**: bzip2 压缩的 tar 文件（如果 bz2 模块可用）。
- **xztar**: xz 压缩的 tar 文件（如果 lzma 模块可用）。

## 2. 重要方法详解
### shutil.make_archive()
`shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])`
参数说明：
- **base_name** 是要创建的文件名称，包括路径，去除任何特定格式的扩展名。 format 是归档格式：为 "zip" (如果 zlib 模块可用), "tar", "gztar" (如果 zlib 模块可用), "bztar" (如果 bz2 模块可用) 或 "xztar" (如果 lzma 模块可用) 中的一个。
- **root_dir** 是一个目录，它将作为归档文件的根目录；例如，我们通常会在创建归档文件之前用 chdir 命令切换到 root_dir。
- **base_dir** 是我们要执行归档的起始目录；也就是说 base_dir 将成为归档文件中所有文件和目录共有的路径前缀。
- **dry_run** 如果 为真值，则不会创建归档文件，但将要被执行的操作会被记录到 logger。
- **owner** 和 **group** 将在创建 tar 归档文件时被使用。 默认会使用当前的所有者和分组。
- **logger** 必须是一个兼容 PEP 282 的对象，通常为 logging.Logger 的实例。
- verbose 参数已不再使用并进入弃用状态。

root_dir 和 base_dir 默认均为当前目录。

引发一个 审计事件 shutil.make_archive 并附带参数 base_name, format, root_dir, base_dir。

在 3.8 版更改: 现在对于通过 format="tar" 创建的归档文件将使用新式的 pax (POSIX.1-2001) 格式而非旧式的 GNU 格式。

### register_archive_format()
`register_archive_format(name, function[, extra_args[, description]])`
function 是将被用来解包归档文件的可调用对象。 该可调用对象将接收要创建文件的 base_name，再加上要归档内容的 base_dir (其默认值为 os.curdir)。 更多参数会被作为关键字参数传入: owner, group, dry_run 和 logger (与向 make_archive() 传入的参数一致)。

如果给出了 extra_args，则其应为一个 (name, value) 对的序列，将在归档器可调用对象被使用时作为附加的关键字参数。

description 由 get_archive_formats() 使用，它将返回归档器的列表。 默认值为一个空字符串。

### unpack_archive()
`unpack_archive(filename[, extract_dir[, format]])`
解包一个归档文件。 
- **filename** 是归档文件的完整路径。
- **extract_dir** 是归档文件解包的目标目录名称。 如果未提供，则将使用当前工作目录。
- **format** 是归档格式：应为 "zip", "tar", "gztar", "bztar" 或 "xztar" 之一。 
  - 或者任何通过 register_unpack_format() 注册的其他格式。 如果未提供，unpack_archive() 将使用归档文件的扩展名来检查是否注册了对应于该扩展名的解包器。 在未找到任何解包器的情况下，将引发 ValueError。

引发一个 审计事件 shutil.unpack_archive 附带参数 filename, extract_dir, format。

在 3.7 版更改: 接受一个 path-like object 作为 filename 和 extract_dir。



