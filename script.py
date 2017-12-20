
import psutil

#获取内存信息
mem = psutil.virtual_memory()

print(mem)

#cpu的信息，包括执行的时间，cpu的核心数等

cpu = psutil.cpu_times()
print(cpu)
print(psutil.cpu_count(logical=False))

#磁盘信息
print(psutil.disk_io_counters())
print(psutil.disk_partitions())
#磁盘中分区参数的信息
print(psutil.disk_usage('/'))
#获取用户数
print("系统的用户数")
print(psutil.users())

#查看用户的进程pid
pid = psutil.pids()
print("用户的进程是",pid)

p = psutil.Process(907) #实例化一个一个进程实例

print("进程的名字是",p.name())

#进程的路径
print(p.exe()) 

#进程的状态
print("进程的状态是",p.status())

#进程的创建时间
print("进程的创建时间",p.create_time())
#uid
print("进程的uid是",p.uids())
#gid
print("进程的gid是",p.gids())
#cpu  affinity
#进程的利用率
print("进程的CPU占用率",p.cpu_percent())
print("进程的内容占有率",p.memory_percent())

#进程的内存rss,vms信息
print(p.memory_info())

#societ有关的进程数
print(p.connections)

#开启的进程数
print(p.threads())


#实用的IP地址处理模块
from IPy import IP


print("这个网段是属于",ip.iptype())

#为什么年轻人都都喜欢喝水呢？
