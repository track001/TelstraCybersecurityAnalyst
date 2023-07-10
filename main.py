"""
Task: Develop a firewall rule to mitigate the ongoing malware attack on the Spring Framework.

Solution:
- Create a custom firewall server that blocks incoming requests to the specific path "/tomcatwar.jsp".
- All other requests will be handled as usual.
"""

import http.server
import socketserver

class FirewallRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/tomcatwar.jsp":
            self.send_response(403)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Access Denied")
        else:
            super().do_GET()

def run_firewall_server():
    handler = FirewallRequestHandler
    with socketserver.TCPServer(("localhost", 8000), handler) as httpd:
        print("Firewall server running on http://localhost:8000")
        httpd.serve_forever()

if __name__ == "__main__":
    run_firewall_server()
