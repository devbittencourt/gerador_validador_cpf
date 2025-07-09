import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000

class CPFHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        conn = sqlite3.connect("cpfs.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, cpf FROM cpfs_encontrados ORDER BY id DESC")
        rows = cursor.fetchall()
        conn.close()

        conteudo = "CPFs encontrados:\n\n"
        for row in rows:
            conteudo += f"{row[0]} - {row[1]}\n"

        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(conteudo.encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), CPFHandler)
    print(f"Servidor iniciado em http://localhost:{PORT}")
    server.serve_forever()
