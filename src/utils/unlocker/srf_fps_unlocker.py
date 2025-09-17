
from copy import deepcopy
from utils.regedit.srf_regedit_io import  WriteRegistryValue
import winreg
import json
import os

def SrfFpsUnlocker(var , fps : int) -> None:
    """
    解锁FPS上限
    
    param : var , fps
    return : None
    """
    var.SRF_REGEDIT_INFO['FPS'] = deepcopy(fps)  # 修改FPS
    data = (json.dumps(var.SRF_REGEDIT_INFO) + '\x00').encode('utf-8')  # 编码为二进制字符串
    WriteRegistryValue(winreg.HKEY_CURRENT_USER , os.path.join(*var.SRF_INFO['PATH']['REGISTRY_KEY_PATH']) , var.SRF_INFO['PATH']['GRAPHICS_VALUE_NAME'] , data , winreg.REG_BINARY)  # 写入注册表