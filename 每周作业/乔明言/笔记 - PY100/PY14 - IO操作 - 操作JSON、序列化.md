---
title: 14 - IO操作 - 操作JSON、序列化
tags: json,序列化,pickle,dump,dumps,load,loads,lambda,class,类序列化
renderNumberedHeading: true
grammar_cjkRuby: true
---

Author:  Qiao My
Create_Time: 2020-3-11

[toc]


如果要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，如XML，但更好的方法时序列化为 JSON字符串。
JSON 仅仅是一个字符串，可以被所有语言读取，也可以方便的存储到磁盘或通过网络传输。
JSON 比 XML 更快，而且可以直接在 web页面中读取，非常方便。

# 一、JSON 文件操作
>JSON (JavaScript Object Notation)，由 RFC 7159 (which obsoletes RFC 4627) 和 ECMA-404 指定，是一个受 JavaScript 的对象字面量语法启发的轻量级数据交换格式，尽管它不仅仅是一个严格意义上的 JavaScript 的字集。

JSON标准规定JSON编码是`UTF-8`。

## 1. JSON 模块方法
| 方法 | 描述 |
| --- | --- |
| `dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)` | 使用这个 转换表 将 obj 序列化为 JSON 格式化流形式的 fp (支持 .write() 的 file-like object)。 |
| `dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)` | 使用这个 转换表 将 obj 序列化为 JSON 格式的 str。 其参数的含义与 dump() 中的相同。 |
| `load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)` | 使用这个 转换表 将 fp (一个支持 .read() 并包含一个 JSON 文档的 text file 或者 binary file) 反序列化为一个 Python 对象。 |
| `loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)` | 使用这个 转换表 将 s (一个包含 JSON 文档的 str, bytes 或 bytearray 实例) 反序列化为 Python 对象。 |
| `class json.JSONDecoder(*, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None)` | 简单的JSON解码器。 |
| `class json.JSONEncoder(*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)` | 用于Python数据结构的可扩展JSON编码器。
| exception json.JSONDecodeError(msg, doc, pos) | 异常 |

## 2. 编码和解码
### Json模块默认 解码规则
| JSON                | Python       |
| ------------------- | ------------ |
| object              | dict         |
| array               | list         |
| string              | str          |
| number (int / real) | int / float  |
| true / false        | True / False |
| null                | None         |

### Json模块默认 编码规则
| Python                                 | JSON         |
| -------------------------------------- | ------------ |
| dict                                   | object       |
| list, tuple                            | array        |
| str                                    | string       |
| int, float, int & float-derived Enums(float 派生的枚举) | number       |
| True / False                           | true / false |
| None                                   | null         |



## 3. JSON 基本方法详解
### dump()
`json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`
使用这个 转换表 将 `obj` 序列化为 JSON 格式化流形式的 fp (支持 .write() 的 file-like object)。
json 模块始终产生 str 对象而非 bytes 对象。因此，fp.write() 必须支持 str 输入。

**skipkeys** 如果是 true （默认为 False），那么那些不是基本对象（包括 str, int、float、bool、None）的字典的键会被跳过；否则引发一个 TypeError。
**ensure_ascii 如果是 true （即默认值），输出保证将所有输入的非 ASCII 字符转义。如果 ensure_ascii 是 false，这些字符会原样输出。
**check_circular** 如果是false (默认为 True)，那么容器类型的循环引用检验会被跳过并且循环引用会引发一个 OverflowError (或者更糟的情况)。
**allow_nan** 如果是 false（默认为 True），那么在对严格 JSON 规格范围外的 float 类型值（nan、inf 和 -inf）进行序列化时会引发一个 ValueError。如果 allow_nan 是 true，则使用它们的 JavaScript 等价形式（NaN、Infinity 和 -Infinity）。
**indent** 如果是一个非负整数或者字符串，那么 JSON 数组元素和对象成员会被美化输出为该值指定的缩进等级。如果缩进等级为零、负数或者 ""，则只会添加换行符。None``（默认值）选择最紧凑的表达。使用一个正整数会让每一层缩进同样数量的空格。如果 *indent* 是一个字符串（比如 ``"\t"），那个字符串会被用于缩进每一层。在 3.2 版 允许使用字符串作为 indent 而不再仅仅是整数。
**separators** 指定一个 (item_separator, key_separator) 元组。当 indent 为 None 时，默认值取 (', ', ': ')，否则取 (',', ': ')。为了得到最紧凑的 JSON 表达式，你应该指定其为 (',', ':') 以消除空白字符。在 3.4 版更改: 现当 indent 不是 None 时，采用 (',', ': ') 作为默认值。
**default** 指定一个函数，每当某个对象无法被序列化时它会被调用。它应该返回该对象的一个可以被 JSON 编码的版本或者引发一个 TypeError。如果没有被指定，则会直接引发 TypeError。
**sort_keys** 如果是 true（默认为 False），那么字典的输出会以键的顺序排序。
**cls** 为了使用一个自定义的 JSONEncoder 子类（比如：覆盖了 default() 方法来序列化额外的类型）， 通过 **cls** 关键字参数来指定；否则将使用 JSONEncoder。

在 3.6 版更改: 所有的可选参数现在是 keyword-only 的了。

注意：与 pickle 和 marshal 不同，JSON 不是一个具有框架的协议，所以尝试多次使用同一个 fp 调用 dump() 来序列化多个对象会产生一个不合规的 JSON 文件。

### dumps()
`json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`
使用这个 转换表 将 obj 序列化为 JSON 格式的 str。 其参数的含义与 dump() 中的相同。

注意：JSON 中的键-值对中的键永远是 str 类型的。当一个对象被转化为 JSON 时，字典中所有的键都会被强制转换为字符串。这所造成的结果是字典被转换为 JSON 然后转换回字典时可能和原来的不相等。换句话说，如果 x 具有非字符串的键，则有 `loads(dumps(x)) != x`。

### load()
`json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`
使用这个 转换表 将 `fp` (一个支持 .read() 并包含一个 JSON 文档的 text file 或者 binary file) 反序列化为一个 Python 对象。

**object_hook** 是一个可选的函数，它会被调用于每一个解码出的对象字面量（即一个 dict）。object_hook 的返回值会取代原本的 dict。这一特性能够被用于实现自定义解码器（如 JSON-RPC 的类型提示)。
**object_pairs_hook** 是一个可选的函数，它会被调用于每一个有序列表对解码出的对象字面量。 object_pairs_hook 的返回值将会取代原本的 dict 。这一特性能够被用于实现自定义解码器。如果 object_hook 也被定义， object_pairs_hook 优先。在 3.1 版添加。
**parse_float** ，如果指定，将与每个要解码 JSON 浮点数的字符串一同调用。默认状态下，相当于 float(num_str) 。可以用于对 JSON 浮点数使用其它数据类型和语法分析程序 （比如 decimal.Decimal ）。
**parse_int** ，如果指定，将与每个要解码 JSON 整数的字符串一同调用。默认状态下，相当于 int(num_str) 。可以用于对 JSON 整数使用其它数据类型和语法分析程序 （比如 float ）。
**parse_constant** ，如果指定，将要与以下字符串中的一个一同调用： '-Infinity' ， 'Infinity' ， 'NaN' 。如果遇到无效的 JSON 数字则可以使用它引发异常。在 3.1 版 parse_constant 不再调用 'null' ， 'true' ， 'false' 。
**cls** 要使用自定义的 JSONDecoder 子类，用 **cls** 指定他；否则使用 JSONDecoder 。额外的关键词参数会通过类的构造函数传递。

如果反序列化的数据不是有效 JSON 文档，引发 JSONDecodeError 错误。

在 3.6 版更改: 
- 所有的可选参数现在是 keyword-only 的了。
- fp 现在可以是 binary file 。输入编码应当是 UTF-8 ， UTF-16 或者 UTF-32 。

### loads()
`json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`
使用这个 转换表 将 s (一个包含 JSON 文档的 str, bytes 或 bytearray 实例) 反序列化为 Python 对象。
除了*encoding*被忽略和弃用自 Python 3.1 以来，其他参数的含义与 load() 中相同。
如果反序列化的数据不是有效 JSON 文档，引发 JSONDecodeError 错误。
在 3.6 版更改: s 现在可以为 bytes 或 bytearray 类型。 输入编码应为 UTF-8, UTF-16 或 UTF-32。

## 4. JSON 进阶 - Class类的序列化与反序列化
Python中的`dict`对象可以直接序列化为JSON的`{}`，但是实际开发中，更多的使用`class`表示对象，定义一个对象然后序列化。
Python 不支持直接将 class 对象序列化 JSON，正确的序列化方式为，为class 专门写一个转换函数，通过`dumps()`方法的defaults参数指定该函数。
例：
```python
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    # 将class 转换为dict
    def student2dict(std):
        return {
            'name': std.name,
            'age': std.age,
            'score': std.score
        }

# 调用
s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
```

### 简化写法
通常`class`的实例都有`__dict__`属性，它就是一个`dict`，用来存储实例变量。但定义了`__slots__`的class例外。
例：
```python
print(json.dumps(s, default=lambda obj: obj.__dict__))
```
JSON反序列化为`class`对象实例。
`loads()`方法转换出一个`dict`对象，传入的`object_hook`函数负责把`dict`转换为实例。
例：
```python
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
```
运行结果：
```python
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> print(json.loads(json_str, object_hook=dict2student))
<__main__.Student object at 0x10cd3c190>
```

# 二、序列化、反序列化
>序列化（serialization）在计算机科学的数据处理中，是指将数据结构或对象状态转换为可以存储或传输的形式，这样在需要的时候能够恢复到原先的状态，而且通过序列化的数据重新获取字节时，可以利用这些字节来产生原始对象的副本（拷贝）。与这个过程相反的动作，即从一系列字节中提取数据结构的操作，就是反序列化（deserialization） - 维基百科

通俗的讲，序列化就是 把变量从内存中变成可存储或可传输的过程。
序列化之后，序列化后的内容就可以写入磁盘，或者通过网络传输到别的机器上。
反过来，把变量内容从序列化的对象重新读到内存里，称为 反序列化。

## 1. pickle 模块
Python 提供了 `pickle` 模块来实现序列化。

**dumps()、dump() 方法**
`pickle.dumps()`方法把任意对象序列化成一个`bytes`，这个`bytes`就可以写入文件。
`pickle.dump()`方法直接把对象序列化后写入一个 file-like Object。
例：
```python
import pickle
>>> d = dict(name='Bob', age=20, score=88)
# dumps
>>> pickle.dumps(d)
b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
# dump
>>> f = open('dump.txt', 'wb')
>>> pickle.dump(d, f)
>>> f.close()
# load
>>> f = open('dump.txt', 'rb')
>>> d = pickle.load(f)
>>> f.close()
>>> d
{'age': 20, 'score': 88, 'name': 'Bob'}
```

**loads()、load() 方法**
loads() 对于封存生成的对象 bytes_object，还原出原对象的结构并返回。
load() 从 file-like Object 中直接反序列化出对象。

注意：pickle的问题和其他编程语言特有的序列化问题一样，只能用于Python，并且可能不同版本Python彼此不兼容，因此只能用来保存不重要的数据，不能成功地反序列化也没关系。


# 参考
【(官档)pickle --- Python 对象序列化】https://docs.python.org/zh-cn/3/library/pickle.html











