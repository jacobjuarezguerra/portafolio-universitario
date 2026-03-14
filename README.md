# Portafolio Universitario - Jacob Juárez Guerra

Portafolio web desarrollado para la tarea universitaria de Ingeniería en Ciencias de la Computación en la Universidad del Valle de Guatemala (UVG).

## Características

- 🎨 Diseño limpio con paleta de colores UVG (verde y blanco)
- 🌙 Modo oscuro (activado manualmente)
- ✨ Animaciones moderadas al hacer scroll
- 🔒 Sección privada con contraseña
- 📱 Diseño responsive (móvil y escritorio)
- 🤖 Chatbot UVG integrado con IA

## Estructura

```
portafolio-universitario/
├── index.html              # Página principal
├── about.html             # Acerca de mí
├── primer-mes.html        # Mi primer mes en la universidad
├── aprendi-computacion.html # Mis aprendizajes en Computación
├── privado.html           # Sección privada (requiere contraseña)
├── css/
│   └── styles.css         # Estilos
├── js/
│   └── main.js            # JavaScript
├── assets/
│   └── images/            # Imágenes
├── trabajos-hechos/       # Trabajos y proyectos
└── README.md
```

## Contraseña de la sección privada

La contraseña es: `marranapuerk`

## Cómo publicar en GitHub Pages

### Opción 1: Usando Git (recomendado)

1. Crea un repositorio nuevo en GitHub (público)
2. En tu terminal, navega a la carpeta del portafolio:
   ```bash
   cd portafolio-universitario
   ```
3. Inicializa git:
   ```bash
   git init
   ```
4. Agrega los archivos:
   ```bash
   git add .
   ```
5. Haz tu primer commit:
   ```bash
   git commit -m "Mi portafolio universitario"
   ```
6. Agrega el remoto de GitHub:
   ```bash
   git remote add origin https://github.com/TU_USUARIO/NOMBRE_REPO.git
   ```
7. Sube los archivos:
   ```bash
   git push -u origin main
   ```

### Habilitar GitHub Pages

1. Ve a tu repositorio en GitHub
2. Click en **Settings**
3. En el menú izquierdo, click en **Pages**
4. En "Build and deployment", en "Source", selecciona **Deploy from a branch**
5. En "Branch", selecciona **main** y **/(root)**
6. Click en **Save**
7. Espera 1-2 minutos y tu sitio estará disponible en:
   `https://TU_USUARIO.github.io/NOMBRE_REPO/`

### ⚠️ Nota importante

El archivo `trabajos-hechos/chatbot/BOT-UVG-Preview/index.html` contiene una API key pre-configurada. Esta es para uso personal. Si planeas hacer el repositorio público, considera:
- Usar tu propia API key
- Implementar un backend para manejar la API key de forma segura

## Personalización

### Cambiar contraseña
Edita el archivo `js/main.js` y busca:
```javascript
const CORRECT_PASSWORD = 'marranapuerk';
```

### Cambiar API key del chatbot
Edita el archivo `aprendi-computacion.html` y busca la línea con la API key.

## Contenido del Portafolio

- **Inicio**: Información general y navegación
- **Acerca de**: Mis intereses personales
- **Mi Primer Mes**: Trabajos de todos los cursos
- **Computación**: Diagramas de flujo, loops Python, chatbot
- **Privado**: Reflexión personal (contraseña requerida)

---

Hecho con ❤️ para UVG
