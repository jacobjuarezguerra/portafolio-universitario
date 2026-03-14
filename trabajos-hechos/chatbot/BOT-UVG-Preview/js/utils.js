// Utilidades para el Chatbot UVG

class ChatUtils {
    /**
     * Formatea la fecha y hora actual
     */
    static getCurrentTimestamp() {
        const now = new Date();
        return now.toLocaleTimeString('es-GT', {
            hour: '2-digit',
            minute: '2-digit'
        });
    }

    /**
     * Sanitiza el input del usuario para prevenir XSS
     */
    static sanitizeInput(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    /**
     * Formatea el texto con markdown básico
     */
    static formatMarkdown(text) {
        return text
            // Negrita
            .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
            // Cursiva
            .replace(/\*(.+?)\*/g, '<em>$1</em>')
            // Código inline
            .replace(/`(.+?)`/g, '<code>$1</code>')
            // Saltos de línea
            .replace(/\n/g, '<br>');
    }

    /**
     * Guarda el historial de conversación
     */
    static saveConversationHistory(history) {
        try {
            localStorage.setItem('uvg_chat_history', JSON.stringify(history));
        } catch (e) {
            console.error('Error guardando historial:', e);
        }
    }

    /**
     * Carga el historial de conversación
     */
    static loadConversationHistory() {
        try {
            const history = localStorage.getItem('uvg_chat_history');
            return history ? JSON.parse(history) : [];
        } catch (e) {
            console.error('Error cargando historial:', e);
            return [];
        }
    }

    /**
     * Limpia el historial de conversación
     */
    static clearConversationHistory() {
        localStorage.removeItem('uvg_chat_history');
    }

    /**
     * Exporta la conversación a un archivo de texto
     */
    static exportConversation(history) {
        const text = history.map(msg => {
            const role = msg.role === 'user' ? 'Estudiante' : 'Asistente UVG';
            return `[${role}]: ${msg.content}\n`;
        }).join('\n');

        const blob = new Blob([text], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `conversacion-uvg-${Date.now()}.txt`;
        a.click();
        URL.revokeObjectURL(url);
    }

    /**
     * Valida la API key de OpenRouter
     */
    static validateApiKey(key) {
        return key && key.startsWith('sk-or-v1-') && key.length > 20;
    }

    /**
     * Cuenta los tokens aproximados en un texto
     */
    static estimateTokens(text) {
        // Aproximación: 1 token ≈ 4 caracteres
        return Math.ceil(text.length / 4);
    }

    /**
     * Calcula el costo aproximado de una conversación
     */
    static estimateCost(history, pricePerMillionTokens = 3) {
        const totalTokens = history.reduce((sum, msg) => {
            return sum + this.estimateTokens(msg.content);
        }, 0);

        return (totalTokens / 1000000) * pricePerMillionTokens;
    }

    /**
     * Detecta si el mensaje contiene código
     */
    static containsCode(text) {
        return /```|`[^`]+`|function|class|const|let|var|import|export/.test(text);
    }

    /**
     * Genera un ID único para mensajes
     */
    static generateMessageId() {
        return `msg_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    }

    /**
     * Trunca el historial si es muy largo
     */
    static truncateHistory(history, maxMessages = 50) {
        if (history.length > maxMessages) {
            return history.slice(-maxMessages);
        }
        return history;
    }

    /**
     * Detecta el idioma del texto
     */
    static detectLanguage(text) {
        const spanishWords = ['el', 'la', 'de', 'que', 'y', 'a', 'en', 'un', 'ser', 'se'];
        const words = text.toLowerCase().split(/\s+/);
        const spanishCount = words.filter(w => spanishWords.includes(w)).length;
        return spanishCount > words.length * 0.1 ? 'es' : 'en';
    }

    /**
     * Formatea números grandes
     */
    static formatNumber(num) {
        if (num >= 1000000) {
            return (num / 1000000).toFixed(1) + 'M';
        }
        if (num >= 1000) {
            return (num / 1000).toFixed(1) + 'K';
        }
        return num.toString();
    }

    /**
     * Copia texto al portapapeles
     */
    static async copyToClipboard(text) {
        try {
            await navigator.clipboard.writeText(text);
            return true;
        } catch (e) {
            console.error('Error copiando al portapapeles:', e);
            return false;
        }
    }

    /**
     * Reproduce un sonido de notificación
     */
    static playNotificationSound() {
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();

        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);

        oscillator.frequency.value = 800;
        oscillator.type = 'sine';

        gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.1);

        oscillator.start(audioContext.currentTime);
        oscillator.stop(audioContext.currentTime + 0.1);
    }

    /**
     * Detecta si el usuario está en móvil
     */
    static isMobile() {
        return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    }

    /**
     * Obtiene estadísticas de la conversación
     */
    static getConversationStats(history) {
        const userMessages = history.filter(m => m.role === 'user').length;
        const assistantMessages = history.filter(m => m.role === 'assistant').length;
        const totalTokens = history.reduce((sum, m) => sum + this.estimateTokens(m.content), 0);

        return {
            userMessages,
            assistantMessages,
            totalMessages: history.length,
            totalTokens,
            estimatedCost: this.estimateCost(history)
        };
    }
}

// Exportar si se usa como módulo
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ChatUtils;
}
