import socket
import webapp
import random

class urlsAleat(webapp.webApp):
    def process(self, parsedRequest):
        aleat = random.randint(0,1000)
        return ("200 OK", "<html><body><h1>Hello World!</h1>" +
                            "<p><a href='"+ str(aleat) +
                            "'>Dame otra</a>" +
                            "</p>" +
                            "</body></html>")

if __name__ == "__main__":
    testWebApp_hola = urlsAleat("localhost", 1234)
