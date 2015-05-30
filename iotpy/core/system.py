import psutil

class System(object):

    def __init__(self):
        pass

    def bootTime(self):
        return datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

    def cpuUser(self):
        output = psutil.cpu_times_percent(interval=1, percpu=False)
        return "%.1f" % output.user

    def cpuSystem(self):
        output = psutil.cpu_times_percent(interval=1, percpu=False)
        return "%.1f" % output.system

# End of File
