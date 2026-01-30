#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8000
os.chdir('c:\\Users\\Alan\\Documents\\licenciasBA')

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"Servidor ejecutándose en http://localhost:{PORT}")
    print("Presiona Ctrl+C para detener")
    httpd.serve_forever()
