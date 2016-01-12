from resource_management import *
from resource_management.core.system import System
import os

config = Script.get_config()

db_path = default('configurations/mongodb/db_path', '/data/mongo')
bind_ip = default('configurations/mongodb/bind_ip', '0.0.0.0')
tcp_port = default('configurations/mongodb/tcp_port', '27017')
log_path = default('configurations/mongodb/log_path', '/var/log/mongodb/mongod.log')
db_auth = default('configurations/mongodb/db_auth', 'false')
# The web status page is always accessible at a port number that is 1000 greater than the port determined by tcp_port.
mongo_host = default('configurations/mongodb/mongo_host', 'unknown')
if mongo_host=="unknown":
    if bind_ip not in ['0.0.0.0','127.0.0.1']:
        mongo_host==bind_ip
