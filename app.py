import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body, tipe = json.dumps({"status": "ok"}), "application/json"
        elif self.path == "/":
            body, tipe = "Halo dari Autore", "text/plain; charset=utf-8"
        else:
            self.send_error(404)
            return
        data = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", tipe)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    print("Listening on 0.0.0.0:8000", flush=True)
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
