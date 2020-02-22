import socket
import webapp

class urlsAleat(webapp.webApp):
    def process(self, parsedRequest):
        return ("200 OK", b"<html><body><h1>Hello World!</h1>" +
                            b"<p><a href='"+ bytes(str(aleat), 'utf-8') +
                            b"'>Dame otra</a>" +
                            b"</p>" +
                            b"</body></html>")

if __name__ == "__main__":
    testWebApp_hola = urlsAleat("localhost", 1234)
