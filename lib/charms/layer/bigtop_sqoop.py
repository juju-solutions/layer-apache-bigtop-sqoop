from jujubigdata import utils
from charms.layer.apache_bigtop_base import Bigtop
from path import Path
from charmhelpers.core import unitdata
from charms import layer


class Sqoop(object):
    def __init__(self, dist_config):
        self.dist_config = dist_config #or utils.DistConfig(data=layer.options('apache-bigtop-base'))

    def install_sqoop(self):
        roles = ['hadoop-client']

        bigtop = Bigtop()
        bigtop.render_site_yaml(roles=roles)
        bigtop.trigger_puppet()

        roles = ['sqoop-server', 'sqoop-client']

        bigtop.render_site_yaml(roles=roles)
        bigtop.trigger_puppet()

