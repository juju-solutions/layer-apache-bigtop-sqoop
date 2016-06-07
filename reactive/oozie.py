from charmhelpers.core import hookenv
from charms.layer.bigtop_oozie import Oozie
from charms.reactive import is_state, set_state, remove_state, when, when_not
from charms.layer.hadoop_client import get_dist_config


@when('bigtop.available', 'mysql.available')
@when_not('oozie.installed')
def install_oozie():
    hookenv.status_set('maintenance', 'Installing Oozie')
    dist = get_dist_config()
    oozie = Oozie(dist)
    oozie.install_oozie()
    set_state('oozie.installed')

#@when('bigtop.available', 'oozie.installed')
#@when_not('oozie.available')
#def configure_oozie():
#    hookenv.status_set('maintenance', 'Installing Pig')
#    dist = get_dist_config
#    oozie = Pig(dist)
#    hadoop_ready = is_state('hadoop.ready')
#    if hadoop_ready:
#        hookenv.status_set('maintenance', 'configuring oozie (mapreduce)')
#        hookenv.log('YARN is ready, configuring Apache Pig in MapReduce mode')
#        oozie.configure_yarn()
#        remove_state('oozie.configured.local')
#        set_state('oozie.configured.yarn')
#        hookenv.status_set('active', 'ready (mapreduce)')
#        hookenv.log('Apache Pig is ready in MapReduce mode')
#    else:
#        hookenv.status_set('maintenance', 'configuring oozie (local)')
#        hookenv.log('YARN is not ready, configuring Pig in local mode')
#        oozie.configure_local()
#        remove_state('oozie.configured.yarn')
#        set_state('oozie.configured.local')
#        hookenv.status_set('active', 'ready (local)')
#        hookenv.log('Apache Pig is ready in local mode')
#
