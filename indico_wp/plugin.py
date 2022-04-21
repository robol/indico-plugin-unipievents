from wtforms.validators import DataRequired

from indico.core import signals
from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint

from .controllers import RHWpUpdate, RHWpStatic
from indico.modules.events.management.views import WPEventManagement

import os, requests, re

from .forms import SettingsForm

from flask import request

class IndicoWp(IndicoPlugin):
    """Indico Wordpress interface

    This plugin synchronizes the changes in Indico events to an
    external Wordpress instance, creating posts with a custom 
    post type 'events'. """

    configurable = True
    settings_form = SettingsForm

    default_settings = {
        'enabled': False,
        'wp_url': '',
        'wp_api_key': ''
    }

    def __init__(self, *args, **kwargs):
        super().init()
        
        # Connect to the event modification signals
        self.connect(signals.event.created, self._on_event_created)
        self.connect(signals.event.deleted, self._on_event_deleted)
        self.connect(signals.event.updated, self._on_event_updated)

        self.template_hook('html-head', self.inject_js)

    def inject_js(self, **kwargs):
        if self.settings.get('enabled') and re.match('^/event/\d+/manage/$', request.path):
            return "<script src='./wp/js/main.js'></script>"

    def _on_event_created(self, event, **kwargs):
        if self.settings.get('enabled'):
            print("Created")
            print(event)
            print(kwargs)
            
            print("Event ID = %d" % event.id)
            print("Category ID = %d" % event.category_id)
            print("External URL = %s" % event.external_url)
            print("Event title = %s" % event.title)
            print("Event description = %s" % event.description)
            
            try:
                pass
                # requests.post(self._wp_url, data = { 'a': 'b' })
            except Exception as e:
                print("Failed to propagate changes to Wordpress")
                print(e)

    def _on_event_deleted(self, event, **kwargs):
        if self.settings.get('enabled'):
            print("Deleted")
            print("Event ID = %d" % event.id)
            print("Category ID = %d" % event.category_id)
            print("External URL = %s" % event.external_url)
            print("Event title = %s" % event.title)
            print("Event description = %s" % event.description)

    def _on_event_updated(self, event, **kwargs):
        if self.settings.get('enabled'):
            print("Updated")
            print("Event ID = %d" % event.id)
            print("Category ID = %d" % event.category_id)
            print("External URL = %s" % event.external_url)
            print("Event title = %s" % event.title)
            print("Event description = %s" % event.description)

    def get_blueprints(self):
        return blueprint        
    

blueprint = IndicoPluginBlueprint('wp', __name__, url_prefix='/event/<int:event_id>/manage/wp')

blueprint.add_url_rule('/update', 'update', view_func = RHWpUpdate)
blueprint.add_url_rule('/js/main.js', 'js', view_func = RHWpStatic)
