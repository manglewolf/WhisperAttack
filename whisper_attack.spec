# -*- mode: python ; coding: utf-8 -*-

APP_NAME = 'WhipserAttack'

a = Analysis(
    ['whisper_attack.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('fuzzy_words.txt','.'),
        ('add_icon.png','.'),
        ('word_mappings.txt','.'),
        ('settings.cfg','.'),
        ('whisper_attack_icon.png','.'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=APP_NAME,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=APP_NAME,  
)

# --- POST-BUILD ASSET MOVER ---
import os
import shutil

# PyInstaller defines 'DISTPATH' globally inside the spec build context
dist_root = os.path.join(DISTPATH, APP_NAME)
internal_dir = os.path.join(dist_root, '_internal')

root_files = [
    'fuzzy_words.txt', 
    'add_icon.png', 
    'word_mappings.txt', 
    'settings.cfg', 
    'whisper_attack_icon.png'
]

# This block fires reliably because it parses immediately after the COLLECT step
if os.path.exists(internal_dir):
    for file_name in root_files:
        source = os.path.join(internal_dir, file_name)
        destination = os.path.join(dist_root, file_name)
        if os.path.exists(source):
            if os.path.exists(destination):
                os.remove(destination)
            shutil.move(source, destination)
            print(f"--> Successfully moved {file_name} to root folder.")
