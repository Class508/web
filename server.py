from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

class MyHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/submit':
            # Get data from the POST request
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            form_data = json.loads(post_data)

            # Save form data to a file
            with open("submissions.txt", "a") as file:
                file.write(json.dumps(form_data) + "\n")

            # Send response
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Submission received!")

server = HTTPServer(('localhost', 8000), MyHandler)
print("Server running on http://localhost:8000")
server.serve_forever()
