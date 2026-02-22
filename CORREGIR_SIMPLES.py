import os

def corregir_rutas_en_archivo(ruta_archivo):
    """Corrige todas las rutas de Alfredo a felip en un archivo"""
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # Reemplazar todas las referencias de Alfredo a felip
        contenido_corregido = contenido.replace('C:\\\\Users\\Alfredo\\Documents\\GitHub\\oldbot', 'C:\\\\Users\\felip\\Documents\\GitHub\\oldbot')
        
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            f.write(contenido_corregido)
        
        print(f"Corregido: {os.path.basename(ruta_archivo)}")
        return True
    except Exception as e:
        print(f"Error en {ruta_archivo}: {e}")
        return False

def main():
    # Lista de archivos principales a corregir
    archivos_principales = [
        "OldBot Launcher.ahk",
        "OldBot Pro.ahk",
        "Setup.ahk"
    ]
    
    corregidos = 0
    errores = 0
    
    for archivo in archivos_principales:
        ruta_completa = os.path.join("c:\\Users\\felip\\Documents\\GitHub\\oldbot", archivo)
        if os.path.exists(ruta_completa):
            if corregir_rutas_en_archivo(ruta_completa):
                corregidos += 1
            else:
                errores += 1
    
    print(f"\n=== CORRECCIÓN ===")
    print(f"Archivos principales corregidos: {corregidos}")
    print(f"Archivos con errores: {errores}")
    
    if errores == 0:
        print("✅ ARCHIVOS PRINCIPALES CORREGIDOS")
        return True
    else:
        print("❌ ERRORES AL CORREGIR ARCHIVOS PRINCIPALES")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("✅ LISTO PARA PROBAR EL BOT")
