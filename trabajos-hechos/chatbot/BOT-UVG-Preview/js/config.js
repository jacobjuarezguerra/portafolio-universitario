// Configuración del Chatbot UVG
// Puedes modificar estos valores según tus necesidades

const CONFIG = {
    // Configuración de OpenRouter
    openrouter: {
        apiUrl: 'https://openrouter.ai/api/v1/chat/completions',
        defaultModel: 'meta-llama/llama-3.3-70b-instruct:free',

        // Modelos alternativos disponibles
        availableModels: {
            'claude-3.5-sonnet': 'anthropic/claude-3.5-sonnet',
            'claude-3-opus': 'anthropic/claude-3-opus',
            'gpt-4-turbo': 'openai/gpt-4-turbo',
            'gpt-3.5-turbo': 'openai/gpt-3.5-turbo',
            'gemini-pro': 'google/gemini-pro',
            'llama-3-70b': 'meta-llama/llama-3-70b-instruct',
            'llama-3-3-70b-instruct': 'meta-llama/llama-3.3-70b-instruct:free',
            'mistral-7b-instruct': 'mistralai/mistral-7b-instruct:free',
            'mistral-small-3.1-24b-instruct': 'mistralai/mistral-small-3.1-24b-instruct:free',
            'gemma-3-12b-it': 'google/gemma-3-12b-it:free'
        }
    },

    // Parámetros del modelo
    modelParams: {
        temperature: 0.7,        // Creatividad (0.0 - 1.0)
        max_tokens: 1000,        // Longitud máxima de respuesta
        top_p: 1.0,              // Diversidad de respuestas
        frequency_penalty: 0.0,  // Penalización por repetición
        presence_penalty: 0.0    // Penalización por temas repetidos
    },

    // Configuración de la interfaz
    ui: {
        title: '🎓 Asistente UVG',
        subtitle: 'Tu compañero virtual en la Universidad del Valle de Guatemala',
        placeholderText: 'Escribe tu mensaje aquí...',
        sendButtonText: 'Enviar',

        // Colores (puedes usar colores hex o nombres CSS)
        colors: {
            primary: '#3b82f6',      // Azul UVG
            primaryDark: '#1e40af',
            secondary: '#2563eb',
            background: '#f8fafc',
            userMessage: '#3b82f6',
            assistantMessage: '#ffffff',
            error: '#dc2626'
        }
    },

    // Mensajes del sistema
    messages: {
        welcome: '¡Hola! 👋 Soy tu asistente virtual de la UVG. Estoy aquí para ayudarte con lo que necesites: dudas académicas, información sobre la universidad, o simplemente para conversar. ¿En qué puedo apoyarte hoy?',

        apiKeyRequired: 'Por favor configura tu API key primero',

        apiKeySaved: '¡Perfecto! Ya podemos empezar a conversar. ¿En qué puedo ayudarte?',

        errorPrefix: 'Error: ',
        errorSuffix: '. Por favor verifica tu API key o intenta de nuevo.'
    },

    // Personalidad del asistente
    personality: {
        name: 'Asistente UVG',

        systemPrompt: `Eres un asistente virtual de la Universidad del Valle de Guatemala (UVG), una de las universidades más prestigiosas de Guatemala y Centroamérica.

Tu personalidad:
- Eres respetuoso, carismático y cercano con los estudiantes
- Usas un tono amigable pero profesional
- Te apasiona ayudar a los estudiantes en su desarrollo académico
- Conoces la cultura universitaria guatemalteca
- Eres paciente y empático con las preocupaciones estudiantiles
- Ocasionalmente usas emojis para ser más expresivo (sin exagerar)

Tu rol:
- Ayudar con dudas académicas generales
- Brindar apoyo motivacional
- Orientar sobre temas universitarios
- Ser un compañero de conversación amigable
- Promover los valores de excelencia académica de la UVG

Importante:
- Si no sabes algo específico de la UVG, sé honesto y sugiere contactar a la universidad
- Mantén siempre un tono positivo y motivador
- Respeta la diversidad y la inclusión
- Responde en español de Guatemala (vos en lugar de tú cuando sea apropiado)`,

        // Contexto adicional sobre UVG (puedes expandir esto)
        context: {
            university: 'Universidad del Valle de Guatemala',
            location: 'Guatemala, Centroamérica',
            values: ['Excelencia académica', 'Innovación', 'Responsabilidad social', 'Integridad'],

            // Información general (actualiza según necesites)
            generalInfo: {
                founded: '1966',
                type: 'Universidad privada',
                campus: ['Campus Central', 'Campus Sur', 'Campus Altiplano'],
                strengths: ['Ingeniería', 'Ciencias', 'Negocios', 'Educación']
            }
        }
    },

    // Configuración de almacenamiento
    storage: {
        apiKeyName: 'openrouter_api_key',
        conversationHistoryName: 'uvg_chat_history',
        maxHistoryLength: 50  // Máximo de mensajes a guardar
    },

    // Características opcionales
    features: {
        saveConversationHistory: false,  // Guardar historial en localStorage
        showTypingIndicator: true,       // Mostrar indicador de "escribiendo..."
        enableKeyboardShortcuts: true,   // Atajos de teclado (Enter para enviar)
        autoScroll: true,                // Scroll automático a nuevos mensajes
        showTimestamps: false            // Mostrar hora de cada mensaje
    }
};

// Exportar configuración (si usas módulos ES6)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}
