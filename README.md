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

## Development

You can start the development environment by adjusting the configuration
in the ```indico.env.sample``` file and renaming it ```indico.env```. Then,
you can start the containers by
```
sudo docker-compose up
```
and connect to [http://localhost:9090](http://localhost:9090). Configure your 
first user account. To update the plugin version in the container, run
```
sudo docker-compose exec -u root web bash -c "cd /indico-unipievents && python3 setup.py install && touch /indico/indico.wsgi"
```
that will rebuild the plugin and restart the WSGI server.  
