import os, sys, platform, ctypes, time, shutil
from tkinter import *

def get_date(file):
    "Returns the last modification access date of @file"
    try:
        date = time.ctime(os.stat(file).st_mtime)
        date = time.strptime(date, "%a %b %d %H:%M:%S %Y")
        date = time.strftime("%d/%m/%Y  %H:%M:%S", date)
        return date
    except FileNotFoundError:
        pass

def get_extension(file):
    """
        Returns the extension of the given @file
    """
    ext = []
    res = ""
    if file.startswith("."):
        res = file[1:]
    elif not '.' in file[1:]:
        res = ""
    else:
        index = len(file)-1
        for l in range(index,1,-1):
            if file[l] !='.':
                ext.append(file[l])
            else:
                break
        ext.reverse()
        for k in range(len(ext)):
            res += ext[k]
    return res.lower()

def get_size(path):
    """
        Returns the last modification date of the given file
    """
    try:
        return int(os.stat(path).st_size/1024)+1
    except FileNotFoundError:
        pass

def get_dirname(path, disk_name):
    """
        Returns the name of the current directory from the address bar or the name of the monted device @disk_name
    """
    temp = []
    res = ''
    if path[1] == ':' and len(path) == 3:
        return disk_name
    else:
        for l in range(len(path)-1,1,-1):
            if path[l] !='\\' and path[l] !='/':
                temp.append(path[l])
            else:
                break
    temp.reverse()
    for k in range(len(temp)):
        res += temp[k]
    return res

def findFileByExtension(path,ext):
    """
        Finds every files than ended with the extension @ext in the given @path
        
        return  res, paths

                res: an array that contains the name of the file
                paths: an array that contains the full path of files in res        
    """
    res = []
    paths = []
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            if get_file_extension(os.path.join(dirpath,f))==ext.upper():
                res.append(f)
                paths.append(os.path.join(dirpath,f))
    return res,paths

def get_os_info():

    info = platform.uname()
    print('System = {0}\nNetwork name = {1}\nRelease = {2}\nVersion = {3}\nVideo card = {4}\nProcessor = {5}'.format(info[0],info[1],info[2],info[3],info[4],info[5]))

"""
get_os_info()
print(platform.machine())
"""

def get_file_extension(path):
    """
        @ Returns the type of the given file
    """
    return os.path.splitext(path)[1][1:]

def get_device_name(drive_letter):
    """
        @params drive_letter: this the letter Windows use to identify connected devices
        @return the name of every connected devices such as disks, USB
        Source: stackoverflow
    """
    kernel32 = ctypes.windll.kernel32
    volumeNameBuffer = ctypes.create_unicode_buffer(1024)
    fileSystemNameBuffer = ctypes.create_unicode_buffer(1024)
    serial_number = None
    max_component_length = None
    file_system_flags = None

    rc = kernel32.GetVolumeInformationW(
            ctypes.c_wchar_p(drive_letter+':\\'),
            volumeNameBuffer,
            ctypes.sizeof(volumeNameBuffer),
            serial_number,
            max_component_length,
            file_system_flags,
            fileSystemNameBuffer,
            ctypes.sizeof(fileSystemNameBuffer)
    )
    return volumeNameBuffer.value

def delete_file(f):
    """
        @params f
        Remove the file named f from the computer
    """
    if os.path.isdir(f):
        try:
            os.rmdir(f)
        except OSError:
            shutil.rmtree(f, ignore_errors=True)
    elif os.path.isfile(f):
        os.remove(f)
    else:
        pass
            
def checker(temp):
    """
        @params temp
        Checks if the filename @temp contains characters in pattern.
    """
    pattern = '\\!/:*?<>|'
    for i in range(len(temp)):
        if temp[i] in pattern:
            return False
    return True