# 🚀 Guía de Inicio Rápido - Chatbot UVG

## ⚡ Configuración en 3 Minutos

### Paso 1: Obtener API Key (2 minutos)

1. Ve a [openrouter.ai](https://openrouter.ai)
2. Crea una cuenta gratuita
3. Ve a la sección "Keys"
4. Haz clic en "Create Key"
5. Copia tu API key (comienza con `sk-or-v1-`)
6. Agrega $5 USD de crédito (te durará meses)

### Paso 2: Configurar el Chatbot (30 segundos)

1. Abre `index.html` en tu navegador
2. Pega tu API key en el panel que aparece
3. Haz clic en "Guardar"

### Paso 3: ¡Listo! (30 segundos)

Escribe tu primer mensaje:
```
Hola, ¿cómo puedes ayudarme?
```

---

## 📁 Archivos Incluidos

```
BOT-UVG/
├── index.html              ⭐ Versión básica (EMPIEZA AQUÍ)
├── index-advanced.html     🚀 Versión con múltiples conversaciones
├── guia.html              📖 Guía completa de usuario
├── config.js              ⚙️ Configuración avanzada
├── models.js              🤖 Catálogo de modelos de IA
├── utils.js               🛠️ Funciones auxiliares
├── styles.css             🎨 Estilos adicionales
├── README.md              📚 Documentación general
├── TECHNICAL.md           🔧 Documentación técnica
├── QUICKSTART.md          ⚡ Esta guía
└── package.json           📦 Configuración npm
```

---

## 🎯 ¿Qué Versión Usar?

### `index.html` - Versión Básica ⭐
**Usa esta si:**
- Es tu primera vez
- Quieres algo simple
- Solo necesitas una conversación

**Características:**
- ✅ Interfaz limpia y simple
- ✅ Una conversación a la vez
- ✅ Fácil de usar
- ✅ Perfecto para empezar

### `index-advanced.html` - Versión Avanzada 🚀
**Usa esta si:**
- Quieres múltiples conversaciones
- Necesitas estadísticas
- Quieres exportar conversaciones

**Características:**
- ✅ Múltiples conversaciones simultáneas
- ✅ Sidebar con historial
- ✅ Estadísticas de uso
- ✅ Exportar a archivo de texto
- ✅ Más opciones de personalización

---

## 💬 Ejemplos de Uso

### Para Estudiantes

**Ayuda con Tareas:**
```
Necesito ayuda para entender el concepto de recursividad en programación
```

**Motivación:**
```
Estoy estresado con los exámenes finales, ¿algún consejo?
```

**Explicaciones:**
```
¿Puedes explicarme la diferencia entre una lista y una tupla en Python?
```

### Para Profesores

**Generar Ideas:**
```
Dame ideas para un proyecto de programación para estudiantes de segundo año
```

**Explicaciones Didácticas:**
```
¿Cómo puedo explicar el concepto de herencia en POO de forma simple?
```

### Para Investigación

**Búsqueda de Información:**
```
¿Qué es el aprendizaje automático y cuáles son sus aplicaciones?
```

**Análisis:**
```
Explícame las ventajas y desventajas de usar microservicios
```

---

## 🎨 Personalización Rápida

### Cambiar el Modelo de IA

Abre `index.html` y busca (línea ~280):

```javascript
model: 'anthropic/claude-3.5-sonnet',
```

Cámbialo por:

**Más económico:**
```javascript
model: 'openai/gpt-3.5-turbo',  // ~$0.50 por millón de tokens
```

**Más potente:**
```javascript
model: 'anthropic/claude-3-opus',  // Máxima capacidad
```

**Balance:**
```javascript
model: 'google/gemini-pro',  // Buena relación calidad/precio
```

### Cambiar los Colores

Busca en `index.html` la sección `<style>` y modifica:

```css
/* Color principal */
background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);

/* Cambia a verde */
background: linear-gradient(135deg, #065f46 0%, #10b981 100%);

/* Cambia a morado */
background: linear-gradient(135deg, #6b21a8 0%, #a855f7 100%);

/* Cambia a rojo */
background: linear-gradient(135deg, #991b1b 0%, #ef4444 100%);
```

### Modificar la Personalidad

Busca `SYSTEM_PROMPT` y edita el texto:

```javascript
const SYSTEM_PROMPT = `
Eres un asistente de la UVG.

// Agrega o modifica características:
- Eres más formal / informal
- Usas más / menos emojis
- Te especializas en [área específica]
- Respondes de forma más breve / detallada
`;
```

---

## 💰 Costos Reales

### Con $5 USD puedes tener:

**Usando Claude 3.5 Sonnet (recomendado):**
- ~150-200 conversaciones completas
- ~1000-1500 mensajes individuales
- Duración: 1-3 meses de uso normal

**Usando GPT-3.5 Turbo (económico):**
- ~500-1000 conversaciones completas
- ~5000-10000 mensajes individuales
- Duración: 3-6 meses de uso normal

**Costo por mensaje:**
- Mensaje corto: $0.001 - $0.003
- Mensaje medio: $0.003 - $0.008
- Mensaje largo: $0.008 - $0.020

---

## 🔧 Solución Rápida de Problemas

### ❌ "Invalid API Key"
**Solución:**
1. Verifica que copiaste la key completa
2. Debe empezar con `sk-or-v1-`
3. Verifica que tengas créditos en OpenRouter

### ❌ El chatbot no responde
**Solución:**
1. Abre la consola (F12)
2. Busca errores en rojo
3. Verifica tu conexión a internet
4. Recarga la página (Ctrl+R)

### ❌ Respuestas muy lentas
**Solución:**
1. Cambia a un modelo más rápido:
   ```javascript
   model: 'openai/gpt-3.5-turbo'
   ```
2. Reduce `max_tokens`:
   ```javascript
   max_tokens: 500
   ```

### ❌ Panel de configuración no aparece
**Solución:**
1. Abre la consola (F12)
2. Escribe: `localStorage.clear()`
3. Presiona Enter
4. Recarga la página

---

## 📱 Usar en Móvil

### Opción 1: Archivo Local
1. Copia los archivos a tu teléfono
2. Abre `index.html` con Chrome/Safari
3. Funciona sin internet (después de configurar)

### Opción 2: Servidor Local
1. Sube los archivos a GitHub Pages
2. Accede desde tu móvil
3. Guarda como acceso directo en pantalla de inicio

---

## 🚀 Próximos Pasos

### Nivel Básico ✅
- [x] Configurar API key
- [x] Enviar primer mensaje
- [x] Tener una conversación

### Nivel Intermedio 🎯
- [ ] Probar diferentes modelos
- [ ] Personalizar colores
- [ ] Exportar conversaciones
- [ ] Usar versión avanzada

### Nivel Avanzado 🚀
- [ ] Modificar la personalidad
- [ ] Agregar funciones personalizadas
- [ ] Integrar con otros servicios
- [ ] Desplegar en la web

---

## 📚 Recursos Adicionales

- **Guía Completa**: Abre `guia.html`
- **Documentación Técnica**: Lee `TECHNICAL.md`
- **OpenRouter Docs**: [openrouter.ai/docs](https://openrouter.ai/docs)
- **Precios**: [openrouter.ai/docs/pricing](https://openrouter.ai/docs/pricing)

---

## 💡 Tips Pro

1. **Ahorra dinero**: Usa GPT-3.5 Turbo para conversaciones simples
2. **Mejor calidad**: Usa Claude 3.5 Sonnet para conversaciones complejas
3. **Limpia el historial**: Borra conversaciones viejas para reducir costos
4. **Exporta importante**: Guarda conversaciones importantes antes de limpiar
5. **Prueba modelos**: Experimenta con diferentes modelos para encontrar tu favorito

---

## ❓ Preguntas Frecuentes

**¿Necesito internet?**
Sí, para comunicarte con la API de OpenRouter.

**¿Es seguro?**
Sí, tu API key se guarda solo en tu navegador.

**¿Puedo usarlo en producción?**
Sí, pero considera agregar autenticación de usuarios.

**¿Funciona offline?**
No, necesitas internet para que la IA responda.

**¿Cuánto cuesta realmente?**
Con $5 USD puedes usar el chatbot por 1-3 meses normalmente.

---

## 🎉 ¡Listo!

Ya tienes todo lo necesario para usar tu chatbot UVG.

**¿Dudas?** Revisa `guia.html` o `TECHNICAL.md`

**¡Disfruta tu asistente virtual! 🎓**

---

**Última actualización**: 2026-03-06
**Versión**: 1.0.0
