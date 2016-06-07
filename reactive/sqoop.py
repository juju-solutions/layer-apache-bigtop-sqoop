from charmhelpers.core import hookenv
from charms.layer.bigtop_sqoop import Sqoop
from charms.reactive import is_state, set_state, remove_state, when, when_not
from charms.layer.hadoop_client import get_dist_config


@when('bigtop.available', 'hadoop.ready')
@when_not('sqoop.installed')
def install_sqoop(db):
    hookenv.status_set('maintenance', 'Installing Sqoop Server')
    dist = get_dist_config()
    sqoop = Sqoop(dist)
    sqoop.install_sqoop()
    set_state('sqoop.installed')

@when('sqoop.installed')
def set_ready():
    hookenv.status_set('active', 'Ready')
