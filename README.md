### README - **CLI de Actividad de Usuario en GitHub**

https://roadmap.sh/projects/github-user-activity
---

#### **Descripción del Proyecto**
Este proyecto es una herramienta de línea de comandos (CLI) que permite obtener la actividad reciente de un usuario de GitHub utilizando la API de GitHub. Con este programa, puedes consultar eventos como commits, creación de issues, pull requests, forks, y más, de una manera sencilla y accesible desde la terminal.

---

#### **Características**
- **Consultar actividad reciente**: Obtiene y muestra hasta 10 eventos recientes del usuario en GitHub.
- **Soporte para varios tipos de eventos**:
  - Pushes (subir commits).
  - Issues (crear o modificar).
  - Pull requests (crear, fusionar, cerrar, etc.).
  - Forks (copiar repositorios).
  - Stars (marcar repositorios como favoritos).
- **Manejo de errores**:
  - Detecta nombres de usuario inválidos.
  - Maneja problemas de conexión.
  - Responde a errores de la API.
- **Sin dependencias externas**: Implementado usando solo las bibliotecas estándar de Python.

---

#### **Requisitos**
- Python 3.x instalado en tu sistema.
- Conexión a Internet para consultar la API de GitHub.

---

#### **Instalación**
1. Clona este repositorio o guarda el archivo `github_activity.py` en tu sistema.
2. Asegúrate de que Python esté instalado y configurado en tu PATH.

---

#### **Uso**
Para ejecutar el script, abre una terminal y proporciona un nombre de usuario de GitHub como argumento:

```bash
python github_activity.py <Usuario_GitHub>
```

##### **Ejemplo**:
```bash
python github_activity.py torvalds
```

##### **Salida Esperada**:
```plaintext
Obteniendo actividad reciente del usuario de GitHub: torvalds...

Actividad reciente en GitHub:
- Subió 2 commit(s) a torvalds/linux
- Marcó con estrella el repositorio someuser/some-repo
- Hizo un fork de repository-owner/repository-name
```

---

#### **Comandos**
- **Consultar actividad reciente**:
  ```bash
  python github_activity.py <Usuario_GitHub>
  ```

---

#### **Mejoras Opcionales**
- **Filtrar por tipo de evento**: Agregar un filtro opcional para mostrar solo ciertos eventos, como commits o forks.
- **Almacenamiento en caché**: Implementar una funcionalidad para guardar resultados localmente y evitar realizar múltiples solicitudes a la API.
- **Información adicional del usuario**: Mostrar datos como seguidores, repositorios públicos y biografía del usuario.

---

#### **Limitaciones**
- **Límite de la API de GitHub**: El límite para usuarios no autenticados es de 60 solicitudes por hora. Si necesitas realizar más solicitudes, puedes usar un token de autenticación (no implementado en este proyecto).
- **Sólo los 10 eventos más recientes**: La API devuelve los eventos en orden cronológico, mostrando solo los más recientes.

---

#### **Notas Técnicas**
- **Endpoint utilizado**:  
  `https://api.github.com/users/<usuario>/events`  
  Este endpoint devuelve un listado de eventos realizados por el usuario en GitHub.
- **Errores manejados**:
  - Nombres de usuario no existentes.
  - Problemas de conexión a Internet o a la API.
  - Respuesta HTTP no exitosa.

---

#### **Licencia**
Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente. 

---

¡Gracias por usar el CLI de Actividad de Usuario en GitHub! 🚀 Si tienes alguna duda o sugerencia, no dudes en contactarme. 😊