# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir al Chatbot UVG! Este documento te guiará en el proceso.

---

## 📋 Tabla de Contenidos

1. [Código de Conducta](#código-de-conducta)
2. [¿Cómo Contribuir?](#cómo-contribuir)
3. [Reportar Bugs](#reportar-bugs)
4. [Sugerir Mejoras](#sugerir-mejoras)
5. [Pull Requests](#pull-requests)
6. [Estilo de Código](#estilo-de-código)
7. [Estructura del Proyecto](#estructura-del-proyecto)

---

## 📜 Código de Conducta

### Nuestro Compromiso

Nos comprometemos a hacer de este proyecto una experiencia libre de acoso para todos, independientemente de:
- Edad
- Tamaño corporal
- Discapacidad
- Etnia
- Identidad y expresión de género
- Nivel de experiencia
- Nacionalidad
- Apariencia personal
- Raza
- Religión
- Identidad y orientación sexual

### Comportamiento Esperado

- Usar lenguaje acogedor e inclusivo
- Respetar diferentes puntos de vista
- Aceptar críticas constructivas
- Enfocarse en lo mejor para la comunidad
- Mostrar empatía hacia otros miembros

### Comportamiento Inaceptable

- Uso de lenguaje o imágenes sexualizadas
- Comentarios insultantes o despectivos
- Acoso público o privado
- Publicar información privada de otros
- Conducta inapropiada en contexto profesional

---

## 🚀 ¿Cómo Contribuir?

### 1. Fork del Repositorio

```bash
# Haz fork en GitHub, luego clona tu fork
git clone https://github.com/TU-USUARIO/chatbot-uvg.git
cd chatbot-uvg
```

### 2. Crea una Rama

```bash
# Crea una rama para tu feature o fix
git checkout -b feature/nueva-funcionalidad
# o
git checkout -b fix/correccion-bug
```

### 3. Haz tus Cambios

- Escribe código limpio y documentado
- Sigue el estilo de código existente
- Agrega comentarios donde sea necesario
- Prueba tus cambios localmente

### 4. Commit

```bash
# Agrega tus cambios
git add .

# Commit con mensaje descriptivo
git commit -m "feat: agregar función de exportar PDF"
# o
git commit -m "fix: corregir error en validación de API key"
```

### 5. Push y Pull Request

```bash
# Push a tu fork
git push origin feature/nueva-funcionalidad

# Luego crea un Pull Request en GitHub
```

---

## 🐛 Reportar Bugs

### Antes de Reportar

1. Verifica que no sea un problema de configuración
2. Busca en issues existentes
3. Prueba con la última versión

### Cómo Reportar

Crea un issue con:

**Título**: Descripción breve del bug

**Descripción**:
```markdown
## Descripción del Bug
[Descripción clara del problema]

## Pasos para Reproducir
1. Ve a '...'
2. Haz click en '...'
3. Scroll hasta '...'
4. Ver error

## Comportamiento Esperado
[Qué debería pasar]

## Comportamiento Actual
[Qué está pasando]

## Screenshots
[Si aplica]

## Entorno
- OS: [ej. Windows 11]
- Navegador: [ej. Chrome 120]
- Versión: [ej. 1.0.0]

## Información Adicional
[Cualquier otro contexto]
```

---

## 💡 Sugerir Mejoras

### Tipos de Mejoras

- **Features**: Nueva funcionalidad
- **Enhancement**: Mejora de funcionalidad existente
- **Documentation**: Mejora de documentación
- **Performance**: Optimización de rendimiento
- **UI/UX**: Mejora de interfaz

### Template de Sugerencia

```markdown
## Descripción de la Mejora
[Descripción clara de la mejora]

## Motivación
[Por qué es necesaria esta mejora]

## Solución Propuesta
[Cómo implementarías la mejora]

## Alternativas Consideradas
[Otras opciones que consideraste]

## Impacto
- [ ] Breaking change
- [ ] Requiere actualización de docs
- [ ] Afecta performance
```

---

## 🔄 Pull Requests

### Checklist

Antes de enviar tu PR, verifica:

- [ ] El código sigue el estilo del proyecto
- [ ] Has probado los cambios localmente
- [ ] Has actualizado la documentación
- [ ] Los commits tienen mensajes descriptivos
- [ ] No hay conflictos con main
- [ ] Has agregado comentarios donde es necesario

### Proceso de Review

1. **Envío**: Creas el PR con descripción clara
2. **Review**: Mantenedores revisan el código
3. **Feedback**: Pueden solicitar cambios
4. **Aprobación**: Una vez aprobado, se hace merge
5. **Merge**: Tu código se integra al proyecto

### Template de PR

```markdown
## Descripción
[Descripción de los cambios]

## Tipo de Cambio
- [ ] Bug fix
- [ ] Nueva feature
- [ ] Breaking change
- [ ] Documentación

## ¿Cómo se ha Probado?
[Describe las pruebas realizadas]

## Checklist
- [ ] Mi código sigue el estilo del proyecto
- [ ] He realizado self-review
- [ ] He comentado código complejo
- [ ] He actualizado la documentación
- [ ] Mis cambios no generan warnings
- [ ] He probado en diferentes navegadores

## Screenshots (si aplica)
[Agrega screenshots]
```

---

## 🎨 Estilo de Código

### JavaScript

```javascript
// ✅ Bueno
function calculateCost(tokens, pricePerMillion) {
    const cost = (tokens / 1000000) * pricePerMillion;
    return cost.toFixed(4);
}

// ❌ Malo
function calc(t,p){return (t/1000000)*p;}
```

**Reglas**:
- Usa `const` y `let`, no `var`
- Nombres descriptivos en camelCase
- Funciones con verbos (get, set, calculate, etc.)
- Comentarios para lógica compleja
- Espacios después de keywords

### HTML

```html
<!-- ✅ Bueno -->
<div class="chat-message">
    <p class="message-content">Hola mundo</p>
</div>

<!-- ❌ Malo -->
<div class=chat-message><p class=message-content>Hola mundo</p></div>
```

**Reglas**:
- Indentación de 4 espacios
- Atributos con comillas dobles
- Nombres de clase en kebab-case
- Estructura semántica

### CSS

```css
/* ✅ Bueno */
.chat-container {
    display: flex;
    flex-direction: column;
    padding: 20px;
}

/* ❌ Malo */
.chat-container{display:flex;flex-direction:column;padding:20px;}
```

**Reglas**:
- Una propiedad por línea
- Orden alfabético de propiedades
- Nombres descriptivos
- Comentarios para secciones

### Commits

```bash
# ✅ Bueno
git commit -m "feat: agregar exportación a PDF"
git commit -m "fix: corregir validación de API key"
git commit -m "docs: actualizar guía de instalación"

# ❌ Malo
git commit -m "cambios"
git commit -m "fix"
git commit -m "update"
```

**Prefijos**:
- `feat:` - Nueva funcionalidad
- `fix:` - Corrección de bug
- `docs:` - Documentación
- `style:` - Formato, no afecta código
- `refactor:` - Refactorización
- `test:` - Agregar tests
- `chore:` - Mantenimiento

---

## 📁 Estructura del Proyecto

```
BOT-UVG/
├── index.html              # Chatbot básico
├── index-advanced.html     # Chatbot avanzado
├── start.html             # Página de inicio
├── guia.html              # Guía interactiva
│
├── config.js              # Configuración
├── models.js              # Modelos de IA
├── utils.js               # Utilidades
├── styles.css             # Estilos adicionales
│
├── README.md              # Documentación principal
├── QUICKSTART.md          # Guía rápida
├── TECHNICAL.md           # Docs técnicas
├── PROMPTS.md             # Biblioteca de prompts
├── DEPLOYMENT.md          # Guía de despliegue
├── PROJECT_SUMMARY.md     # Resumen del proyecto
├── CONTRIBUTING.md        # Esta guía
│
├── LICENSE                # Licencia MIT
├── .gitignore            # Archivos ignorados
└── package.json          # Configuración npm
```

---

## 🎯 Áreas de Contribución

### 🔴 Alta Prioridad

- [ ] Agregar tests automatizados
- [ ] Implementar backend para API keys
- [ ] Mejorar accesibilidad (WCAG)
- [ ] Optimizar performance
- [ ] Agregar más modelos de IA

### 🟡 Media Prioridad

- [ ] Tema oscuro completo
- [ ] Exportar a diferentes formatos
- [ ] Búsqueda en historial
- [ ] Atajos de teclado adicionales
- [ ] Integración con servicios UVG

### 🟢 Baja Prioridad

- [ ] Más temas de colores
- [ ] Animaciones adicionales
- [ ] Easter eggs
- [ ] Más idiomas
- [ ] App móvil nativa

---

## 🧪 Testing

### Manual Testing

Antes de enviar PR, prueba:

1. **Funcionalidad Básica**
   - [ ] Enviar mensaje
   - [ ] Recibir respuesta
   - [ ] Guardar API key
   - [ ] Limpiar conversación

2. **Navegadores**
   - [ ] Chrome
   - [ ] Firefox
   - [ ] Safari
   - [ ] Edge

3. **Dispositivos**
   - [ ] Desktop
   - [ ] Tablet
   - [ ] Móvil

4. **Casos Edge**
   - [ ] Sin API key
   - [ ] API key inválida
   - [ ] Sin internet
   - [ ] Mensajes muy largos

### Automated Testing (Futuro)

```javascript
// Ejemplo de test con Jest
describe('ChatUtils', () => {
    test('sanitizeInput removes HTML tags', () => {
        const input = '<script>alert("xss")</script>';
        const output = ChatUtils.sanitizeInput(input);
        expect(output).not.toContain('<script>');
    });

    test('estimateTokens calculates correctly', () => {
        const text = 'Hello world';
        const tokens = ChatUtils.estimateTokens(text);
        expect(tokens).toBeGreaterThan(0);
    });
});
```

---

## 📚 Recursos para Contribuidores

### Documentación
- [README.md](README.md) - Información general
- [TECHNICAL.md](TECHNICAL.md) - Detalles técnicos
- [DEPLOYMENT.md](DEPLOYMENT.md) - Guía de despliegue

### Herramientas Útiles
- [VS Code](https://code.visualstudio.com/) - Editor recomendado
- [Git](https://git-scm.com/) - Control de versiones
- [GitHub Desktop](https://desktop.github.com/) - GUI para Git

### Extensiones VS Code
- ESLint - Linting de JavaScript
- Prettier - Formateo de código
- Live Server - Servidor local
- GitLens - Mejor integración con Git

---

## 🏆 Reconocimientos

### Contribuidores

Todos los contribuidores serán reconocidos en:
- README.md
- Página de inicio del proyecto
- Release notes

### Tipos de Contribución

No solo código cuenta como contribución:
- 📝 Documentación
- 🐛 Reportar bugs
- 💡 Sugerir features
- 🎨 Diseño
- 🌍 Traducciones
- 📢 Promoción
- 🧪 Testing

---

## ❓ Preguntas Frecuentes

### ¿Necesito experiencia previa?

No necesariamente. Hay tareas para todos los niveles:
- **Principiante**: Documentación, reportar bugs
- **Intermedio**: Fixes pequeños, mejoras UI
- **Avanzado**: Features nuevas, refactoring

### ¿Cuánto tiempo toma el review?

Generalmente 2-7 días. Depende de:
- Complejidad del cambio
- Disponibilidad de mantenedores
- Calidad del código

### ¿Qué pasa si mi PR es rechazado?

- Recibirás feedback constructivo
- Puedes hacer cambios y reenviar
- O discutir alternativas

### ¿Puedo trabajar en múltiples issues?

Sí, pero recomendamos:
- Empezar con uno
- Completarlo antes de tomar otro
- Comunicar si vas a tardar

---

## 📞 Contacto

### Para Contribuidores

- **Issues**: Para bugs y features
- **Discussions**: Para preguntas generales
- **Email**: [contacto si aplica]

### Mantenedores

- Revisan PRs
- Responden issues
- Guían contribuidores
- Mantienen el proyecto

---

## 🎉 ¡Gracias por Contribuir!

Tu contribución, sin importar el tamaño, hace que este proyecto sea mejor para todos.

**Pasos siguientes**:
1. Lee esta guía completa
2. Busca un issue para trabajar
3. Haz fork del repositorio
4. ¡Empieza a contribuir!

---

**¡Bienvenido al equipo! 🚀**

---

*Última actualización: 2026-03-06*
*Versión: 1.0.0*
