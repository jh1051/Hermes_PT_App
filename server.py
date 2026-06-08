#!/usr/bin/env python3
"""Dashboard data server. Serves the PT dashboard JSON."""
import http.server
import socketserver
import os

PORT = 8000
os.chdir("/root/dashboard")


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Disable caching so dashboard picks up edits immediately
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, format, *args):
        # Quieter logs
        pass


if __name__ == "__main__":
    with ReusableTCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Dashboard server on :{PORT}, cwd={os.getcwd()}")
        httpd.serve_forever()
