#!/usr/bin/env python
"""Static file server, using Python's CherryPy. Should be used when Django's static development server just doesn't cut."""
import cherrypy
from cherrypy.lib.static import serve_file

import os.path

class Root:
    @cherrypy.expose
    def index(self, name):
        return 'serve_file(os.path.join(static_dir, name))'

if __name__=='__main__':
    static_dir = os.path.dirname(os.path.abspath(__file__))  # Root static dir is this file's directory.

    cherrypy.config.update( {  # I prefer configuring the server here, instead of in an external file.
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 8080,
        } )
    conf = {
        '/': {  # Root folder.
            'tools.staticdir.on':   True,  # Enable or disable this rule.
            'tools.staticdir.root': static_dir,
            'tools.staticdir.dir':  '',
        }
    }

    cherrypy.quickstart(Root(), '/', config=conf)  # ..and LAUNCH ! :)