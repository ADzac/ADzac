import shutil

total, used, free = shutil.disk_usage("/")

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))


import psutil
    
print(psutil.virtual_memory().total//(2**30))
print(psutil.virtual_memory().used//(2**30))
print(psutil.virtual_memory().free//(2**30))

import psutil

def get_cpu_usage_pct():
    """
    Obtains the system's average CPU load as measured over a period of 500 milliseconds.
    :returns: System CPU load as a percentage.
    :rtype: float
    """
    return psutil.cpu_percent(interval=0.5)

print('System CPU load is {} %'.format(get_cpu_usage_pct()))
print(psutil.sensors_temperatures())
