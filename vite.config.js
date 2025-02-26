import { defineConfig } from 'vite'


export default defineConfig({
    server: {
        // open: '/docs/index.html',
        port: 3001,
        proxy: {
            '/res': {
              target: 'http://localhost:3002', // URL Bottle server
              changeOrigin: true,
              // rewrite: (path) => path.replace(/^\/api/, '')
            },
        },
    },
})