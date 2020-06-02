import psutil
print("------------------------------------------------")
print('1.To get the information about the pc ')
print('2.To get information about the boot-time of the computer ')
print('3.To get the information about the cpu_frequency ')
print('4.To get the information about the Disk-partations ')
print('5.To get the information about the Disk_io_counters ')
print('6.To get the information about the Net_io_counters ')
print('7.To get the swap memory of the system ')
print('8.To know the running pids ')
choice=input('enter the option to get the operation: ')
if choice=='1':
    print(psutil.cpu_stats())
elif choice=='2':
    print(psutil.boot_time())
elif choice=='3':
    print(psutil.cpu_freq())
elif choice=='4':
    print(psutil.disk_partitions())
elif choice=='5':
    print(psutil.disk_io_counters())
elif choice=='6':
    p=psutil.net_io_counters()
    print('No of packets sent :',p.packets_sent)
    print('No of packets recieve :',p.packets_recv)
    print("No of bytes sent :",p.bytes_sent)
    print('No of bytes recieved :',p.bytes_recv)
elif choice=='7':
    print(psutil.swap_memory())
elif choice=='8':
    print(psutil.pids())
else:
    print('----------SORRY FOR NOT SATISFYING YOUR OPTONS------------------------')
