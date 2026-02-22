import os
import re

def corregir_archivo(ruta_archivo):
    """Corrige todas las referencias de Alfredo a felip en un archivo"""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8', errors='ignore') as f:
            contenido = f.read()
        
        # Reemplazar todas las referencias de Alfredo a felip
        contenido_corregido = contenido.replace('C:\\Users\\Alfredo\\Documents\\GitHub\\oldbot', 'C:\\Users\\felip\\Documents\\GitHub\\oldbot')
        
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            f.write(contenido_corregido)
        
        print(f"✅ Corregido: {os.path.basename(ruta_archivo)}")
        return True
    except Exception as e:
        print(f"❌ Error en {ruta_archivo}: {e}")
        return False

def main():
    # Archivos principales que necesitan corrección según el grep
    archivos_a_corregir = [
        "OldBot Launcher.ahk",
        "OldBot Pro.ahk", 
        "Setup.ahk",
        "Cavebot.ahk",
        "Data\\Executables\\Support.ahk",
        "Data\\Executables\\Alerts.ahk",
        "Data\\Executables\\Fishing.ahk",
        "Data\\Executables\\ItemRefill.ahk",
        "Data\\Executables\\Runemaker.ahk",
        "Data\\Executables\\SioFriend.ahk"
        "__Files\\Includes\\_Core.ahk",
        "__Files\\Includes\\Actions\\ICavebot.ahk",
        "__Files\\Includes\\Alerts.ahk",
        "__Files\\Includes\\Cavebot\\ICavebot.ahk",
        "__Files\\Includes\\Client.ahk",
        "__Files\\Includes\\Fishing.ahk",
        "__Files\\Includes\\GUI Classes.ahk",
        "__Files\\Includes\\GUI.ahk",
        "__Files\\Includes\\IHealing.ahk",
        "__Files\\Includes\\IActionScripts.ahk",
        "__Files\\Includes\\IClientJson.ahk",
        "__Files\\Includes\\IComponents.ahk",
        "__Files\\Includes\\IExecutables.ahk",
        "__Files\\Includes\\ILibraries.ahk",
        "__Files\\Includes\\ILooting.ahk",
        "__Files\\Includes\\IMainOldBotObjects.ahk",
        "__Files\\Includes\\IObjects.ahk",
        "__Files\\Includes\\IPolicies.ahk",
        "__Files\\Includes\\IPositions.ahk",
        "__Files\\Includes\\IRunemaker.ahk",
        "__Files\\Includes\\ISettingsGuis.ahk",
        "__Files\\Includes\\ISioComponents.ahk",
        "__Files\\Includes\\ISupport.ahk",
        "__Files\\Includes\\Item Refill.ahk",
        "__Files\\Includes\\Navigation.ahk",
        "__Files\\Includes\\Persistent.ahk",
        "__Files\\Includes\\Reconnect.ahk",
        "__Files\\Includes\\Script.ahk",
        "__Files\\Includes\\Sio.ahk",
        "__Files\\Includes\\Targeting.ahk",
        "__Files\\Includes\\Waypoint.ahk",
        "__Files\\Includes\\IEvents.ahk",
        "__Files\\Includes\\ILibraries.ahk",
        "__Files\\Includes\\Actions\\ICavebot.ahk",
        "__Files\\Includes\\IHotkeys.ahk",
        "__Files\\Includes\\hotkeys\\hotkeys_actionscript.ahk",
        "__Files\\Includes\\hotkeys\\hotkeys_floorspy.ahk",
        "__Files\\Includes\\hotkeys\\hotkeys_main.ahk",
        "__Files\\Includes\\hotkeys\\hotkeys_mapviewer.ahk",
        "__Files\\Includes\\hotkeys\\hotkeys_tibia.ahk",
        "__Files\\Includes\\hotkeys\\hotkeys_oldbot_window.ahk",
        "__Files\\Includes\\hotkeys\\hotkeys_waypoint.ahk",
        "__Files\\Includes\\hotkeys\\hotkeys_actionscript.ahk",
        "__Files\\Includes\\hotkeys\\hotkeys_floorspy.ahk",
        "__Files\\Includes\\_Magnifier.ahk",
        "__Files\\Includes\\Window Events\\gui_close.ahk",
        "__Files\\Includes\\Window Events\\gui_escape.ahk",
        "__Files\\Shared\\OldBot\\default_functions.ahk",
        "__Files\\Shared\\OldBot\\ClientAreas\\_AbstractClientArea.ahk",
        "__Files\\Shared\\OldBot\\ImageSearch\\_AbstractBase64Image.ahk",
        "__Files\\Shared\\OldBot\\ImageSearch\\_AbstractBitmapSearch.ahk",
        "__Files\\Shared\\OldBot\\ImageSearch\\_AbstractImageSearch.ahk",
        "__Files\\Shared\\OldBot\\ImageSearch\\_Base64ImageSearch.ahk",
        "__Files\\Shared\\OldBot\\ImageSearch\\_BitmapImageSearch.ahk",
        "__Files\\Shared\\OldBot\\ImageSearch\\_ImageSearch.ahk",
        "__Files\\Shared\\OldBot\\Includes\\_IOldBotObjects.ahk",
        "__Files\\Shared\\OldBot\\Objects\\_Memory\\_MemoryAddress.ahk",
        "__Files\\Shared\\OldBot\\Objects\\_BitmapIcon.ahk",
        "__Files\\Shared\\OldBot\\Objects\\_CharCoordinate.ahk",
        "__Files\\Shared\\OldBot\\Objects\\_ClickParams.ahk",
        "__Files\\Shared\\OldBot\\Objects\\_Coordinate.ahk",
        "__Files\\Shared\\OldBot\\Objects\\_Coordinates.ahk",
        "__Files\\Shared\\OldBot\\Objects\\_Icon.ahk",
        "__Files\\Shared\\OldBot\\Objects\\_MapCoordinate.ahk",
        "__Files\\Shared\\OldBot\\Objects\\_Process.ahk",
        "__Files\\Shared\\OldBot\\Objects\\_ProcessQueue.ahk",
        "__Files\\Shared\\OldBot\\Requests\\_AbstractRequest.ahk",
        "__Files\\Shared\\OldBot\\Requests\\_AbstractUpdaterRequest.ahk",
        "__Files\\Shared\\OldBot\\Requests\\_DownloadFileRequest.ahk",
        "__Files\\Shared\\OldBot\\Requests\\_GetHashesRequest.ahk",
        "__Files\\Shared\\OldBot\\Requests\\_UploadFileRequest.ahk",
        "__Files\\Shared\\OldBot\\Settings\\_Ini\\_AbstractIniSettings.ahk",
        "__Files\\Shared\\OldBot\\Settings\\_Ini\\_GlobalIniSettings.ahk",
        "__Files\\Shared\\OldBot\\Settings\\_JSON\\_AbstractClientJsonSettings.ahk",
        "__Files\\Shared\\OldBot\\Settings\\_JSON\\_AbstractJsonSettings.ahk",
        "__Files\\Shared\\OldBot\\Settings\\_Objects\\_IObjects.ahk",
        "__Files\\Shared\\OldBot\\Settings\\_Objects\\_DefaultBoolean.ahk",
        "__Files\\Shared\\OldBot\\Settings\\_Objects\\_DefaultEnum.ahk",
        "__Files\\Shared\\OldBot\\Settings\\_Objects\\_DefaultString.ahk",
        "__Files\\Shared\\OldBot\\Settings\\_Objects\\_DefaultValue.ahk",
        "__Files\\Shared\\OldBot\\Settings\\_AbstractSettings.ahk",
        "__Files\\Shared\\OldBot\\Settings\\_MemorySettings.ahk"
    ]
    
    corregidos = 0
    errores = 0
    
    for archivo in archivos_a_corregir:
        ruta_completa = os.path.join("c:\\Users\\felip\\Documents\\GitHub\\oldbot", archivo)
        if os.path.exists(ruta_completa):
            if corregir_archivo(ruta_completa):
                corregidos += 1
            else:
                errores += 1
        else:
            print(f"⚠️  No existe: {archivo}")
            errores += 1
    
    print(f"\n=== RESUMEN FINAL ===")
    print(f"✅ Archivos corregidos: {corregidos}")
    print(f"❌ Archivos con errores: {errores}")
    print(f"📁 Total archivos procesados: {corregidos + errores}")
    
    if errores == 0:
        print("🎉 TODAS LAS REFERENCIAS A ALFREDO HAN SIDO CORREGIDAS")
        print("🚀 AHORA EL BOT DEBERÍA FUNCIONAR SIN ERRORES DE PATH")
        return True
    else:
        print("💥 HUBO ERRORES - REVISAR MANUALMENTE")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("✨ EJECUTA EL BOT PARA VERIFICAR QUE TODO FUNCIONE CORRECTAMENTE")
