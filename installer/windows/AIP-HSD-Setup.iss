; AIP-HSD Universal Polyglot Setup Script (Inno Setup)
; Allows user to select Backend and Frontend stack during installation.

[Setup]
AppName=AI-Powered Hybrid Security Dashboard (AIP-HSD)
AppVersion=1.1.0
DefaultDirName={pf}\AIP-HSD
DefaultGroupName=AIP-HSD
OutputBaseFilename=AIP-HSD-Universal-Setup
Compression=lzma
SolidCompression=yes

[Types]
Name: "custom"; Description: "Custom Installation"; Flags: iscustom

[Components]
Name: "backend"; Description: "AIP-HSD Backend Services"; Types: custom
Name: "backend\python"; Description: "Python Backend (FastAPI)"; Types: custom
Name: "backend\nodejs"; Description: "Node.js Backend (Express)"; Types: custom
Name: "backend\go"; Description: "Go Backend (Gin)"; Types: custom
Name: "backend\rust"; Description: "Rust Backend (Axum)"; Types: custom

Name: "frontend"; Description: "AIP-HSD Frontend Dashboard"; Types: custom
Name: "frontend\react"; Description: "React Dashboard (TypeScript)"; Types: custom
Name: "frontend\nextjs"; Description: "Next.js Dashboard"; Types: custom
Name: "frontend\static"; Description: "Static HTML HUD"; Types: custom

[Files]
; Python Backend Files
Source: "..\..\backend\python\*"; DestDir: "{app}\backend\python"; Components: backend\python; Flags: recursesubdirs
; Node.js Backend Files
Source: "..\..\backend\nodejs\*"; DestDir: "{app}\backend\nodejs"; Components: backend\nodejs; Flags: recursesubdirs
; ... and so on for all stacks

[Icons]
Name: "{group}\AIP-HSD Dashboard"; Filename: "{app}\frontend\static\index.html"
