# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/pudszTTIOT/Desktop/py/Python Creations/Completed/Projects/The Vinyl Frontier (TVF)/Version 1.1/homepage.py', 'C:/Users/pudszTTIOT/Desktop/py/Python Creations/Completed/Projects/The Vinyl Frontier (TVF)/Version 1.1/main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='The Vinyl Frontier (TVF) v1.1',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\pudszTTIOT\\Desktop\\py\\Python Creations\\Completed\\Projects\\The Vinyl Frontier (TVF)\\Images\\The Vinyl Frontier 2.ico'],
)
