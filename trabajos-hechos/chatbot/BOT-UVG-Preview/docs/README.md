# 🎓 Chatbot UVG - Asistente Virtual

Chatbot conversacional para estudiantes de la Universidad del Valle de Guatemala (UVG) con inteligencia artificial.

## 🚀 Características

- **Personalidad Carismática**: Asistente respetuoso y cercano diseñado específicamente para estudiantes universitarios
- **Conversación Natural**: Usa Claude 3.5 Sonnet vía OpenRouter para respuestas inteligentes
- **Interfaz Moderna**: Diseño limpio y responsivo con los colores de UVG
- **Historial de Conversación**: Mantiene el contexto de la conversación
- **Fácil Configuración**: Solo necesitas una API key de OpenRouter

## 📋 Requisitos

- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- API Key de OpenRouter ([obtener aquí](https://openrouter.ai/keys))

## 🔧 Instalación

1. Descarga o clona este repositorio
2. Abre `index.html` en tu navegador
3. Ingresa tu API key de OpenRouter en el panel de configuración
4. ¡Comienza a conversar!

## 💡 Uso

### Configuración Inicial

1. Al abrir el chatbot por primera vez, verás un panel de configuración
2. Ingresa tu API key de OpenRouter (formato: `sk-or-v1-...`)
3. Haz clic en "Guardar"
4. La API key se guardará en tu navegador para futuras sesiones

### Conversación

- Escribe tu mensaje en el campo de texto
- Presiona Enter o haz clic en "Enviar"
- El asistente responderá de forma natural y contextual

### Ejemplos de Preguntas

- "¿Qué carreras ofrece la UVG?"
- "Ayúdame con mi proyecto de programación"
- "Necesito motivación para estudiar"
- "¿Cómo puedo mejorar mis hábitos de estudio?"

## 🎨 Personalización

### Cambiar el Modelo de IA

En `index.html`, línea ~280, puedes cambiar el modelo:

```javascript
model: 'anthropic/claude-3.5-sonnet', // Modelo actual
// Otras opciones:
// 'openai/gpt-4-turbo'
// 'google/gemini-pro'
// 'meta-llama/llama-3-70b-instruct'
```

### Modificar la Personalidad

Edita la variable `SYSTEM_PROMPT` en `index.html` (línea ~170) para ajustar:
- Tono de conversación
- Conocimientos específicos
- Estilo de respuesta

### Cambiar Colores

Modifica las variables CSS en la sección `<style>`:
- `background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)` - Fondo principal
- `.chat-header` - Colores del encabezado
- `.message.user .message-content` - Color de mensajes del usuario

## 🔒 Seguridad

- La API key se almacena localmente en tu navegador (localStorage)
- No se envía información a servidores externos excepto a OpenRouter
- Todas las conversaciones son privadas

## 💰 Costos

OpenRouter cobra por uso según el modelo:
- Claude 3.5 Sonnet: ~$3 por millón de tokens
- Conversaciones típicas: $0.01 - $0.05 por sesión

Consulta precios actualizados en [openrouter.ai/docs/pricing](https://openrouter.ai/docs/pricing)

## 🛠️ Solución de Problemas

### "Error en la respuesta del servidor"
- Verifica que tu API key sea válida
- Asegúrate de tener créditos en tu cuenta de OpenRouter

### El chatbot no responde
- Revisa la consola del navegador (F12) para ver errores
- Verifica tu conexión a internet

### Panel de configuración no aparece
- Borra el localStorage: `localStorage.clear()` en la consola
- Recarga la página

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

## 🤝 Contribuciones

¿Tienes ideas para mejorar el chatbot? ¡Las contribuciones son bienvenidas!

---

Desarrollado con ❤️ para la comunidad UVG
