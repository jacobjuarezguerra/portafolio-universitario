# 📚 Documentación Técnica - Chatbot UVG

## Arquitectura del Sistema

### Componentes Principales

```
BOT-UVG/
├── index.html              # Versión básica del chatbot
├── index-advanced.html     # Versión avanzada con sidebar y múltiples conversaciones
├── guia.html              # Guía de usuario completa
├── config.js              # Archivo de configuración
├── utils.js               # Utilidades y funciones helper
├── README.md              # Documentación general
└── package.json           # Configuración npm (opcional)
```

## Tecnologías Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **API**: OpenRouter API (https://openrouter.ai)
- **Modelo de IA**: Claude 3.5 Sonnet (Anthropic)
- **Almacenamiento**: LocalStorage del navegador

## Flujo de Datos

```
Usuario → Input → Validación → API Request → OpenRouter → Claude 3.5 Sonnet
                                                              ↓
Usuario ← UI Update ← Procesamiento ← API Response ← OpenRouter
```

## API de OpenRouter

### Endpoint
```
POST https://openrouter.ai/api/v1/chat/completions
```

### Headers Requeridos
```javascript
{
  'Authorization': 'Bearer sk-or-v1-...',
  'Content-Type': 'application/json',
  'HTTP-Referer': window.location.href,
  'X-Title': 'UVG Chat Assistant'
}
```

### Estructura del Request
```javascript
{
  "model": "anthropic/claude-3.5-sonnet",
  "messages": [
    {
      "role": "system",
      "content": "Prompt del sistema..."
    },
    {
      "role": "user",
      "content": "Mensaje del usuario"
    },
    {
      "role": "assistant",
      "content": "Respuesta del asistente"
    }
  ],
  "temperature": 0.7,
  "max_tokens": 1000
}
```

### Estructura del Response
```javascript
{
  "id": "gen-...",
  "model": "anthropic/claude-3.5-sonnet",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Respuesta generada..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 150,
    "completion_tokens": 200,
    "total_tokens": 350
  }
}
```

## Parámetros del Modelo

### Temperature (0.0 - 1.0)
- **0.0-0.3**: Respuestas muy consistentes y predecibles
- **0.4-0.7**: Balance entre creatividad y consistencia (recomendado)
- **0.8-1.0**: Respuestas más creativas y variadas

### Max Tokens
- Controla la longitud máxima de la respuesta
- 1 token ≈ 4 caracteres en español
- Recomendado: 500-1500 tokens

### Top P (0.0 - 1.0)
- Controla la diversidad de las respuestas
- Recomendado: 1.0 (por defecto)

## Almacenamiento Local

### LocalStorage Keys

```javascript
// API Key
localStorage.setItem('openrouter_api_key', 'sk-or-v1-...');

// Historial de conversación (versión básica)
localStorage.setItem('uvg_chat_history', JSON.stringify([...]));

// Conversaciones múltiples (versión avanzada)
localStorage.setItem('uvg_conversations', JSON.stringify({...}));
```

### Estructura de Conversación

```javascript
{
  "id": "conv_1234567890",
  "title": "Conversación sobre programación",
  "messages": [
    {
      "role": "user",
      "content": "¿Cómo funciona recursividad?",
      "timestamp": 1709683494894
    },
    {
      "role": "assistant",
      "content": "La recursividad es...",
      "timestamp": 1709683496123
    }
  ],
  "createdAt": 1709683494894
}
```

## Funciones Principales

### sendMessage()
Envía un mensaje a la API de OpenRouter y procesa la respuesta.

```javascript
async function sendMessage() {
  // 1. Validar input
  // 2. Mostrar mensaje del usuario
  // 3. Hacer request a OpenRouter
  // 4. Procesar respuesta
  // 5. Mostrar respuesta del asistente
  // 6. Actualizar historial
}
```

### showMessage(role, content, timestamp)
Renderiza un mensaje en la interfaz.

```javascript
function showMessage(role, content, timestamp) {
  // role: 'user' | 'assistant'
  // content: string (texto del mensaje)
  // timestamp: number (milisegundos desde epoch)
}
```

### saveApiKey()
Guarda la API key en localStorage.

```javascript
function saveApiKey() {
  const key = document.getElementById('apiKeyInput').value.trim();
  if (validateApiKey(key)) {
    localStorage.setItem('openrouter_api_key', key);
  }
}
```

## Utilidades (utils.js)

### ChatUtils.sanitizeInput(text)
Previene ataques XSS sanitizando el input del usuario.

```javascript
ChatUtils.sanitizeInput('<script>alert("xss")</script>');
// Output: "&lt;script&gt;alert("xss")&lt;/script&gt;"
```

### ChatUtils.formatMarkdown(text)
Convierte markdown básico a HTML.

```javascript
ChatUtils.formatMarkdown('**Hola** mundo');
// Output: "<strong>Hola</strong> mundo"
```

### ChatUtils.estimateTokens(text)
Estima el número de tokens en un texto.

```javascript
ChatUtils.estimateTokens('Hola mundo');
// Output: ~3 tokens
```

### ChatUtils.estimateCost(history, pricePerMillionTokens)
Calcula el costo aproximado de una conversación.

```javascript
ChatUtils.estimateCost(conversationHistory, 3);
// Output: 0.0045 (USD)
```

## Personalización del System Prompt

El system prompt define la personalidad y comportamiento del asistente:

```javascript
const SYSTEM_PROMPT = `
Eres un asistente virtual de la Universidad del Valle de Guatemala (UVG).

Tu personalidad:
- Respetuoso y carismático
- Tono amigable pero profesional
- Empático con estudiantes

Tu rol:
- Ayudar con dudas académicas
- Brindar apoyo motivacional
- Orientar sobre temas universitarios

Importante:
- Responde en español de Guatemala
- Usa "vos" en lugar de "tú"
- Mantén un tono positivo
`;
```

## Modelos Disponibles

### Claude 3.5 Sonnet (Recomendado)
```javascript
model: 'anthropic/claude-3.5-sonnet'
```
- Mejor balance calidad/precio
- Excelente comprensión del contexto
- Respuestas naturales y coherentes

### GPT-4 Turbo
```javascript
model: 'openai/gpt-4-turbo'
```
- Máxima capacidad
- Más costoso
- Ideal para tareas complejas

### GPT-3.5 Turbo
```javascript
model: 'openai/gpt-3.5-turbo'
```
- Más económico
- Respuestas rápidas
- Bueno para conversaciones simples

### Gemini Pro
```javascript
model: 'google/gemini-pro'
```
- Balance precio/calidad
- Buena comprensión multilingüe

## Manejo de Errores

### Error: Invalid API Key
```javascript
if (!response.ok) {
  const errorData = await response.json();
  if (errorData.error?.code === 'invalid_api_key') {
    showError('API Key inválida. Verifica tu configuración.');
  }
}
```

### Error: Insufficient Credits
```javascript
if (errorData.error?.code === 'insufficient_credits') {
  showError('Créditos insuficientes. Recarga tu cuenta en OpenRouter.');
}
```

### Error: Rate Limit
```javascript
if (response.status === 429) {
  showError('Demasiadas solicitudes. Espera un momento e intenta de nuevo.');
}
```

## Optimizaciones

### 1. Truncar Historial
Limita el historial para reducir costos:

```javascript
function truncateHistory(history, maxMessages = 20) {
  if (history.length > maxMessages) {
    return history.slice(-maxMessages);
  }
  return history;
}
```

### 2. Debounce en Input
Evita llamadas innecesarias:

```javascript
let typingTimer;
input.addEventListener('input', () => {
  clearTimeout(typingTimer);
  typingTimer = setTimeout(() => {
    // Acción después de que el usuario deja de escribir
  }, 500);
});
```

### 3. Caché de Respuestas
Guarda respuestas comunes:

```javascript
const responseCache = new Map();

function getCachedResponse(message) {
  const normalized = message.toLowerCase().trim();
  return responseCache.get(normalized);
}
```

## Seguridad

### 1. Validación de API Key
```javascript
function validateApiKey(key) {
  return key &&
         key.startsWith('sk-or-v1-') &&
         key.length > 20;
}
```

### 2. Sanitización de Input
```javascript
function sanitizeInput(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}
```

### 3. Rate Limiting Local
```javascript
let lastRequestTime = 0;
const MIN_REQUEST_INTERVAL = 1000; // 1 segundo

function canMakeRequest() {
  const now = Date.now();
  if (now - lastRequestTime < MIN_REQUEST_INTERVAL) {
    return false;
  }
  lastRequestTime = now;
  return true;
}
```

## Testing

### Test Manual Básico

1. **Test de Conexión**
   - Abrir index.html
   - Verificar que carga correctamente
   - Verificar que aparece el panel de configuración

2. **Test de API Key**
   - Ingresar API key válida
   - Verificar que se guarda en localStorage
   - Verificar que el panel se cierra

3. **Test de Mensajes**
   - Enviar mensaje simple: "Hola"
   - Verificar respuesta del asistente
   - Verificar que el historial se actualiza

4. **Test de Errores**
   - Probar con API key inválida
   - Verificar mensaje de error
   - Probar sin conexión a internet

### Test de Rendimiento

```javascript
// Medir tiempo de respuesta
const startTime = performance.now();
await sendMessage();
const endTime = performance.now();
console.log(`Tiempo de respuesta: ${endTime - startTime}ms`);
```

## Deployment

### Opción 1: Archivo Local
Simplemente abre `index.html` en tu navegador.

### Opción 2: Servidor Local
```bash
# Con Python
python -m http.server 8080

# Con Node.js
npx http-server -p 8080

# Con live-server
npx live-server --port=8080
```

### Opción 3: GitHub Pages
1. Sube los archivos a un repositorio de GitHub
2. Ve a Settings → Pages
3. Selecciona la rama main
4. Tu chatbot estará en: `https://username.github.io/repo-name`

### Opción 4: Netlify/Vercel
1. Arrastra la carpeta a Netlify Drop
2. Tu chatbot estará online en segundos

## Costos Estimados

### Por Conversación
- Conversación corta (5 mensajes): ~$0.01 USD
- Conversación media (20 mensajes): ~$0.03 USD
- Conversación larga (50 mensajes): ~$0.08 USD

### Por Mes (uso moderado)
- 10 conversaciones/día: ~$3-5 USD/mes
- 50 conversaciones/día: ~$15-25 USD/mes
- 100 conversaciones/día: ~$30-50 USD/mes

## Troubleshooting

### Problema: No aparece el panel de configuración
**Solución**: Borra el localStorage
```javascript
localStorage.clear();
location.reload();
```

### Problema: Respuestas muy lentas
**Solución**: Cambia a un modelo más rápido
```javascript
model: 'openai/gpt-3.5-turbo'
```

### Problema: Costos muy altos
**Solución**: Reduce max_tokens y trunca el historial
```javascript
max_tokens: 500,
history: truncateHistory(history, 10)
```

## Recursos Adicionales

- **OpenRouter Docs**: https://openrouter.ai/docs
- **Claude API Docs**: https://docs.anthropic.com
- **Pricing**: https://openrouter.ai/docs/pricing
- **Models**: https://openrouter.ai/docs/models

## Licencia

MIT License - Libre para uso educativo y comercial.

---

**Última actualización**: 2026-03-06
**Versión**: 1.0.0
