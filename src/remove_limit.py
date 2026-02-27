import winreg

def unlimit(name: str):
    if name == "" or name is None:
        return 1
    path = f'Software\\{name}'
    value_name = "SetUnlimit"

    try:
        key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, path, access=winreg.KEY_WRITE)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        return 0
    except FileNotFoundError:
        return 2