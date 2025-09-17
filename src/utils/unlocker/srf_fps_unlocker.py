
from utils.regedit.srf_regedit_io import  WriteRegistryValue
import winreg
import json
import os

def SrfFpsUnlocker(var , fps : int) -> None:
    var.SRF_REGEDIT_INFO['FPS'] = fps
    data = (json.dumps(var.SRF_REGEDIT_INFO) + '\x00').encode('utf-8')
    WriteRegistryValue(winreg.HKEY_CURRENT_USER , os.path.join(*var.SRF_INFO['PATH']['REGISTRY_KEY_PATH']) , var.SRF_INFO['PATH']['GRAPHICS_VALUE_NAME'] , data , winreg.REG_BINARY)