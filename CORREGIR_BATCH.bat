@echo off
echo Corrigiendo rutas de Alfredo a felip...

powershell -Command "Get-Content 'c:\Users\felip\Documents\GitHub\oldbot\OldBot Launcher.ahk' -replace 'C:\\Users\\Alfredo\\Documents\\GitHub\\oldbot', 'C:\\Users\\felip\\Documents\\GitHub\\oldbot' | Set-Content 'c:\Users\felip\Documents\GitHub\oldbot\OldBot Launcher.ahk'"

powershell -Command "Get-Content 'c:\Users\felip\Documents\GitHub\oldbot\OldBot Pro.ahk' -replace 'C:\\Users\\Alfredo\\Documents\\GitHub\\oldbot', 'C:\\Users\\felip\\Documents\\GitHub\\oldbot' | Set-Content 'c:\Users\felip\Documents\GitHub\oldbot\OldBot Pro.ahk'"

powershell -Command "Get-Content 'c:\Users\felip\Documents\GitHub\oldbot\Setup.ahk' -replace 'C:\\Users\\Alfredo\\Documents\\GitHub\\oldbot', 'C:\\Users\\felip\\Documents\\GitHub\\oldbot' | Set-Content 'c:\Users\felip\Documents\GitHub\oldbot\Setup.ahk'"

echo.
echo Rutas corregidas. Listo para probar el bot.

pause
