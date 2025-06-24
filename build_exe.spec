# -*- mode: python ; coding: utf-8 -*-


a1 = Analysis(
    ["osb.py"],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=["refnx", "pint", "scipy.special", "scipy.sparse"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz1 = PYZ(a1.pure)
splash1 = Splash(
    "splash.png",
    binaries=a1.binaries,
    datas=a1.datas,
    text_pos=(18, 460),
    text_size=12,
    text_color="black",
    minify_script=True,
    always_on_top=True,
    text_default="Loading Sample Builder...",
)


exe1 = EXE(
    pyz1,
    a1.scripts,
    splash1,
    [],
    exclude_binaries=True,
    name="osb",
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

a2 = Analysis(
    ["orso_viewer.py"],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=["refnx", "pint", "scipy.special", "scipy.sparse"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz2 = PYZ(a2.pure)
splash2 = Splash(
    "splash.png",
    binaries=a2.binaries,
    datas=a2.datas,
    text_pos=(18, 460),
    text_size=12,
    text_color="black",
    minify_script=True,
    always_on_top=True,
    text_default="Loading ORSO Viewer...",
)


exe2 = EXE(
    pyz2,
    a2.scripts,
    splash2,
    [],
    exclude_binaries=True,
    name="orso_viewer",
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
    exe1,
    a1.binaries,
    a1.datas,
    splash1.binaries,
    exe2,
    a2.binaries,
    a2.datas,
    splash2.binaries,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="orso_tools",
)
