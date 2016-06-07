from charmhelpers.core import hookenv
from charms.layer.bigtop_oozie import Oozie
from charms.reactive import is_state, set_state, remove_state, when, when_not
from charms.layer.hadoop_client import get_dist_config


@when('bigtop.available', 'db.available')
@when_not('oozie.installed')
def install_oozie(db):
    hookenv.status_set('maintenance', 'Installing Oozie')
    dist = get_dist_config()
    oozie = Oozie(dist)
    oozie.install_oozie()
    set_state('oozie.installed')
