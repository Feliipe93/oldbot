import os

def corregir_archivo(ruta_archivo):
    """Corrige todas las referencias de Alfredo a felip en un archivo"""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8', errors='ignore') as f:
            contenido = f.read()
        
        # Reemplazar todas las referencias de Alfredo a felip
        contenido_corregido = contenido.replace('C:\\Users\\Alfredo\\Documents\\GitHub\\oldbot', 'C:\\Users\\felip\\Documents\\GitHub\\oldbot')
        
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            f.write(contenido_corregido)
        
        print(f"Corregido: {os.path.basename(ruta_archivo)}")
        return True
    except Exception as e:
        print(f"Error en {ruta_archivo}: {e}")
        return False

def main():
    # Archivos principales que necesitan corrección
    archivos_a_corregir = [
        "OldBot Launcher.ahk",
        "OldBot Pro.ahk",
        "Setup.ahk"
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
    
    print(f"\n=== RESUMEN ===")
    print(f"Archivos corregidos: {corregidos}")
    print(f"Archivos con errores: {errores}")
    print(f"Total archivos procesados: {corregidos + errores}")
    
    if errores == 0:
        print("TODOS LOS ARCHIVOS PRINCIPALES HAN SIDO CORREGIDOS")
        print("AHORA PRUEBA EL BOT")
        return True
    else:
        print("HUBO ERRORES AL CORREGIR")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("EJECUTA: start \"AutoHotkey\" \"c:\\Users\\felip\\Documents\\GitHub\\oldbot\\OldBot Pro.ahk\"")
