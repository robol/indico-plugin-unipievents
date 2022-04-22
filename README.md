# Indico WP

Indico WP is an Indico plugin that synchronizes events to a Wordpress 
instance running the Unipi Events plugin; it is currently in use at the
Department of Mathematics of the University of Pisa. 

## Installation

You may install the plugin by cloning the repository on the Indico server
and then running:
```
python3 setup.py install
```
Check that the plugin is installed by running
```
indico setup list-plugins
```
To enable the plugin, insert the line 
```
PLUGINS={ 'wp' }
```
to your ```indico.conf```, or just add ```'wp'``` to the list of loaded
plugins in case you already have other plugins loaded. 
