const http = require('http');
const httpProxy = require('http-proxy');
const { spawn } = require('child_process');

// Start Django server
const django = spawn('.venv/bin/python', ['manage.py', 'runserver', '127.0.0.1:8000'], {
  env: { ...process.env, DJANGO_SETTINGS_MODULE: 'constructor_telegram_bots.settings_dev' },
  stdio: ['ignore', 'pipe', 'pipe']
});

django.stdout.on('data', (data) => console.log(`[Django] ${data}`));
django.stderr.on('data', (data) => console.log(`[Django] ${data}`));

// Wait for Django to start
setTimeout(() => {
  // Create proxy server
  const proxy = httpProxy.createProxyServer({ target: 'http://127.0.0.1:8000' });

  const server = http.createServer((req, res) => {
    proxy.web(req, res, {}, (err) => {
      console.error('Proxy error:', err);
      res.writeHead(502);
      res.end('Bad Gateway');
    });
  });

  server.listen(3000, () => {
    console.log('Proxy server running on http://localhost:3000');
  });
}, 3000);

process.on('SIGTERM', () => {
  django.kill();
  process.exit(0);
});
