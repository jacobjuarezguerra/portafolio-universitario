# 🌐 Guía de Despliegue - Chatbot UVG

Opciones para poner tu chatbot en línea y accesible desde cualquier lugar.

---

## 📋 Tabla de Contenidos

1. [GitHub Pages (Gratis)](#github-pages)
2. [Netlify (Gratis)](#netlify)
3. [Vercel (Gratis)](#vercel)
4. [Servidor Propio](#servidor-propio)
5. [Consideraciones de Seguridad](#seguridad)

---

## 🚀 Opción 1: GitHub Pages (Recomendado)

### ✅ Ventajas
- Completamente gratis
- Fácil de configurar
- Actualizaciones automáticas con git push
- SSL/HTTPS incluido
- Dominio personalizado opcional

### 📝 Pasos

#### 1. Crear Repositorio en GitHub

```bash
# Inicializar git en tu carpeta
cd "C:\Users\Nahataen\Desktop\BOT-UVG"
git init

# Agregar archivos
git add .

# Primer commit
git commit -m "Initial commit: Chatbot UVG v1.0"
```

#### 2. Subir a GitHub

```bash
# Crear repositorio en github.com (nombre: chatbot-uvg)
# Luego conectar y subir:

git remote add origin https://github.com/TU-USUARIO/chatbot-uvg.git
git branch -M main
git push -u origin main
```

#### 3. Activar GitHub Pages

1. Ve a tu repositorio en GitHub
2. Click en **Settings**
3. Scroll hasta **Pages** (menú lateral)
4. En **Source**, selecciona **main** branch
5. Click en **Save**

#### 4. Acceder a tu Chatbot

Tu chatbot estará disponible en:
```
https://TU-USUARIO.github.io/chatbot-uvg/start.html
```

### 🎯 Dominio Personalizado (Opcional)

1. Compra un dominio (ej: chatbot-uvg.com)
2. En GitHub Pages settings, agrega tu dominio
3. Configura DNS en tu proveedor:
   ```
   Type: CNAME
   Name: www
   Value: TU-USUARIO.github.io
   ```

---

## 🚀 Opción 2: Netlify

### ✅ Ventajas
- Gratis para proyectos pequeños
- Deploy en segundos
- SSL automático
- Formularios y funciones serverless
- Dominio personalizado gratis

### 📝 Pasos

#### Método 1: Drag & Drop (Más Fácil)

1. Ve a [netlify.com](https://netlify.com)
2. Crea una cuenta gratuita
3. Click en **Add new site** → **Deploy manually**
4. Arrastra la carpeta `BOT-UVG` a la zona de drop
5. ¡Listo! Tu sitio estará en línea en segundos

Tu URL será algo como: `https://random-name-123.netlify.app`

#### Método 2: Con Git (Recomendado)

1. Sube tu código a GitHub (ver pasos arriba)
2. En Netlify, click **Add new site** → **Import from Git**
3. Conecta tu repositorio de GitHub
4. Click en **Deploy site**

### 🎨 Configuración Adicional

Crea un archivo `netlify.toml` en la raíz:

```toml
[build]
  publish = "."

[[redirects]]
  from = "/*"
  to = "/start.html"
  status = 200
```

---

## 🚀 Opción 3: Vercel

### ✅ Ventajas
- Gratis para proyectos personales
- Deploy ultra rápido
- SSL automático
- Edge functions
- Analytics incluido

### 📝 Pasos

1. Ve a [vercel.com](https://vercel.com)
2. Crea una cuenta con GitHub
3. Click en **Add New** → **Project**
4. Importa tu repositorio de GitHub
5. Click en **Deploy**

Tu URL será: `https://chatbot-uvg.vercel.app`

### 🎨 Configuración

Crea `vercel.json` en la raíz:

```json
{
  "rewrites": [
    { "source": "/", "destination": "/start.html" }
  ]
}
```

---

## 🚀 Opción 4: Servidor Propio

### Para VPS o Servidor Dedicado

#### Con Nginx

1. **Instalar Nginx**
```bash
sudo apt update
sudo apt install nginx
```

2. **Copiar archivos**
```bash
sudo mkdir -p /var/www/chatbot-uvg
sudo cp -r * /var/www/chatbot-uvg/
```

3. **Configurar Nginx**
```bash
sudo nano /etc/nginx/sites-available/chatbot-uvg
```

Contenido:
```nginx
server {
    listen 80;
    server_name tu-dominio.com;
    root /var/www/chatbot-uvg;
    index start.html;

    location / {
        try_files $uri $uri/ /start.html;
    }

    # Caché para archivos estáticos
    location ~* \.(js|css|png|jpg|jpeg|gif|ico)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

4. **Activar sitio**
```bash
sudo ln -s /etc/nginx/sites-available/chatbot-uvg /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

5. **SSL con Let's Encrypt**
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d tu-dominio.com
```

#### Con Apache

1. **Instalar Apache**
```bash
sudo apt update
sudo apt install apache2
```

2. **Copiar archivos**
```bash
sudo mkdir -p /var/www/chatbot-uvg
sudo cp -r * /var/www/chatbot-uvg/
```

3. **Configurar Apache**
```bash
sudo nano /etc/apache2/sites-available/chatbot-uvg.conf
```

Contenido:
```apache
<VirtualHost *:80>
    ServerName tu-dominio.com
    DocumentRoot /var/www/chatbot-uvg

    <Directory /var/www/chatbot-uvg>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/chatbot-error.log
    CustomLog ${APACHE_LOG_DIR}/chatbot-access.log combined
</VirtualHost>
```

4. **Activar sitio**
```bash
sudo a2ensite chatbot-uvg
sudo systemctl restart apache2
```

---

## 🔒 Consideraciones de Seguridad

### ⚠️ IMPORTANTE: API Keys

**NUNCA** subas tu API key al repositorio público.

#### Solución 1: Variables de Entorno (Recomendado)

Crea un archivo `.env.example`:
```
OPENROUTER_API_KEY=tu_api_key_aqui
```

Agrega `.env` a `.gitignore`:
```
.env
.env.local
```

#### Solución 2: Backend Proxy

Crea un backend simple que maneje las API keys:

**backend.js** (Node.js):
```javascript
const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

app.post('/api/chat', async (req, res) => {
  const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.OPENROUTER_API_KEY}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(req.body)
  });

  const data = await response.json();
  res.json(data);
});

app.listen(3000);
```

Despliega en:
- Heroku (gratis)
- Railway (gratis)
- Render (gratis)

#### Solución 3: Autenticación de Usuarios

Implementa login para que solo usuarios autorizados usen el chatbot:

```javascript
// Ejemplo simple con Firebase Auth
import { initializeApp } from 'firebase/app';
import { getAuth, signInWithEmailAndPassword } from 'firebase/auth';

const auth = getAuth();

async function login(email, password) {
  try {
    await signInWithEmailAndPassword(auth, email, password);
    // Usuario autenticado, permitir acceso al chatbot
  } catch (error) {
    console.error('Error de autenticación:', error);
  }
}
```

---

## 📊 Monitoreo y Analytics

### Google Analytics

Agrega a tu `index.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Plausible Analytics (Alternativa privada)

```html
<script defer data-domain="tu-dominio.com" src="https://plausible.io/js/script.js"></script>
```

---

## 🚀 Optimizaciones para Producción

### 1. Minificar Archivos

```bash
# Instalar herramientas
npm install -g html-minifier uglify-js clean-css-cli

# Minificar HTML
html-minifier --collapse-whitespace --remove-comments index.html -o index.min.html

# Minificar JS
uglifyjs utils.js -c -m -o utils.min.js

# Minificar CSS
cleancss styles.css -o styles.min.css
```

### 2. Comprimir Imágenes

Si agregas imágenes, usa:
- [TinyPNG](https://tinypng.com)
- [Squoosh](https://squoosh.app)

### 3. CDN

Usa un CDN para archivos estáticos:
- Cloudflare (gratis)
- jsDelivr (gratis)

### 4. Service Worker (PWA)

Crea `sw.js`:

```javascript
const CACHE_NAME = 'chatbot-uvg-v1';
const urlsToCache = [
  '/',
  '/start.html',
  '/index.html',
  '/utils.js',
  '/styles.css'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
```

Registra en tu HTML:

```javascript
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}
```

---

## 📱 Hacer PWA (Progressive Web App)

Crea `manifest.json`:

```json
{
  "name": "Chatbot UVG",
  "short_name": "UVG Chat",
  "description": "Asistente Virtual de la Universidad del Valle de Guatemala",
  "start_url": "/start.html",
  "display": "standalone",
  "background_color": "#1e3a8a",
  "theme_color": "#3b82f6",
  "icons": [
    {
      "src": "/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ]
}
```

Agrega a tu HTML:

```html
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#3b82f6">
```

---

## 🎯 Checklist de Despliegue

### Antes de Desplegar

- [ ] Probar localmente en diferentes navegadores
- [ ] Verificar que no hay API keys en el código
- [ ] Minificar archivos (opcional)
- [ ] Optimizar imágenes (si las hay)
- [ ] Configurar .gitignore correctamente
- [ ] Actualizar URLs en la documentación

### Durante el Despliegue

- [ ] Elegir plataforma (GitHub Pages, Netlify, Vercel)
- [ ] Configurar dominio personalizado (opcional)
- [ ] Activar SSL/HTTPS
- [ ] Configurar redirects si es necesario
- [ ] Probar en producción

### Después del Despliegue

- [ ] Verificar que todo funciona
- [ ] Configurar analytics (opcional)
- [ ] Configurar monitoreo de errores
- [ ] Documentar la URL de producción
- [ ] Compartir con usuarios

---

## 🆘 Solución de Problemas

### Error: "API key not working in production"

**Causa**: La API key está hardcodeada y expuesta.

**Solución**: Implementa un backend proxy o usa variables de entorno.

### Error: "CORS blocked"

**Causa**: Restricciones de CORS del navegador.

**Solución**:
- Usa un backend proxy
- Configura headers CORS en tu servidor
- OpenRouter ya permite CORS, verifica tu configuración

### Error: "Site not loading"

**Causa**: Configuración incorrecta de rutas.

**Solución**:
- Verifica que `start.html` o `index.html` esté en la raíz
- Configura redirects correctamente
- Revisa logs del servidor

---

## 📚 Recursos Adicionales

### Plataformas de Hosting Gratis
- [GitHub Pages](https://pages.github.com)
- [Netlify](https://netlify.com)
- [Vercel](https://vercel.com)
- [Cloudflare Pages](https://pages.cloudflare.com)
- [Render](https://render.com)

### Dominios Gratis
- [Freenom](https://freenom.com) - .tk, .ml, .ga
- [GitHub Pages](https://pages.github.com) - username.github.io

### SSL Gratis
- [Let's Encrypt](https://letsencrypt.org)
- Incluido en Netlify/Vercel/GitHub Pages

---

## 🎉 ¡Listo para Producción!

Tu chatbot está listo para ser desplegado. Elige la opción que mejor se adapte a tus necesidades:

- **Más fácil**: Netlify Drag & Drop
- **Más control**: GitHub Pages
- **Más rápido**: Vercel
- **Más flexible**: Servidor propio

---

**¡Éxito con tu despliegue! 🚀**

---

*Última actualización: 2026-03-06*
*Versión: 1.0.0*
