import os, pwd, grp

from resource_management import *

class MongoBase(Script):
    repos_file_path = '/etc/yum.repos.d/mongodb.repo'
    config_file_path = '/etc/mongod.conf'
    mongo_packages=None

    def installMongo(self, env):
        import params

        env.set_params(params)

        self.install_packages(env)
        if os.path.exists(self.repos_file_path):
            print "File exists"
        else:
            print "file not exists"
            File(self.repos_file_path,
                 content=Template("mongodb.repo"),
                 mode=0644
                 )
        print "installing mongodb..."
        if self.mongo_packages is not None and len(self.mongo_packages):
            for pack in self.mongo_packages:
                Package(pack)
                

    def configureMongo(self, env):
        import params

        env.set_params(params)
        if not os.path.exists(params.db_path):
            Directory([params.db_path],
          	  owner='mongod',
          	  group='mongod',
          	  recursive=False
          	  )
        Execute('rm ' + self.config_file_path)
        print 'Updating mongod config file...'
        File(self.config_file_path,
             content=Template("mongod.conf.j2"),
             mode=0644,
             owner='mongod'
             )
