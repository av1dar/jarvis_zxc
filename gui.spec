# Збірка: на Windows, у корені проєкту виконати:
#   pyinstaller gui.spec
# Результат: dist/JarvisSettings/JarvisSettings.exe

# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ["gui/jarvis_settings.py"],
    pathex=["."],
    binaries=[],
    datas=[
        ("custom_commands.yaml", "."),
        ("config.yaml", "."),
    ],
    hiddenimports=["yaml"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="JarvisSettings",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon="assets/icon.ico",
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="JarvisSettings",
)
