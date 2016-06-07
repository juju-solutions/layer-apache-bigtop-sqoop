from jujubigdata import utils
from charms.layer.apache_bigtop_base import Bigtop
from path import Path
from charmhelpers.core import unitdata, hookenv, host
from charms import layer


class Sqoop(object):
    def __init__(self, dist_config):
        self.dist_config = dist_config #or utils.DistConfig(data=layer.options('apache-bigtop-base'))

    def install_sqoop(self):
        roles = ['hadoop-client']

        bigtop = Bigtop()
        bigtop.render_site_yaml(roles=roles)
        bigtop.trigger_puppet()

        roles = ['sqoop-server']

        bigtop.render_site_yaml(roles=roles)
        bigtop.trigger_puppet()

    def open_ports(self):
        for port in self.dist_config.exposed_ports('sqoop'):
            hookenv.open_port(port)

    def restart(self):
        self.stop()
        self.start()

    def start(self):
        host.service_start('sqoop2-server')

    def stop(self):
        host.service_stop('sqoop2-server')
