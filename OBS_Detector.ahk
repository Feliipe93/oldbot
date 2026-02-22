/*
OBS Detector para OldBot - Función simple y segura
*/

; Función para detectar ventana de OBS
DetectarOBS() {
    WinGet, windows, List
    Loop, %windows% {
        WinGetTitle, title, % "ahk_id " windows%A_Index%
        WinGetClass, class, % "ahk_id " windows%A_Index%
        
        ; Buscar OBS con Game Capture
        if (InStr(title, "OBS") || InStr(title, "Game Capture")) {
            return windows%A_Index%
        }
    }
    return 0
}

; Probar detección
obsWindow := DetectarOBS()

if (obsWindow) {
    MsgBox, 64, OBS Detectado, ¡OBS detectado correctamente!`nID de ventana: %obsWindow%`n`nEl bot puede usar OBS para captura.
} else {
    MsgBox, 48, OBS No Detectado, OBS no detectado.`n`nAsegúrate de que OBS esté ejecutando con el juego capturado.
}

ExitApp
