import json

def application(environ, start_response):
    if environ["REQUEST_METHOD"] == "GET" and environ["PATH_INFO"] == "/info":
        response_data = {
            "method": environ["REQUEST_METHOD"],
            "url": environ["PATH_INFO"],
            "protocol": environ["SERVER_PROTOCOL"]
        }
        response_body = json.dumps(response_data)
        start_response("200 OK", [("Content-Type", "application/json")])
        return [response_body.encode("utf-8")]
    else:
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"Not Found"]
