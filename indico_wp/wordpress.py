#
# Implementation of the Wordpress API for adding / updating / deleting
# events as custom post types. 
#

import requests

from flask_pluginengine import current_plugin
from requests.auth import HTTPBasicAuth

from indico.modules.events.models.events import EventType

def post_request(endpoint, data):
    wp_url = current_plugin.settings.get('wp_url')
    wp_username = current_plugin.settings.get('wp_username')
    wp_password = current_plugin.settings.get('wp_application_password')

    if wp_url[-1] == '/':
        wp_url = wp_url[:-1]
    if endpoint[0] != '/':
        endpoint = '/' + endpoint

    response = requests.post(wp_url + endpoint,
                             data = data,
                             auth = HTTPBasicAuth(wp_username, wp_password))

    if response.status_code >= 300:
        raise RuntimeError('Invalid response from the Wordpress API')

def delete_event(event_id):
    #FIXME: We need support for the indico_id meta and custom
    # event post type to implement this, see update_event(). 
    print("Deleting event with id = %d" % event_id)
    print("FIXME: Not implemented")

def update_event(event):
    #FIXME: We need to update this function to post custom post
    # types of type 'event', and to check if an event with the
    # appropriate meta key 'indico_id' exists; if that's the
    # case, we just update the post.
    
    print("Updating event with id = %d" % event.id)

    post_title = event.title
    if event.type == 'lecture':
        post_title = "Seminar: " + post_title

    description = str(event.description)
    description += "<p>Further information is available at the <a href=\"%s\">event page</a> on the Indico platform</p>"  % event.external_url

    event_data = {
        'status': 'publish',
        'title': post_title,
        'content': description,
        #'meta': {
        #    'indico_id': event.id
        #}
    }

    post_request('/wp-json/wp/v2/posts', event_data)
    
    #print("| Category ID = %d" % event.category_id)
    #print("| External URL = %s" % event.external_url)
    #print("| Event title = %s" % event.title)
    #print("| Event description = %s" % event.description)
    #print("| Type: %s" % event.type)
    #print(event.type == 'lecture')

    print("FIXME: Not implemented")
