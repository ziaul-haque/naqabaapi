from flask_script import Manager, Server
from run import create_app

app = create_app()

manager = Manager(app)

manager.add_command("runserver", Server())


if __name__ == '__main__':
    manager.run()
