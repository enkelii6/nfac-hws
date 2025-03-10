def application(environ, start_response):
    if environ["REQUEST_METHOD"] == "GET" and environ["PATH_INFO"] == "/ping":
        start_response("200 OK", [("Content-Type", "text/plain")])
        return [b"pong"]
    else:
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"Not Found"]
