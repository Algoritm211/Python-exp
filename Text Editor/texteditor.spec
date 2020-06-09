# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['texteditor.py'],
             pathex=['/Users/alexfrost/Desktop/Python projects/Text Editor'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='texteditor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='/Users/alexfrost/Desktop/Python projects/Text Editor/texteditor.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='texteditor')
app = BUNDLE(coll,
             name='texteditor.app',
             icon='/Users/alexfrost/Desktop/Python projects/Text Editor/texteditor.ico',
             bundle_identifier=None)
