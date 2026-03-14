// Configuración de modelos disponibles en OpenRouter
const MODELS = {
    // Anthropic Claude
    claude: {
        'claude-3.5-sonnet': {
            id: 'anthropic/claude-3.5-sonnet',
            name: 'Claude 3.5 Sonnet',
            provider: 'Anthropic',
            contextWindow: 200000,
            maxOutput: 4096,
            pricing: {
                prompt: 3.00,  // por millón de tokens
                completion: 15.00
            },
            description: 'Mejor balance calidad/precio. Excelente para conversaciones complejas.',
            recommended: true
        },
        'claude-3-opus': {
            id: 'anthropic/claude-3-opus',
            name: 'Claude 3 Opus',
            provider: 'Anthropic',
            contextWindow: 200000,
            maxOutput: 4096,
            pricing: {
                prompt: 15.00,
                completion: 75.00
            },
            description: 'Máxima capacidad y precisión. Ideal para tareas muy complejas.'
        },
        'claude-3-haiku': {
            id: 'anthropic/claude-3-haiku',
            name: 'Claude 3 Haiku',
            provider: 'Anthropic',
            contextWindow: 200000,
            maxOutput: 4096,
            pricing: {
                prompt: 0.25,
                completion: 1.25
            },
            description: 'Más rápido y económico. Bueno para conversaciones simples.'
        }
    },

    // OpenAI GPT
    openai: {
        'gpt-4-turbo': {
            id: 'openai/gpt-4-turbo',
            name: 'GPT-4 Turbo',
            provider: 'OpenAI',
            contextWindow: 128000,
            maxOutput: 4096,
            pricing: {
                prompt: 10.00,
                completion: 30.00
            },
            description: 'Modelo avanzado de OpenAI con gran contexto.'
        },
        'gpt-4': {
            id: 'openai/gpt-4',
            name: 'GPT-4',
            provider: 'OpenAI',
            contextWindow: 8192,
            maxOutput: 4096,
            pricing: {
                prompt: 30.00,
                completion: 60.00
            },
            description: 'Modelo original GPT-4. Muy capaz pero costoso.'
        },
        'gpt-3.5-turbo': {
            id: 'openai/gpt-3.5-turbo',
            name: 'GPT-3.5 Turbo',
            provider: 'OpenAI',
            contextWindow: 16385,
            maxOutput: 4096,
            pricing: {
                prompt: 0.50,
                completion: 1.50
            },
            description: 'Económico y rápido. Bueno para conversaciones generales.'
        }
    },

    // Google Gemini
    google: {
        'gemini-pro': {
            id: 'google/gemini-pro',
            name: 'Gemini Pro',
            provider: 'Google',
            contextWindow: 32768,
            maxOutput: 2048,
            pricing: {
                prompt: 0.50,
                completion: 1.50
            },
            description: 'Balance precio/calidad de Google. Buena comprensión multilingüe.'
        },
        'gemini-pro-1.5': {
            id: 'google/gemini-pro-1.5',
            name: 'Gemini Pro 1.5',
            provider: 'Google',
            contextWindow: 1000000,
            maxOutput: 8192,
            pricing: {
                prompt: 2.50,
                completion: 10.00
            },
            description: 'Contexto masivo. Ideal para documentos largos.'
        }
    },

    // Meta Llama
    meta: {
        'llama-3-70b': {
            id: 'meta-llama/llama-3-70b-instruct',
            name: 'Llama 3 70B',
            provider: 'Meta',
            contextWindow: 8192,
            maxOutput: 2048,
            pricing: {
                prompt: 0.70,
                completion: 0.80
            },
            description: 'Modelo open source de Meta. Buena relación calidad/precio.'
        },
        'llama-3-8b': {
            id: 'meta-llama/llama-3-8b-instruct',
            name: 'Llama 3 8B',
            provider: 'Meta',
            contextWindow: 8192,
            maxOutput: 2048,
            pricing: {
                prompt: 0.10,
                completion: 0.10
            },
            description: 'Muy económico. Bueno para tareas simples.'
        }
    },

    // Mistral AI
    mistral: {
        'mistral-large': {
            id: 'mistralai/mistral-large',
            name: 'Mistral Large',
            provider: 'Mistral AI',
            contextWindow: 32768,
            maxOutput: 4096,
            pricing: {
                prompt: 8.00,
                completion: 24.00
            },
            description: 'Modelo europeo de alta capacidad.'
        },
        'mistral-medium': {
            id: 'mistralai/mistral-medium',
            name: 'Mistral Medium',
            provider: 'Mistral AI',
            contextWindow: 32768,
            maxOutput: 4096,
            pricing: {
                prompt: 2.70,
                completion: 8.10
            },
            description: 'Balance entre capacidad y costo.'
        }
    }
};

// Función para obtener todos los modelos
function getAllModels() {
    const allModels = [];
    for (const provider in MODELS) {
        for (const model in MODELS[provider]) {
            allModels.push(MODELS[provider][model]);
        }
    }
    return allModels;
}

// Función para obtener modelo recomendado
function getRecommendedModel() {
    return MODELS.claude['claude-3.5-sonnet'];
}

// Función para obtener modelos por proveedor
function getModelsByProvider(provider) {
    return MODELS[provider] || {};
}

// Función para calcular costo estimado
function calculateCost(promptTokens, completionTokens, modelId) {
    const allModels = getAllModels();
    const model = allModels.find(m => m.id === modelId);

    if (!model) return 0;

    const promptCost = (promptTokens / 1000000) * model.pricing.prompt;
    const completionCost = (completionTokens / 1000000) * model.pricing.completion;

    return promptCost + completionCost;
}

// Función para obtener modelos económicos
function getEconomicModels() {
    const allModels = getAllModels();
    return allModels
        .filter(m => m.pricing.prompt < 1.0)
        .sort((a, b) => a.pricing.prompt - b.pricing.prompt);
}

// Función para obtener modelos premium
function getPremiumModels() {
    const allModels = getAllModels();
    return allModels
        .filter(m => m.pricing.prompt >= 10.0)
        .sort((a, b) => b.pricing.prompt - a.pricing.prompt);
}

// Exportar
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        MODELS,
        getAllModels,
        getRecommendedModel,
        getModelsByProvider,
        calculateCost,
        getEconomicModels,
        getPremiumModels
    };
}
