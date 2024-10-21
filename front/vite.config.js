import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  preview: {
    port: 80,
    strictPort: true,
  },
  server: {
    port: 80,
    strictPort: true,
    host: true,
    origin: "http://0.0.0.0:80",
  },
  optimizeDeps: {
    include: ["esm-dep > cjs-dep"],
  },
  build: {
    rollupOptions: {
      external: [
        '@opentelemetry/instrumentation-xml-http-request'
      ]
    }
  }
})
