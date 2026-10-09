from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "127.0.0.1"
PORT = 8000


class LabHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            body = b"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kirby Security Lab</title>
</head>
<body>
    <h1>Kirby Security Lab</h1>
    <p>Authorized penetration-testing target.</p>
    <p>Environment: Localhost only.</p>
</body>
</html>
"""

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header(
                "Content-Security-Policy",
                "default-src 'self'; frame-ancestors 'none'"
            )
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("X-Frame-Options", "DENY")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        else:
            body = b"404 - Not Found"

            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("X-Frame-Options", "DENY")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    def log_message(self, format_string, *args):
        print(f"[HTTP] {self.address_string()} - {format_string % args}")


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), LabHandler)
    print(f"Lab server running at http://{HOST}:{PORT}")
    print("Safety restriction: listening on localhost only.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nLab server stopped.")
    finally:
        server.server_close()
