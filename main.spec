# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
hidden = collect_submodules('au_ootp_tournament_utilities_v2')
hidden += collect_submodules('apps')

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
       ('image_assets', 'au_ootp_tournament_utilities_v2\\image_assets'),
       ('settings_default.ini', '.'),
       ('README.md', '.')],
    hiddenimports=hidden,
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
    a.binaries,
    a.datas,
    [],
    name='main',
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
)