
from model.database import DatabaseEngine
from model.dao.member_dao import MemberDAO
from exceptions import ResourceNotFound, InvalidData, Error

# ma moffication 
def main():
    print("BDS Association application")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///bds.db')
    database_engine.create_database()

    # TODO to choose your action
    commands = {
        "exit": "Quit the Shell",
        "add": "Add association member",
        "list": "List association members",
        "search": "Show member profile",
        "delete": "Delete a member",
        "update": "Update a member",
        "help": "Show this help"
    }

    help(commands)

    while True:
        try:
            command = ask_command(commands)
            if command == 'exit':
                # Exit loop
                break
            elif command == 'add':
                # TODO
                continue
            elif command == 'list':
                with database_engine.new_session() as session:
                    members = MemberDAO(session).get_all()
                    # To_dict is function  defined in model/mapping/member.py
                    members_data = [member.to_dict() for member in members]
                return members_data
            elif command == 'search':
                # TODO
                continue
            elif command == 'delete':
                # TODO
                continue
            elif command == 'update':
                # TODO
                continue
            elif command == 'help':
                # TODO
                continue
            else:
                print("Unknown command")
        except ResourceNotFound:
            error_message("Member not found")
        except InvalidData as e:
            error_message(str(e))
        except Error as e:
            error_message("An error occurred (%s)" % str(e))


def help(commands):
    print()
    for command, description in commands.items():
        print("  * %s: '%s'" % (command, description))
    print()


def ask_command(commands):

    command = input('command > ').lower().strip()
    while command not in commands.keys():
        print("Unknown command")
        command = input('command >').lower().strip()

    return command


def error_message(message: str):
    print("/!\\ %s" % message.upper())


if __name__ == "__main__":
    main()
