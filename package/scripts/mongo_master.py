import os

from resource_management import *
from mongo_base import MongoBase

class MongoMaster(MongoBase):
    mongo_packages=['mongodb-org']

    def install(self, env):
        import params
        env.set_params(params)
        self.installMongo(env)
        self.configure(env)

    def configure(self,env):
        import params
        env.set_params(params)
        self.configureMongo(env)

    def start(self, env):
        import params
        print "start mongodb"
        Execute('service mongod start > /dev/null ')

    def stop(self, env):
        print "stop services.."
        Execute('service mongod stop')

    def restart(self, env):
        import params
        print "restart mongodb"
        Execute('service mongod restart > /dev/null ')

    def status(self, env):
        print "checking status..."
        Execute('service mongod status')


if __name__ == "__main__":
    MongoMaster().execute()
