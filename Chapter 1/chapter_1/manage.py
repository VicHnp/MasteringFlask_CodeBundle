from flask.ext.script import Manager, Server
from main import app

manager = Manager(app)
manager.add_command("server", Server())

@manager.shell
def make_shell_context():
    b = dict(app=app)
    print('xxxx')
    print(b)
    print('xxx')
    return b
    #return dict(app=app)

if __name__ == "__main__":
    manager.run()
