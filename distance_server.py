import distance
import io
import logging
import socketserver
from threading import Condition, Thread
from http import server

distance_sensor = distance.DistanceSensor()


class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/on':
            distance_sensor.start()
            self.send_response(200)
            self.end_headers()
        elif self.path == '/off':
            distance_sensor.pause()
            self.send_response(200)
            self.end_headers()
        else:
            self.send_error(404)
            self.end_headers()


class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


def main():
    try:
        address = ('', 8001)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        distance_sensor.stop()


if __name__ == '__main__':
    main()
