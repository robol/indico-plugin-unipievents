from wtforms import StringField, BooleanField
from indico.web.forms.base import IndicoForm
from indico.web.forms.widgets import SwitchWidget

from indico_wp import _

class SettingsForm(IndicoForm):
    enabled = BooleanField(_("Enabled"), widget=SwitchWidget())
    wp_url = StringField(_("Wordpress URL"))
    wp_api_key = StringField(_("Wordpress API key"))
