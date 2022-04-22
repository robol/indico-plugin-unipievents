from flask import jsonify, request, Response
import os, warnings

from indico.modules.events.management.controllers import RHManageEventBase
from indico.modules.events.models.events import Event

from .wordpress import update_event

with open(os.path.join(
        os.path.dirname(__file__),
        'static', 'main.js')) as h:
    js_data = h.read()

class RHWpUpdate(RHManageEventBase):

    def _process(self):
        event_id = request.view_args['event_id']
        event = Event.get(event_id)

        success = True
        message = "Event updated successfully"

        try:
            update_event(event)
        except:
            success = False
            message = "Failure to update the event with ID = %d" % event_id
            warnings.warn(message)
                            
        return jsonify({
            "success": success,
            "message": message
        })

class RHWpStatic(RHManageEventBase):
    
    def _process(self):
        return Response(js_data, mimetype = 'text/javascript')
