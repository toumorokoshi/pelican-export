# pelican-export

pelican-export is a plugin into pelican that handles exporting of
posts from pelican to other formats. Currently the following formats
are supported:

* Wordpress

# Installation

pelican-export requires python3.7 or above.

    pip install pelican-export


# Usage

As with any pelican plugin, the plugin should be included in the PLUGINS global
variable in your pelicanconf.py. In addition, you should configure the exporter
using the configure_exporter method exposed. Here's an example with WordPress:

    # declare the plugin for pelican
    PLUGINS = ["pelican-export"]

    # configure the pelican_export itself
    from pelican_export import configure_exporter

    configure_exporter(export_type="wordpress", export_configuration={
        "url": "http://example.com/xmlrpc.php", 
        "username": "foo", 
        "password": "bar",
    })


# Authoring an Exporter

See [the exporter](./pelican_export/exporter.py) for the interface, and [the initialization code](./pelican_export/__init__.py) for how to integrate it as an option.