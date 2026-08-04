from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
import json

from try_pandas import get_ages_table


ROOT = Path(__file__).parent
STATIC_DIR = ROOT / "static"


class AppHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/api/data":
            self.handle_api()
            return

        if parsed.path == "/":
            self.path = "/index.html"
        super().do_GET()

    def handle_api(self):
        try:
            payload = get_ages_table()
            self.send_json(payload, 200)
        except (ValueError, OSError) as error:
            self.send_json({"error": str(error)}, 400)

    def send_json(self, payload: dict, status: int):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    address = ("127.0.0.1", 8000)
    print("Pandas Playground running at http://127.0.0.1:8000")
    ThreadingHTTPServer(address, AppHandler).serve_forever()
