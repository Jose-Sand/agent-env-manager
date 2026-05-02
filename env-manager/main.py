import argparse
import env_manager.__init__ as init
from env_manager import EnvironmentManager

def main():
    parser = argparse.ArgumentParser(description='Env Manager CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Define subparser for create command
    create_parser = subparsers.add_parser('create', help='Create a new environment')
    create_parser.add_argument('--name', type=str, required=True, help='Environment name')
    create_parser.add_argument('--variables', nargs='+', help='Variables to set in the environment')

    # Define subparser for list command
    list_parser = subparsers.add_parser('list', help='List all environments')

    # Define subparser for delete command
    delete_parser = subparsers.add_parser('delete', help='Delete an environment')
    delete_parser.add_argument('--name', type=str, required=True, help='Environment name to delete')

    # Define subparser for set command
    set_parser = subparsers.add_parser('set', help='Set a variable in the current environment')
    set_parser.add_argument('--key', type=str, required=True, help='Variable key')
    set_parser.add_argument('--value', type=str, required=True, help='Variable value')

    # Define subparser for config command
    config_parser = subparsers.add_parser('config', help='Set a configuration in the current environment')
    config_parser.add_argument('--key', type=str, required=True, help='Configuration key')
    config_parser.add_argument('--value', type=str, required=True, help='Configuration value')

    # Define subparser for db command
    db_parser = subparsers.add_parser('db', help='Set a database configuration in the current environment')
    db_parser.add_argument('--host', type=str, required=True, help='Database host')
    db_parser.add_argument('--port', type=int, required=True, help='Database port')
    db_parser.add_argument('--database', type=str, required=True, help='Database name')

    args = parser.parse_args()

    if args.command == 'create':
        EnvironmentManager.create_environment(args.name, args.variables)
    elif args.command == 'list':
        EnvironmentManager.list_environments()
    elif args.command == 'delete':
        EnvironmentManager.delete_environment(args.name)
    elif args.command == 'set':
        EnvironmentManager.set_variable(args.key, args.value)
    elif args.command == 'config':
        EnvironmentManager.set_config(args.key, args.value)
    elif args.command == 'db':
        EnvironmentManager.set_db_config(args.host, args.port, args.database)

if __name__ == '__main__':
    main()