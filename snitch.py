import http.server
from colorama import Fore, Style

from sys import argv

# get port from command line
if len(argv) > 1:
    port = int(argv[1])
else:
    port = 8080


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.run()

    def do_POST(self):
        self.run()

    def do_PUT(self):
        self.run()

    def do_PATCH(self):
        self.run()

    def do_DELETE(self):
        self.run()

    def do_OPTIONS(self):
        self.run()

    def do_HEAD(self):
        self.run()

    def do_CONNECT(self):
        self.run()

    def do_TRACE(self):
        self.run()

    def do_QUERY(self):
        self.run()


    def log_message(self, format, *args):
        print(Fore.YELLOW + "##############################################################")
        print(Fore.LIGHTRED_EX + args[0])
        for key in self.headers.keys():
            print(Fore.MAGENTA + key + ": " + Fore.BLUE + self.headers[key])
        content_length = self.headers.get('Content-Length')
        if content_length is not None:
            content_len = int(content_length)
            post_body = self.rfile.read(content_len)
            print(Fore.GREEN + post_body.decode("utf-8"))
        Style.RESET_ALL

    def run(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-Length', 11)
        self.end_headers()
        message = "HTTP Snitch"
        self.wfile.write(bytes(message, "utf8"))


with http.server.HTTPServer(('', port), Handler) as server:
    print(Fore.GREEN + "HTTP Snitch server started at port " + Fore.RED + str(port))
    server.serve_forever()
