---
title: multiprocessing 模块函数列表
tags: multiprocessing,Process,Queue,Pipes,Connection,Lock,RLock,BaseManager,pool
renderNumberedHeading: true
grammar_cjkRuby: true
---

Author:  Qiao My
Create_Time: 2020-3-21

[toc]

> 官档：[multiprocessing --- 基于进程的并行](https://docs.python.org/zh-cn/3/library/multiprocessing.html#shared-ctypes-objects)
# Process 和异常
`class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)`
| 方法 | 描述 |
| --- | --- |
| run() | 表示进程活动的方法。你可以在子类中重载此方法。标准 run() 方法调用传递给对象构造函数的可调用对象作为目标参数（如果有），分别从 args 和 kwargs 参数中获取顺序和关键字参数。 |
| start() | 启动进程活动。这个方法每个进程对象最多只能调用一次。它会将对象的 run() 方法安排在一个单独的进程中调用。 |
| join([timeout]) | 如果可选参数 timeout 是 None （默认值），则该方法将阻塞，直到调用 join() 方法的进程终止。如果 timeout 是一个正数，它最多会阻塞 timeout 秒。请注意，如果进程终止或方法超时，则该方法返回 None 。检查进程的 exitcode 以确定它是否终止。一个进程可以被 join 多次。进程无法join自身，因为这会导致死锁。尝试在启动进程之前join进程是错误的。 |
| name | 进程的名称。该名称是一个字符串，仅用于识别目的。它没有语义。可以为多个进程指定相同的名称。初始名称由构造器设定。 如果没有为构造器提供显式名称，则会构造一个形式为 'Process-N1:N2:...:Nk' 的名称，其中每个 Nk 是其父亲的第 N 个孩子。 |
| is_alive() | 返回进程是否还活着。粗略地说，从 start() 方法返回到子进程终止之前，进程对象仍处于活动状态。 |
| daemon | 进程的守护标志，一个布尔值。这必须在 start() 被调用之前设置。初始值继承自创建进程。当进程退出时，它会尝试终止其所有守护进程子进程。请注意，不允许守护进程创建子进程。否则，守护进程会在子进程退出时终止其子进程。 另外，这些 不是 Unix守护进程或服务，它们是正常进程，如果非守护进程已经退出，它们将被终止（并且不被合并）。 |
| pid | 返回进程ID。在生成该进程之前，这将是 None 。 |
| exitcode | 子进程的退出代码。如果进程尚未终止，这将是 None 。负值 -N 表示子进程被信号 N 终止。 |
| authkey | 进程的身份验证密钥（字节字符串）。当 multiprocessing 初始化时，主进程使用 os.urandom() 分配一个随机字符串。当创建 Process 对象时，它将继承其父进程的身份验证密钥，尽管可以通过将 authkey 设置为另一个字节字符串来更改。 |
| sentinel | 系统对象的数字句柄，当进程结束时将变为 "ready" 。如果要使用 multiprocessing.connection.wait() 一次等待多个事件，可以使用此值。否则调用 join() 更简单。 |
| terminate() | 终止进程。 在Unix上，这是使用 SIGTERM 信号完成的；在Windows上使用 TerminateProcess() 。 请注意，不会执行退出处理程序和finally子句等。请注意，进程的后代进程将不会被终止 —— 它们将简单地变成孤立的。警告 如果在关联进程使用管道或队列时使用此方法，则管道或队列可能会损坏，并可能无法被其他进程使用。类似地，如果进程已获得锁或信号量等，则终止它可能导致其他进程死锁。 |
| kill() | 与 terminate() 相同，但在Unix上使用 SIGKILL 信号。 |
| close() | 关闭 Process 对象，释放与之关联的所有资源。如果底层进程仍在运行，则会引发 ValueError 。一旦 close() 成功返回， Process 对象的大多数其他方法和属性将引发 ValueError 。 |
| exception multiprocessing.ProcessError | 所有 multiprocessing 异常的基类。 |
| exception multiprocessing.BufferTooShort | 当提供的缓冲区对象太小而无法读取消息时， Connection.recv_bytes_into() 引发的异常。如果 e 是一个 BufferTooShort 实例，那么 e.args[0] 将把消息作为字节字符串给出。 |
| exception multiprocessing.AuthenticationError | 出现身份验证错误时引发。 |
| exception multiprocessing.TimeoutError | 有超时的方法超时时引发。 |


注意 start() 、 join() 、 is_alive() 、 terminate() 和 exitcode 方法只能由创建进程对象的进程调用。



# 管道和队列
**multiprocessing.Pipe([duplex])**
返回一对 Connection`对象  ``(conn1, conn2)` ， 分别表示管道的两端。
如果 duplex 被置为 True (默认值)，那么该管道是双向的。如果 duplex 被置为 False ，那么该管道是单向的，即 conn1 只能用于接收消息，而 conn2 仅能用于发送消息。

## Queue
**class multiprocessing.Queue([maxsize])**
返回一个使用一个管道和少量锁和信号量实现的共享队列实例。当一个进程将一个对象放进队列中时，一个写入线程会启动并将对象从缓冲区写入管道中。

| 方法 | 描述 |
| --- | --- |
| qsize() | 返回队列的大致长度。由于多线程或者多进程的上下文，这个数字是不可靠的。注意，在 Unix 平台上，例如 Mac OS X ，这个方法可能会抛出 NotImplementedError  异常，因为该平台没有实现 sem_getvalue() 。 |
| empty() | 如果队列是空的，返回 True ，反之返回 False 。 由于多线程或多进程的环境，该状态是不可靠的。 |
| full() | 如果队列是满的，返回 True ，反之返回 False 。 由于多线程或多进程的环境，该状态是不可靠的。 |
| put(obj[, block[, timeout]]) | 将 obj 放入队列。如果可选参数 block 是 True (默认值) 而且 timeout 是 None (默认值), 将会阻塞当前进程，直到有空的缓冲槽。如果 timeout 是正数，将会在阻塞了最多 timeout 秒之后还是没有可用的缓冲槽时抛出 queue.Full  异常。反之 (block 是 False 时)，仅当有可用缓冲槽时才放入对象，否则抛出 queue.Full 异常 (在这种情形下 timeout 参数会被忽略)。 |
| put_nowait(obj) | 相当于 put(obj, False)。 |
| get([block[, timeout]]) | 从队列中取出并返回对象。如果可选参数 block 是 True (默认值) 而且 timeout 是 None (默认值), 将会阻塞当前进程，直到队列中出现可用的对象。如果 timeout 是正数，将会在阻塞了最多 timeout 秒之后还是没有可用的对象时抛出 queue.Empty 异常。反之 (block 是 False 时)，仅当有可用对象能够取出时返回，否则抛出 queue.Empty 异常 (在这种情形下 timeout 参数会被忽略)。 |
| get_nowait() | 相当于 get(False)。multiprocessing.Queue 类有一些在 queue.Queue 类中没有出现的方法。这些方法在大多数情形下并不是必须的。 |
| close() | 指示当前进程将不会再往队列中放入对象。一旦所有缓冲区中的数据被写入管道之后，后台的线程会退出。这个方法在队列被gc回收时会自动调用。 |
| join_thread() | 等待后台线程。这个方法仅在调用了 close() 方法之后可用。这会阻塞当前进程，直到后台线程退出，确保所有缓冲区中的数据都被写入管道中。默认情况下，如果一个不是队列创建者的进程试图退出，它会尝试等待这个队列的后台线程。这个进程可以使用 cancel_join_thread() 让 join_thread() 方法什么都不做直接跳过。 |
| cancel_join_thread() | 防止 join_thread() 方法阻塞当前进程。具体而言，这防止进程退出时自动等待后台线程退出。详见 join_thread()。可能这个方法称为”allow_exit_without_flush()“ 会更好。这有可能会导致正在排队进入队列的数据丢失，大多数情况下你不需要用到这个方法，仅当你不关心底层管道中可能丢失的数据，只是希望进程能够马上退出时使用。注解 该类的功能依赖于宿主操作系统具有可用的共享信号量实现。否则该类将被禁用，任何试图实例化一个 Queue 对象的操作都会抛出 ImportError 异常，更多信息详见 bpo-3770 。后续说明的任何专用队列对象亦如此。 |


## SimpleQueue
**class multiprocessing.SimpleQueue**
这是一个简化的 Queue 类的实现，很像带锁的 Pipe 。
| 方法 | 描述 |
| --- | --- |
| empty() | 如果队列为空返回 True ，否则返回 False 。 |
| get() | 从队列中移出并返回一个对象。 |
| put(item) | 将 item 放入队列。 |


## JoinableQueue
**class multiprocessing.JoinableQueue([maxsize])**
JoinableQueue 类是 Queue 的子类，额外添加了 task_done() 和 join() 方法。
| 方法 | 描述 |
| --- | --- |
| task_done() | 指出之前进入队列的任务已经完成。由队列的消费者进程使用。对于每次调用 get() 获取的任务，执行完成后调用 task_done() 告诉队列该任务已经处理完成。如果 join() 方法正在阻塞之中，该方法会在所有对象都被处理完的时候返回 (即对之前使用 put() 放进队列中的所有对象都已经返回了对应的 task_done() ) 。如果被调用的次数多于放入队列中的项目数量，将引发 ValueError 异常 。 |
| join() | 阻塞至队列中所有的元素都被接收和处理完毕。当条目添加到队列的时候，未完成任务的计数就会增加。每当消费者进程调用 task_done() 表示这个条目已经被回收，该条目所有工作已经完成，未完成计数就会减少。当未完成计数降到零的时候， join() 阻塞被解除。 |


# 杂项

| 方法 | 描述 |
| --- | --- |
| multiprocessing.active_children() | 返回当前进程存活的子进程的列表。调用该方法有“等待”已经结束的进程的副作用。 |
| multiprocessing.cpu_count() | 返回系统的CPU数量。该数量不同于当前进程可以使用的CPU数量。可用的CPU数量可以由 len(os.sched_getaffinity(0)) 方法获得。可能引发 NotImplementedError 。 |
| multiprocessing.current_process() | 返回与当前进程相对应的 Process 对象。和 threading.current_thread() 相同。 |
| multiprocessing.parent_process() | 返回父进程 Process  对象，和父进程调用 current_process() 返回的对象一样。如果一个进程已经是主进程， parent_process 会返回 None. |
| multiprocessing.freeze_support() | 为使用了 multiprocessing  的程序，提供冻结以产生 Windows 可执行文件的支持。(在 py2exe, PyInstaller 和 cx_Freeze 上测试通过)需要在 main 模块的 if __name__ == '__main__' 该行之后马上调用该函数。如果没有调用 freeze_support() 在尝试运行被冻结的可执行文件时会抛出 RuntimeError 异常。对 freeze_support() 的调用在非 Windows 平台上是无效的。如果该模块在 Windows 平台的 Python 解释器中正常运行 (该程序没有被冻结)， 调用``freeze_support()`` 也是无效的。 |
| multiprocessing.get_all_start_methods() | 返回支持的启动方法的列表，该列表的首项即为默认选项。可能的启动方法有 'fork', 'spawn' 和``'forkserver'。在 Windows 中，只有  ``'spawn' 是可用的。Unix平台总是支持``'fork'`` 和``'spawn'，且 ``'fork' 是默认值。 |
| multiprocessing.get_context(method=None) | 返回一个 Context 对象。该对象具有和 multiprocessing 模块相同的API。如果 method 设置成 None 那么将返回默认上下文对象。否则 method  应该是 'fork', 'spawn', 'forkserver' 。 如果指定的启动方法不存在，将抛出 ValueError  异常。 |
| multiprocessing.get_start_method(allow_none=False) | 返回启动进程时使用的启动方法名。如果启动方法已经固定，并且 allow_none 被设置成 False ，那么启动方法将被固定为默认的启动方法，并且返回其方法名。如果启动方法没有设定，并且 allow_none 被设置成 True ，那么将返回 None  。返回值将为 'fork' , 'spawn' , 'forkserver' 或者 None 。 'fork'``是 Unix 的默认值，   ``'spawn' 是 Windows 的默认值。 |
| multiprocessing.set_executable() | 设置在启动子进程时使用的 Python 解释器路径。 |
| multiprocessing.set_start_method(method) | 设置启动子进程的方法。 method 可以是 'fork' , 'spawn' 或者 'forkserver' 。注意这最多只能调用一次，并且需要藏在 main 模块中，由 if __name__ == '__main__' 进行保护。 |




# 连接（Connection）对象
**class multiprocessing.connection.Connection**
| 方法 | 描述 |
| --- | --- |
| send(obj) | 将一个对象发送到连接的另一端，可以用 recv() 读取。发送的对象必须是可以序列化的，过大的对象 ( 接近 32MiB+ ，这个值取决于操作系统 ) 有可能引发 ValueError  异常。 |
| recv() | 返回一个由另一端使用 send() 发送的对象。该方法会一直阻塞直到接收到对象。 如果对端关闭了连接或者没有东西可接收，将抛出 EOFError  异常。 |
| fileno() | 返回由连接对象使用的描述符或者句柄。 |
| close() | 关闭连接对象。当连接对象被垃圾回收时会自动调用。 |
| poll([timeout]) | 返回连接对象中是否有可以读取的数据。如果未指定 timeout ，此方法会马上返回。如果 timeout 是一个数字，则指定了最大阻塞的秒数。如果 timeout 是 None  ，那么将一直等待，不会超时。注意通过使用 multiprocessing.connection.wait() 可以一次轮询多个连接对象。 |
| send_bytes(buffer[, offset[, size]]) | 从一个 bytes-like object  （字节类对象）对象中取出字节数组并作为一条完整消息发送。如果由 offset  给定了在 buffer 中读取数据的位置。 如果给定了 size ，那么将会从缓冲区中读取多个字节。 过大的缓冲区 ( 接近 32MiB+ ，此值依赖于操作系统 ) 有可能引发 ValueError  异常。 |
| recv_bytes([maxlength]) | 以字符串形式返回一条从连接对象另一端发送过来的字节数据。此方法在接收到数据前将一直阻塞。 如果连接对象被对端关闭或者没有数据可读取，将抛出 EOFError  异常。如果给定了 maxlength 并且消息长于 maxlength 那么将抛出 OSError 并且该连接对象将不再可读。 |
| recv_bytes_into(buffer[, offset]) | 将一条完整的字节数据消息读入 buffer 中并返回消息的字节数。 此方法在接收到数据前将一直阻塞。 如果连接对象被对端关闭或者没有数据可读取，将抛出 EOFError  异常。 |



# 同步原语
| 方法 | 描述 |
| --- | --- |
| class multiprocessing.Barrier(parties[, action[, timeout]]) | 类似 threading.Barrier 的栅栏对象。 |
| class multiprocessing.BoundedSemaphore([value]) | 非常类似 threading.BoundedSemaphore 的有界信号量对象。一个小小的不同在于，它的 acquire  方法的第一个参数名是和 Lock.acquire() 一样的 block 。 |
| class multiprocessing.Condition([lock]) | 条件变量： threading.Condition 的别名。指定的 lock 参数应该是 multiprocessing 模块中的 Lock 或者 RLock 对象。 |
| class multiprocessing.Event | A clone of threading.Event. |
| class multiprocessing.Semaphore([value]) | 一种信号量对象: 类似于 threading.Semaphore.一个小小的不同在于，它的 acquire  方法的第一个参数名是和 Lock.acquire() 一样的 block 。 |
| class multiprocessing.Lock | - |
| class multiprocessing.RLock | -  |

## Lock
**class multiprocessing.Lock**
原始锁（非递归锁）对象，类似于 threading.Lock 。一旦一个进程或者线程拿到了锁，后续的任何其他进程或线程的其他请求都会被阻塞直到锁被释放。任何进程或线程都可以释放锁。除非另有说明，否则 multiprocessing.Lock  用于进程或者线程的概念和行为都和 threading.Lock  一致。
| 方法 | 描述 |
| --- | --- |
| acquire(block=True, timeout=None) | 获得锁，阻塞或非阻塞的。 |
| release() | 释放锁，可以在任何进程、线程使用，并不限于锁的拥有者。 |


## RLock
**class multiprocessing.RLock**
| 方法 | 描述 |
| --- | --- |
| acquire(block=True, timeout=None) | 获得锁，阻塞或非阻塞的。 |
| release() | 释放锁，使锁内的递归等级减一。如果释放后锁内的递归等级降低为0，则会重置锁的状态为释放状态（即没有被任何进程、线程持有），重置后如果有有其他进程和线程在等待这把锁，他们中的一个会获得这个锁而继续运行。如果释放后锁内的递归等级还没到达0，则这个锁仍将保持未释放状态且当前进程和线程仍然是持有者。只有当前进程或线程是锁的持有者时，才允许调用这个方法。如果当前进程或线程不是这个锁的拥有者，或者这个锁处于已释放的状态(即没有任何拥有者)，调用这个方法会抛出 AssertionError 异常。注意这里抛出的异常类型和 threading.RLock.release() 中实现的行为不一样。 |



# 共享 ctypes 对象
| 方法 | 描述 |
| --- | --- |
| `multiprocessing.Value(typecode_or_type, *args, lock=True)` | 返回一个从共享内存上创建的 ctypes 对象。默认情况下返回的对象实际上是经过了同步器包装过的。可以通过 Value 的 value 属性访问这个对象本身。 |
| `multiprocessing.Array(typecode_or_type, size_or_initializer, *, lock=True)` | 从共享内存中申请并返回一个具有ctypes类型的数组对象。默认情况下返回值实际上是被同步器包装过的数组对象。 |



# multiprocessing.sharedctypes 模块
| 方法 | 描述 |
| --- | --- |
| multiprocessing.sharedctypes.RawArray(typecode_or_type, size_or_initializer) | 从共享内存中申请并返回一个 ctypes 数组。 |
| `multiprocessing.sharedctypes.RawValue(typecode_or_type, *args)` | 从共享内存中申请并返回一个 ctypes 对象。 |
| `multiprocessing.sharedctypes.Array(typecode_or_type, size_or_initializer, *, lock=True)` | 返回一个纯 ctypes 数组, 或者在此之上经过同步器包装过的进程安全的对象，这取决于 lock 参数的值，除此之外，和 RawArray() 一样。 |
| `multiprocessing.sharedctypes.Value(typecode_or_type, *args, lock=True)` | 返回一个纯 ctypes 数组, 或者在此之上经过同步器包装过的进程安全的对象，这取决于 lock 参数的值，除此之外，和 RawArray() 一样。 |
| multiprocessing.sharedctypes.copy(obj) | 从共享内存中申请一片空间将 ctypes 对象 obj 过来，然后返回一个新的 ctypes 对象。 |
| multiprocessing.sharedctypes.synchronized(obj[, lock]) | 将一个 ctypes 对象包装为进程安全的对象并返回，使用 lock 同步对于它的操作。如果 lock 是 None (默认值) ，则会自动创建一个 multiprocessing.RLock 对象。 |




# 管理器
**multiprocessing.Manager()**
返回一个已启动的 SyncManager 管理器对象，这个对象可以用于在不同进程中共享数据。返回的管理器对象对应了一个已经启动的子进程，并且拥有一系列方法可以用于创建共享对象、返回对应的代理。 |


## managers.BaseManager
**class multiprocessing.managers.BaseManager([address[, authkey]])**
创建一个 BaseManager 对象。
一旦创建，应该及时调用 start() 或者 get_server().serve_forever() 以确保管理器对象对应的管理进程已经启动。
| 方法 | 描述 |
| --- | --- |
| start([initializer[, initargs]]) | 为管理器开启一个子进程，如果 initializer 不是 None , 子进程在启动时将会调用 `initializer(*initargs)` 。 |
| get_server() | 返回一个 Server  对象，它是管理器在后台控制的真实的服务。 Server  对象拥有 serve_forever() 方法。 |
| connect() | 将本地管理器对象连接到一个远程管理器进程: |
| shutdown() | 停止管理器的进程。这个方法只能用于已经使用 start() 启动的服务进程。可以被多次调用。 |
| register(typeid[, callable[, proxytype[, exposed[, method_to_typeid[, create_method]]]]]) | 一个 classmethod，可以将一个类型或者可调用对象注册到管理器类。typeid 是一种 "类型标识符"，用于唯一表示某种共享对象类型，必须是一个字符串。callable 是一个用来为此类型标识符创建对象的可调用对象。如果一个管理器实例将使用 connect() 方法连接到服务器，或者 create_method 参数为 False，那么这里可留下 None。proxytype 是 BaseProxy  的子类，可以根据 typeid 为共享对象创建一个代理，如果是 None , 则会自动创建一个代理类。exposed 是一个函数名组成的序列，用来指明只有这些方法可以使用 BaseProxy._callmethod() 代理。(如果 exposed 是 None, 则会在 proxytype._exposed_ 存在的情况下转而使用它) 当暴露的方法列表没有指定的时候，共享对象的所有 “公共方法” 都会被代理。（这里的“公共方法”是指所有拥有 __call__() 方法并且不是以 '_' 开头的属性）method_to_typeid 是一个映射，用来指定那些应该返回代理对象的暴露方法所返回的类型。（如果 method_to_typeid 是 None, 则 proxytype._method_to_typeid_ 会在存在的情况下被使用）如果方法名称不在这个映射中或者映射是 None ,则方法返回的对象会是一个值拷贝。create_method 指明，是否要创建一个以 typeid 命名并返回一个代理对象的方法，这个函数会被服务进程用于创建共享对象，默认为 True 。 |
| address | 管理器所用的地址。BaseManager 实例的只读属性。 |


## managers.SyncManager
**class multiprocessing.managers.SyncManager**
BaseManager 的子类，可用于进程的同步。这个类型的对象使用 multiprocessing.Manager() 创建。
它拥有一系列方法，可以为大部分常用数据类型创建并返回 代理对象 代理，用于进程间同步。甚至包括共享列表和字典。
| 方法 | 描述 |
| --- | --- |
| Barrier(parties[, action[, timeout]]) | 创建一个共享的 threading.Barrier 对象并返回它的代理。 |
| BoundedSemaphore([value]) | 创建一个共享的 threading.BoundedSemaphore 对象并返回它的代理。 |
| Condition([lock]) | 创建一个共享的 threading.Condition 对象并返回它的代理。如果提供了 lock 参数，那它必须是 threading.Lock 或 threading.RLock 的代理对象。 |
| Event() | 创建一个共享的 threading.Event 对象并返回它的代理。 |
| Lock() | 创建一个共享的 threading.Lock 对象并返回它的代理。 |
| Namespace() | 创建一个共享的 Namespace 对象并返回它的代理。 |
| Queue([maxsize]) | 创建一个共享的 queue.Queue 对象并返回它的代理。 |
| RLock() | 创建一个共享的 threading.RLock 对象并返回它的代理。 |
| Semaphore([value]) | 创建一个共享的 threading.Semaphore 对象并返回它的代理。 |
| Array(typecode, sequence) | 创建一个数组并返回它的代理。 |
| Value(typecode, value) | 创建一个具有可写 value 属性的对象并返回它的代理。 |
| dict()、dict(mapping)、dict(sequence) | 创建一个共享的 dict 对象并返回它的代理。 |
| list()、list(sequence) | 创建一个共享的 list 对象并返回它的代理。 |


**class multiprocessing.managers.Namespace**
一个可以注册到 SyncManager 的类型。



# 代理对象
**class multiprocessing.managers.BaseProxy**
代理对象是 BaseProxy 派生类的实例。
| 方法 | 描述 |
| --- | --- |
| _callmethod(methodname[, args[, kwds]]) | 调用指涉对象的方法并返回结果。 |
| _getvalue() | 返回指涉对象的一份拷贝。如果指涉对象无法序列化，则会抛出一个异常。 |
| __repr__() | 返回代理对象的内部字符串表示。 |
| __str__() | 返回指涉对象的内部字符串表示。 |



# 进程池
## pool.Pool
**class multiprocessing.pool.Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])**
一个进程池对象，它控制可以提交作业的工作进程池。它支持带有超时和回调的异步结果，以及一个并行的 map 实现。processes 是要使用的工作进程数目。如果 processes 为 None，则使用 os.cpu_count() 返回的值。
| 方法 | 描述 |
| --- | --- |
| apply(func[, args[, kwds]]) | 使用 args 参数以及 kwds 命名参数调用 func , 它会返回结果前阻塞。这种情况下，apply_async() 更适合并行化工作。另外 func 只会在一个进程池中的一个工作进程中执行。 |
| apply_async(func[, args[, kwds[, callback[, error_callback]]]]) | apply() 方法的一个变种，返回一个结果对象。如果指定了 callback , 它必须是一个接受单个参数的可调用对象。当执行成功时， callback 会被用于处理执行后的返回结果，否则，调用 error_callback 。如果指定了 error_callback , 它必须是一个接受单个参数的可调用对象。当目标函数执行失败时， 会将抛出的异常对象作为参数传递给 error_callback 执行。回调函数应该立即执行完成，否则会阻塞负责处理结果的线程。 |
| map(func, iterable[, chunksize]) | 内置 map() 函数的并行版本 (但它只支持一个 iterable 参数，对于多个可迭代对象请参阅 starmap())。 它会保持阻塞直到获得结果。这个方法会将可迭代对象分割为许多块，然后提交给进程池。可以将 chunksize 设置为一个正整数从而（近似）指定每个块的大小可以。注意对于很长的迭代对象，可能消耗很多内存。可以考虑使用 imap() 或 imap_unordered() 并且显示指定 chunksize 以提升效率。 |
| map_async(func, iterable[, chunksize[, callback[, error_callback]]]) | 和 map() 方法类似，但是返回一个可用于获取结果的对象。如果指定了 callback , 它必须是一个接受单个参数的可调用对象。当执行成功时， callback 会被用于处理执行后的返回结果，否则，调用 error_callback 。如果指定了 error_callback , 它必须是一个接受单个参数的可调用对象。当目标函数执行失败时， 会将抛出的异常对象作为参数传递给 error_callback 执行。回调函数应该立即执行完成，否则会阻塞负责处理结果的线程。 |
| imap(func, iterable[, chunksize]) | map() 的延迟执行版本。chunksize 参数的作用和 map() 方法的一样。对于很长的迭代器，给 chunksize 设置一个很大的值会比默认值 1 极大 地加快执行速度。同样，如果 chunksize 是 1 , 那么 imap() 方法所返回的迭代器的 next() 方法拥有一个可选的 timeout 参数： 如果无法在 timeout 秒内执行得到结果，则``next(timeout)`` 会抛出 multiprocessing.TimeoutError 异常。 |
| imap_unordered(func, iterable[, chunksize]) | 和 imap() 相同，只不过通过迭代器返回的结果是任意的。（当进程池中只有一个工作进程的时候，返回结果的顺序才能认为是"有序"的） |
| starmap(func, iterable[, chunksize]) | 和 map() 类似，不过 iterable 中的每一项会被解包再作为函数参数。比如可迭代对象 [(1,2), (3, 4)] 会转化为等价于 [func(1,2), func(3,4)] 的调用。 |
| starmap_async(func, iterable[, chunksize[, callback[, error_callback]]]) | 相当于 starmap() 与 map_async() 的结合，迭代 iterable 的每一项，解包作为 func 的参数并执行，返回用于获取结果的对象。 |
| close() | 阻止后续任务提交到进程池，当所有任务执行完成后，工作进程会退出。 |
| terminate() | 不必等待未完成的任务，立即停止工作进程。当进程池对象呗垃圾回收时， 会立即调用 terminate() 。 |
| join() | 等待工作进程结束。调用 join() 前必须先调用 close() 或者 terminate() 。 |



## pool.AsyncResult
**class multiprocessing.pool.AsyncResult**
Pool.apply_async() 和 Pool.map_async() 返回对象所属的类。
| 方法 | 描述 |
| --- | --- |
| get([timeout]) | 用于获取执行结果。如果 timeout 不是 None 并且在 timeout 秒内仍然没有执行完得到结果，则抛出 multiprocessing.TimeoutError 异常。如果远程调用发生异常，这个异常会通过 get() 重新抛出。 |
| wait([timeout]) | 阻塞，直到返回结果，或者 timeout 秒后超时。 |
| ready() | 返回执行状态，是否已经完成。 |
| successful() | 判断调用是否已经完成并且未引发异常。 如果还未获得结果则将引发 ValueError。 |



# 监听者及客户端
| 方法 | 描述 |
| --- | --- |
| multiprocessing.connection.deliver_challenge(connection, authkey) | 发送一个随机生成的消息到另一端，并等待回复。 |
| multiprocessing.connection.answer_challenge(connection, authkey) | 接收一条信息，使用 authkey 作为键计算信息摘要，然后将摘要发送回去。 |
| multiprocessing.connection.Client(address[, family[, authkey]]) | 尝试使用 address 地址上的监听者建立一个连接，返回 Connection 。 |
| multiprocessing.connection.wait(object_list, timeout=None) | 一直等待直到 object_list 中某个对象处于就绪状态。返回 object_list 中处于就绪状态的对象。如果 timeout 是一个浮点型，该方法会最多阻塞这么多秒。如果 timeout 是 None ，则会允许阻塞的事件没有限制。timeout为负数的情况下和为0的情况相同。 |
| class multiprocessing.connection.Listener([address[, family[, backlog[, authkey]]]]) | 可以监听连接请求，是对于绑定套接字或者 Windows 命名管道的封装。 |


## connection.Listener 的方法
| 方法 | 描述 |
| --- | --- |
| accept() | 接受一个连接并返回一个 Connection 对象，其连接到的监听器对象已绑定套接字或者命名管道。如果已经尝试过认证并且失败了，则会抛出 AuthenticationError 异常。 |
| close() | 关闭监听器对象上的绑定套接字或者命名管道。此函数会在监听器被垃圾回收后自动调用。不过仍然建议显式调用函数关闭。 |
| address | 监听器对象使用的地址。 |
| last_accepted | 最后一个连接所使用的地址。如果没有的话就是 None 。 |



# 日志
当前模块也提供了一些对 logging 的支持。注意， logging 模块本身并没有使用进程间共享的锁，所以来自于多个进程的日志可能（具体取决于使用的日志 handler 类型）相互覆盖或者混杂。
| 方法 | 描述 |
| --- | --- |
| multiprocessing.get_logger() | 返回 multiprocessing 使用的 logger，必要的话会创建一个新的。如果创建的首个 logger 日志级别为 logging.NOTSET 并且没有默认 handler。通过这个 logger 打印的消息不会传递到根 logger。注意在 Windows 上，子进程只会继承父进程 logger 的日志级别 - 对于logger的其他自定义项不会继承。 |
| multiprocessing.log_to_stderr() | 此函数会调用 get_logger() 但是会在返回的 logger 上增加一个 handler，将所有输出都使用 '[%(levelname)s/%(processName)s] %(message)s' 的格式发送到 sys.stderr 。 |























