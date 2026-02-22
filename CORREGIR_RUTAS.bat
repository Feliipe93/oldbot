@echo off
echo Corrigiendo todas las referencias de "Alfredo" a "felip"...
echo.

REM Corregir archivos principales
powershell -Command "(Get-Content 'c:\Users\felip\Documents\GitHub\oldbot\__Files\Shared\OldBot\ClientAreas\_AbstractClientArea.ahk') -replace 'C:\\Users\\Alfredo\\Documents\\GitHub\\oldbot', 'C:\\Users\\felip\\Documents\\GitHub\\oldbot' | Set-Content 'c:\Users\felip\Documents\GitHub\oldbot\__Files\Shared\OldBot\ClientAreas\_AbstractClientArea.ahk'"

powershell -Command "(Get-Content 'c:\Users\felip\Documents\GitHub\oldbot\__Files\Shared\OldBot\ImageSearch\_AbstractBase64Image.ahk') -replace 'C:\\Users\\Alfredo\\Documents\\GitHub\\oldbot', 'C:\\Users\\felip\\Documents\\GitHub\\oldbot' | Set-Content 'c:\Users\felip\Documents\GitHub\oldbot\__Files\Shared\OldBot\ImageSearch\_AbstractBase64Image.ahk'"

powershell -Command "(Get-Content 'c:\Users\felip\Documents\GitHub\oldbot\__Files\Shared\OldBot\ImageSearch\_AbstractBitmapSearch.ahk') -replace 'C:\\Users\\Alfredo\\Documents\\GitHub\\oldbot', 'C:\\Users\\felip\\Documents\\GitHub\\oldbot' | Set-Content 'c:\Users\felip\Documents\GitHub\oldbot\__Files\Shared\OldBot\ImageSearch\_AbstractBitmapSearch.ahk'"

powershell -Command "(Get-Content 'c:\Users\felip\Documents\GitHub\oldbot\__Files\Shared\OldBot\ImageSearch\_AbstractImageSearch.ahk') -replace 'C:\\Users\\Alfredo\\Documents\\GitHub\\oldbot', 'C:\\Users\\felip\\Documents\\GitHub\\oldbot' | Set-Content 'c:\Users\felip\Documents\GitHub\oldbot\__Files\Shared\OldBot\ImageSearch\_AbstractImageSearch.ahk'"

powershell -Command "(Get-Content 'c:\Users\felip\Documents\GitHub\oldbot\__Files\Shared\OldBot\ImageSearch\_Base64ImageSearch.ahk') -replace 'C:\\Users\\Alfredo\\Documents\\GitHub\\oldbot', 'C:\\Users\\felip\\Documents\\GitHub\\oldbot' | Set-Content 'c:\Users\felip\Documents\GitHub\oldbot\__Files\Shared\OldBot\ImageSearch\_Base64ImageSearch.ahk'"

powershell -Command "(Get-Content 'c:\Users\felip\Documents\GitHub\oldbot\__Files\Shared\OldBot\ImageSearch\_BitmapImageSearch.ahk') -replace 'C:\\Users\\Alfredo\\Documents\\GitHub\\oldbot', 'C:\\Users\\felip\\Documents\\GitHub\\oldbot' | Set-Content 'c:\Users\felip\Documents\GitHub\oldbot\__Files\Shared\OldBot\ImageSearch\_BitmapImageSearch.ahk'"

echo.
echo Corregidos 5 archivos principales...
pause
