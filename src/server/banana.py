#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import tornado.httpserver
import tornado.ioloop
import tornado.locale
import tornado.web
from tornado.options import define, options, parse_command_line

import util.config.config
import router
from util.log.log import runtime_log

logger = runtime_log()

port = int(util.config.config.get("global", "port"))
define("app", default="pandora", help="service name")
debug_mode = int(util.config.config.get("global", "server_debug_mode"))

settings = {
    "debug": debug_mode,
    "template_path": os.getenv("TEMPLATES"),
}
define("port", default=port, help="pandora listen port")

def main():
    parse_command_line()
    log = "start pandora api server at %s" % options.port
    logger.info(log)
    print log
    app = tornado.web.Application(router.url_map, **settings)
    app.listening_port = options.port
    server = tornado.httpserver.HTTPServer(app, max_body_size=800*1024*1024)
    server.bind(options.port)
    server.start(1)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
