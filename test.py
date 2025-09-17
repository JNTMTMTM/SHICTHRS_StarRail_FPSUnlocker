
import winreg
import json

# Specify the registry key path
registry_key_path = r"SOFTWARE\miHoYo\崩坏：星穹铁道"
# Specify the value name
graphics_value_name = "GraphicsSettings_Model_h2986158309"


def set_game_fps(fps: int) -> None:
    """
    Set the FPS of the game.

    Parameters:
    - fps
    """
    value = read_registry_value(winreg.HKEY_CURRENT_USER, registry_key_path, graphics_value_name)

    data_dict = json.loads(value.decode('utf-8').strip('\x00'))

    data_dict['FPS'] = fps
    data = (json.dumps(data_dict) + '\x00').encode('utf-8')
    write_registry_value(winreg.HKEY_CURRENT_USER, registry_key_path, graphics_value_name, data, winreg.REG_BINARY)


def read_registry_value(key, sub_key, value_name):
    """
    Read the content of the specified registry value.

    Parameters:
    - key: The handle of an open registry key.
    - sub_key: The name of the key, relative to key, to open.
    - value_name: The name of the value to query.

    Returns:
        The content of the specified value in the registry.
    """
    try:
        # Open the specified registry key
        registry_key = winreg.OpenKey(key, sub_key)
        # Read the content of the specified value in the registry
        value, _ = winreg.QueryValueEx(registry_key, value_name)
        # Close the registry key
        winreg.CloseKey(registry_key)
        return value
    except FileNotFoundError:
        # raise FileNotFoundError(f"Specified registry key or value not found: {sub_key}\\{value_name}")
        return None
    except Exception as e:
        raise Exception(f"Error reading registry value: {e}")

def write_registry_value(key, sub_key, value_name, data, mode) -> None:
    """
    Write a registry value to the specified registry key.

    Parameters:
    - key: The registry key.
    - sub_key: The subkey under the specified registry key.
    - value_name: The name of the registry value.
    - data: The data to be written to the registry.
    - mode: The type of data.
    """
    try:
        # Open or create the specified registry key
        registry_key = winreg.CreateKey(key, sub_key)
        # Write data to the registry
        winreg.SetValueEx(registry_key, value_name, 0, mode, data)
        # Close the registry key
        winreg.CloseKey(registry_key)
    except Exception as e:
        raise Exception(f"Error writing registry value: {e}")

set_game_fps(120)