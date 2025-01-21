import sys
import json
import urllib.request
import urllib.error


def obtener_actividad_github(usuario):
    """Obtiene la actividad reciente de un usuario de GitHub usando la API de GitHub."""
    url = f"https://api.github.com/users/{usuario}/events"
    
    try:
        # Solicitar datos de la API de GitHub
        with urllib.request.urlopen(url) as respuesta:
            if respuesta.status == 200:
                datos = json.load(respuesta)
                return datos
    except urllib.error.HTTPError as e:
        print(f"Error: No se pudo obtener la información. Código HTTP {e.code}")
    except urllib.error.URLError as e:
        print(f"Error: No se pudo conectar a la API de GitHub. Razón: {e.reason}")
    
    return None


def mostrar_actividad(actividad):
    """Muestra la actividad reciente del usuario de GitHub en un formato legible."""
    if not actividad:
        print("No se encontró actividad o ocurrió un error.")
        return

    print("\nActividad reciente en GitHub:")
    for i, evento in enumerate(actividad[:10]):  # Mostrar solo los 10 eventos más recientes
        tipo_evento = evento.get("type")
        nombre_repo = evento["repo"]["name"]
        
        if tipo_evento == "PushEvent":
            commits = len(evento["payload"]["commits"])
            print(f"- Subió {commits} commit(s) a {nombre_repo}")
        elif tipo_evento == "IssuesEvent":
            accion = evento["payload"]["action"]
            print(f"- {accion.capitalize()} un issue en {nombre_repo}")
        elif tipo_evento == "WatchEvent":
            print(f"- Marcó con estrella el repositorio {nombre_repo}")
        elif tipo_evento == "ForkEvent":
            print(f"- Hizo un fork de {nombre_repo}")
        elif tipo_evento == "PullRequestEvent":
            accion = evento["payload"]["action"]
            print(f"- {accion.capitalize()} un pull request en {nombre_repo}")
        else:
            print(f"- {tipo_evento} en {nombre_repo}")


def main():
    """Función principal para manejar argumentos y ejecutar las funciones."""
    if len(sys.argv) < 2:
        print("Uso: python github_activity.py <Usuario_GitHub>")
        return

    usuario = sys.argv[1]
    print(f"Obteniendo actividad reciente del usuario de GitHub: {usuario}...\n")
    
    actividad = obtener_actividad_github(usuario)
    mostrar_actividad(actividad)


if __name__ == "__main__":
    main()
