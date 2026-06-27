[Setup]
AppName=Sticky Notes
AppVersion=1.0
DefaultDirName={pf}\StickyNotes
DefaultGroupName=Sticky Notes
OutputDir=dist_installer
OutputBaseFilename=StickyNotesInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

Source: "resources\icon.ico"; DestDir: "{app}\resources"; Flags: ignoreversion

[Icons]
Name: "{group}\Sticky Notes"; Filename: "{app}\main.exe"

Name: "{commondesktop}\Sticky Notes"; Filename: "{app}\main.exe"

[Run]
Filename: "{app}\main.exe"; Description: "Run Sticky Notes"; Flags: nowait postinstall skipifsilent

[Registry]
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; \
ValueType: string; ValueName: "StickyNotes"; ValueData: "{app}\main.exe"; Flags: uninsdeletevalue