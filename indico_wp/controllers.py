from flask import jsonify, request, Response
from indico.modules.events.management.controllers import RHManageEventBase

from flask_pluginengine import current_plugin

import os

with open(os.path.join(
        os.path.dirname(__file__),
        'static', 'main.js')) as h:
    js_data = h.read()

class RHWpUpdate(RHManageEventBase):

    def _process(self):
        return jsonify({ "message": "Test", 'api_key': current_plugin.settings.get('wp_api_key') })

class RHWpStatic(RHManageEventBase):
    
    def _process(self):
        return Response(js_data, mimetype = 'text/javascript')
