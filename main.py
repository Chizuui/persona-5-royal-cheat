import ctypes, utility
from ctypes import wintypes
from consts import *

kernel32 = ctypes.windll.kernel32

pid = utility.GetProcId("P5R.exe")
handle = kernel32.OpenProcess(PROCESS_ALL_ACCESS, 0, ctypes.wintypes.DWORD(pid))
base_address = utility.GetModuleBaseAddress(pid, "P5R.exe")
objectPointer = base_address + 0x1ECA01C

# Feature
features = [
    (ctypes.c_ulonglong(objectPointer + 0x0), ctypes.c_int(1)),  # protagonistHP
    (ctypes.c_ulonglong(objectPointer + 0x4), ctypes.c_int(999)),  # protagonistSP
    (ctypes.c_ulonglong(objectPointer + 0x10), ctypes.c_int(9999999)), # protagonistXP
    (ctypes.c_ulonglong(objectPointer + 0x0C), ctypes.c_int(99)), # protagonist level
    (ctypes.c_ulonglong(objectPointer + 0x2A0), ctypes.c_int(999)),  # RyujiHP
    (ctypes.c_ulonglong(objectPointer + 0x2A4), ctypes.c_int(999)),  # RyujiSP
    (ctypes.c_ulonglong(objectPointer + 0x2E0), ctypes.c_int(9999999)), # RyujiXP
    (ctypes.c_ulonglong(objectPointer + 0x540), ctypes.c_int(999)),  # MorganaHP
    (ctypes.c_ulonglong(objectPointer + 0x544), ctypes.c_int(999)),  # MorganaSP
    (ctypes.c_ulonglong(objectPointer + 0x580), ctypes.c_int(9999999)),  # MorganaXP
    (ctypes.c_ulonglong(objectPointer + 0x7E0), ctypes.c_int(999)),  # AnnHP
    (ctypes.c_ulonglong(objectPointer + 0x7E4), ctypes.c_int(999)),  # AnnSP
    (ctypes.c_ulonglong(objectPointer + 0x820), ctypes.c_int(9999999)),  # AnnXP
    (ctypes.c_ulonglong(objectPointer + 0xA80), ctypes.c_int(999)),  # YusukeHP
    (ctypes.c_ulonglong(objectPointer + 0xA84), ctypes.c_int(999)),  # YusukeSP
    (ctypes.c_ulonglong(objectPointer + 0xAC0), ctypes.c_int(9999999)),  # YusukeXP
    (ctypes.c_ulonglong(objectPointer + 0xD20), ctypes.c_int(999)),  # MakotoHP
    (ctypes.c_ulonglong(objectPointer + 0xD24), ctypes.c_int(999)),  # MakotoSP
    (ctypes.c_ulonglong(objectPointer + 0xD60), ctypes.c_int(9999999)),  # MakotoXP
    (ctypes.c_ulonglong(objectPointer + 0xFC0), ctypes.c_int(999)),  # HaruHP
    (ctypes.c_ulonglong(objectPointer + 0xFC4), ctypes.c_int(999)),  # HaruSP
    (ctypes.c_ulonglong(objectPointer + 0x1000), ctypes.c_int(9999999)),  # HaruXP
    (ctypes.c_ulonglong(base_address + 0x1ECB51C), ctypes.c_int(999)),  # AkechiHP
    (ctypes.c_ulonglong(base_address + 0x1ECB51C + 0x4), ctypes.c_int(999)),  # AkechiSP
    (ctypes.c_ulonglong(base_address + 0x1ECB51C + 0x40), ctypes.c_int(9999999)), #AkechiXP
    (ctypes.c_ulonglong(base_address + 0x1ECA01C + 0x1260), ctypes.c_int(999)),  # FutabaHP
    (ctypes.c_ulonglong(base_address + 0x1ECA01C + 0x1264), ctypes.c_int(999)),  # FutabaSP
    (ctypes.c_ulonglong(base_address + 0x1ECA01C + 0x12A0), ctypes.c_int(9999999)),  # FutabaXP
    (ctypes.c_ulonglong(base_address + 0x1ECB2BC + 0x500), ctypes.c_int(999)),  # KasumiHP
    (ctypes.c_ulonglong(base_address + 0x1ECB2BC + 0x504), ctypes.c_int(999)),  # KasumiSP
    (ctypes.c_ulonglong(base_address + 0x1ECB2BC + 0x540), ctypes.c_int(9999999)),  # KasumiXP
    (ctypes.c_ulonglong(base_address + 0x1ECD4DC), ctypes.c_int(9999999)),  # moneyPtr
    (ctypes.c_ulonglong(base_address + 0x1EFDCD8), ctypes.c_int(9999999)),  # thievesDenPtr
    (ctypes.c_ulonglong(base_address + 0x1EDD57C), ctypes.c_int(10)),  # Sojiro Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0x10), ctypes.c_int(10)),  # Takemi Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0x20), ctypes.c_int(10)),  # Mishima Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0x30), ctypes.c_int(10)),  # Maruki Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0x40), ctypes.c_int(10)),  # Yoshida Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0x50), ctypes.c_int(10)),  # Kasumi Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0x60), ctypes.c_int(10)),  # Akechi Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0x70), ctypes.c_int(10)),  # Yusuke Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0x80), ctypes.c_int(10)),  # Kawakami Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0x90), ctypes.c_int(10)),  # Ohya Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0xA0), ctypes.c_int(10)),  # Oda Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0xB0), ctypes.c_int(10)),  # Chihaya Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0xC0), ctypes.c_int(10)),  # Iwai Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0xD0), ctypes.c_int(10)),  # Sae Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0xE0), ctypes.c_int(10)),  # Makoto Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0xF0), ctypes.c_int(10)),  # Hifumi Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C+0x100), ctypes.c_int(10)),  # Futaba Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C-0x10), ctypes.c_int(10)),  # Morgana Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C-0x20), ctypes.c_int(10)),  # Ann Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C-0x30), ctypes.c_int(10)),  # Igor Confidant
    (ctypes.c_ulonglong(base_address + 0x1EDD57C-0x40), ctypes.c_int(10)),  # Ryuji Confidant
]

# Write to memory
while True:
    for address, value in features:
        kernel32.WriteProcessMemory(handle, address, ctypes.byref(value), ctypes.sizeof(value), None)
    print("Done!")
# Close handle
    kernel32.CloseHandle(handle) 
# If you want to lock your values, comment line 76
