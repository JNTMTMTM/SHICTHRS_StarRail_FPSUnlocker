
import winreg

def ReadRegistryValue(key, sub_key, value_name) -> dict:
    # 打开键
    registry_key = winreg.OpenKey(key, sub_key)

    # 读取键
    value, _ = winreg.QueryValueEx(registry_key, value_name)

    # 关闭键
    winreg.CloseKey(registry_key)

    # 返回键值
    return value


def WriteRegistryValue(key , sub_key , value_name , data , mode) -> None:
    # 开启键
    registry_key = winreg.CreateKey(key , sub_key)
    # 修改键
    winreg.SetValueEx(registry_key , value_name , 0 , mode , data)
    # 关闭键
    winreg.CloseKey(registry_key)
        
