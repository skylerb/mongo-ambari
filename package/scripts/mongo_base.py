import os, pwd

from resource_management import *

class MongoBase(Script):
    repos_file_path = '/etc/yum.repos.d/mongodb.repo'
    config_file_path = '/etc/mongod.conf'
    mongo_packages=None

    def installMongo(self, env):
        import params

        env.set_params(params)

        self.install_packages(env)
        self.create_linux_user(params.mongo_user, params.mongo_group)
  	if params.mongo_user != 'root':
  		Execute('cp /etc/sudoers /etc/sudoers.bak')
  		Execute('echo "'+params.mongo_user+' ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers')
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
                
    def create_linux_user(self, user, group):
	  try: pwd.getpwnam(user)
	  except KeyError: Execute('adduser ' + user)
	  try: grp.getgrnam(group)
	  except KeyError: Execute('groupadd ' + group)

    def configureMongo(self, env):
        import params

        env.set_params(params)
        if not os.path.exist(params.db_path):
            Directory([params.db_path],
          	  owner=params.mongo_user,
          	  group=params.mongo_group,
          	  recursive=False
          	  )
        File(self.config_file_path,
             content=Template("mongod.conf.j2"),
             mode=0644
             )
