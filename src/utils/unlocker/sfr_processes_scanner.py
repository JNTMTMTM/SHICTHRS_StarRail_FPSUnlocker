
from typing import Union
import psutil
def GetAllProcesses() -> Union[list , bool]:
    """
    获取所有进程
    
    FUNC-LOADED -> None

    param : None
    return : Union[list , bool]
    """
    processes = []  # 初始化进程表
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):  # 遍历所有进程
        try:
            processes.append((proc.info)['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            return None
    return processes
