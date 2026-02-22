import os
import re

def corregir_rutas_en_archivo(ruta_archivo):
    """Corrige todas las rutas de Alfredo a felip en un archivo"""
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
    base_path = r"c:\Users\felip\Documents\GitHub\oldbot"
    
    # Buscar todos los archivos .ahk que contienen referencias a Alfredo
    archivos_con_alfredo = []
    for raiz, subdirs, archivos in os.walk(base_path):
        for archivo in archivos:
            if archivo.endswith('.ahk'):
                ruta_completa = os.path.join(raiz, archivo)
                try:
                    with open(ruta_completa, 'r', encoding='utf-8', errors='ignore') as f:
                        contenido = f.read()
                        if 'C:\\Users\\Alfredo\\Documents\\GitHub\\oldbot' in contenido:
                            archivos_con_alfredo.append(ruta_completa)
                except:
                    continue
    
    # Corregir todos los archivos encontrados
    corregidos = 0
    errores = 0
    
    for archivo in archivos_con_alfredo:
        if corregir_rutas_en_archivo(archivo):
            corregidos += 1
        else:
            errores += 1
    
    print(f"\n=== CORRECCIÓN FINAL ===")
    print(f"Archivos con referencias a Alfredo encontrados: {len(archivos_con_alfredo)}")
    print(f"Archivos corregidos correctamente: {corregidos}")
    print(f"Archivos con errores: {errores}")
    
    if errores == 0:
        print("🎉 TODAS LAS REFERENCIAS A FELIP HAN SIDO CORREGIDAS")
        print("🚀 AHORA EL BOT DEBERÍA FUNCIONAR SIN ERRORES DE RUTA")
        return True
    else:
        print("💥 HUBO ERRORES AL CORREGIR ALGUNOS ARCHIVOS")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("✨ EJECUTA CORRECTA - BOT LISTO PARA FUNCIONAR")
