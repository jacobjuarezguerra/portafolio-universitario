# Directorio de Datos

Este directorio está destinado para almacenar datos relacionados con el chatbot UVG.

## Uso Sugerido

- **Historial de conversaciones**: Exportar y guardar conversaciones importantes
- **Configuraciones personalizadas**: Backups de configuraciones de usuario
- **Logs**: Registros de uso y errores (si se implementa)
- **Datos de entrenamiento**: Ejemplos de conversaciones para mejorar el chatbot
- **Caché**: Datos temporales para mejorar el rendimiento

## Estructura Sugerida

```
data/
├── conversations/     # Historial de conversaciones exportadas
├── configs/          # Backups de configuraciones
├── logs/             # Logs de uso y errores
└── cache/            # Datos temporales en caché
```

## Nota de Privacidad

Este directorio está incluido en `.gitignore` para proteger la privacidad de los usuarios. Los datos almacenados aquí no se subirán al repositorio.
