import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la ruta desde el archivo .env
# El segundo argumento es un valor por defecto (None) si no se encuentra la variable
downloads_path_raw = os.getenv("DOWNLOADS_DIR")


def get_downloads_path():
    """
    Verifica y retorna la ruta de descargas configurada.
    """
    if not downloads_path_raw:
        print("❌ ERROR: No se encontró la variable DOWNLOADS_DIR en el archivo .env")
        return None

    # Convertimos la cadena de texto en un objeto Path (más fácil de manejar)
    path = Path(downloads_path_raw)

    # Verificamos si la ruta realmente existe en tu computadora
    if path.exists() and path.is_dir():
        return path
    else:
        print(f"❌ ERROR: La ruta especificada no existe o no es una carpeta: {path}")
        return None


# Bloque de prueba: Solo se ejecuta si corres este archivo directamente en PyCharm
if __name__ == "__main__":
    print("--- Verificando Configuración de GestorAcadem ---")
    ruta = get_downloads_path()

    if ruta:
        print(f"✅ Configuración exitosa.")
        print(f"📍 Carpeta de descargas detectada en: {ruta}")
    else:
        print("⚠️ Hay un problema con la configuración. Revisa tu archivo .env")