from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
import json
import subprocess
import sys
import time

from try_pandas import get_ages_table


ROOT = Path(__file__).parent
STATIC_DIR = ROOT / "static"
PANDAS_FILE = ROOT / "try_pandas.py"


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


def run_server():
    address = ("127.0.0.1", 8000)
    print("Pandas Playground running at http://127.0.0.1:8000")
    ThreadingHTTPServer(address, AppHandler).serve_forever()


def run_with_reload():
    last_modified = PANDAS_FILE.stat().st_mtime_ns
    server = subprocess.Popen([sys.executable, __file__, "--serve"])
    print(f"Watching {PANDAS_FILE.name} for changes...")

    try:
        while True:
            time.sleep(0.5)
            modified = PANDAS_FILE.stat().st_mtime_ns
            if modified == last_modified:
                continue

            last_modified = modified
            print(f"Change detected in {PANDAS_FILE.name}; restarting server...")
            server.terminate()
            server.wait()
            server = subprocess.Popen([sys.executable, __file__, "--serve"])
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        server.terminate()
        server.wait()


if __name__ == "__main__":
    if "--serve" in sys.argv:
        run_server()
    else:
        run_with_reload()
