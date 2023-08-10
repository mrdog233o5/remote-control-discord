# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


setup_a = Analysis(
    ['setup.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
setup_pyz = PYZ(setup_a.pure, setup_a.zipped_data, cipher=block_cipher)

setup_exe = EXE(
    setup_pyz,
    setup_a.scripts,
    [],
    exclude_binaries=False,
    name='setup',
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
	uac_admin=True,
)
main_a = Analysis(
    ['SchoolCheatTools.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
main_pyz = PYZ(main_a.pure, main_a.zipped_data, cipher=block_cipher)

main_exe = EXE(
    main_pyz,
    main_a.scripts,
    [],
    exclude_binaries=False,
    name='SchoolCheatTools',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
	uac_admin=True,
)
coll = COLLECT(
    setup_exe,
    setup_a.binaries,
    setup_a.zipfiles,
    setup_a.datas,
    main_exe,
    main_a.binaries,
    main_a.zipfiles,
    main_a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
	name='.build',
)
setup_app = BUNDLE(
    coll,
    name='setup.app',
    icon=None,
    bundle_identifier=None,
)
main_app = BUNDLE(
    coll,
    name='SchoolCheatTools.app',
    icon=None,
    bundle_identifier=None,
)
