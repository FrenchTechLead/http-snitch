from http.server import BaseHTTPRequestHandler, HTTPServer
from colorama import Fore, Back, Style

from sys import argv

# get port from command line
if len(argv) > 1:
    port = int(argv[1])
else:
    port = 8080

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.run()
    def do_POST(self):
        self.run()
    def do_DELETE(self):
        self.run()
    def log_message(self, format, *args):
        print(Fore.YELLOW + "##############################################################")
        print(Fore.LIGHTRED_EX + args[0])
        for key in self.headers.keys():
            print(Fore.MAGENTA + key + ": " + Fore.BLUE + self.headers[key])
        Style.RESET_ALL

    def run(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "HTTP Snitch"
        self.wfile.write(bytes(message, "utf8"))


with HTTPServer(('', port), Handler) as server:
    print(Fore.GREEN + "HTTP Snitch server started at port " + Fore.RED + str(port))
    server.serve_forever()
