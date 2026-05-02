import unittest
from dotenv import load_dotenv
from env_manager import EnvironmentManager, Envi

class TestEnvironmentManager(unittest.TestCase):

    def setUp(self):
        self.env_manager = EnvironmentManager()

    def test_create_environment(self):
        env_name = 'test_env'
        env_variables = {'VAR1': 'value1', 'VAR2': 'value2'}
        self.env_manager.create_environment(env_name, env_variables)
        self.assertEqual(len(Envi.get_environments()), 1)

    def test_get_environment(self):
        env_name = 'test_env'
        env_variables = {'VAR1': 'value1', 'VAR2': 'value2'}
        self.env_manager.create_environment(env_name, env_variables)
        environment = Envi.get_environment(env_name)
        self.assertEqual(environment['name'], env_name)

    def test_update_environment(self):
        env_name = 'test_env'
        env_variables = {'VAR1': 'value1', 'VAR2': 'value2'}
        self.env_manager.create_environment(env_name, env_variables)
        environment = Envi.get_environment(env_name)
        environment['name'] = 'new_name'
        self.env_manager.update_environment(environment)
        self.assertEqual(Envi.get_environment('new_name')['name'], 'new_name')

    def test_delete_environment(self):
        env_name = 'test_env'
        env_variables = {'VAR1': 'value1', 'VAR2': 'value2'}
        self.env_manager.create_environment(env_name, env_variables)
        environment = Envi.get_environment(env_name)
        self.env_manager.delete_environment(environment)
        self.assertEqual(len(Envi.get_environments()), 0)

    def test_get_environment_variables(self):
        env_name = 'test_env'
        env_variables = {'VAR1': 'value1', 'VAR2': 'value2'}
        self.env_manager.create_environment(env_name, env_variables)
        environment = Envi.get_environment(env_name)
        variables = self.env_manager.get_environment_variables(environment)
        self.assertEqual(variables, env_variables)

    def test_set_environment_variable(self):
        env_name = 'test_env'
        env_variables = {'VAR1': 'value1', 'VAR2': 'value2'}
        self.env_manager.create_environment(env_name, env_variables)
        environment = Envi.get_environment(env_name)
        variable_name = 'new_var'
        new_value = 'new_value'
        self.env_manager.set_environment_variable(environment, variable_name, new_value)
        variables = self.env_manager.get_environment_variables(environment)
        self.assertEqual(variables[variable_name], new_value)

    def test_get_database_config(self):
        env_name = 'test_env'
        env_variables = {'VAR1': 'value1', 'VAR2': 'value2'}
        self.env_manager.create_environment(env_name, env_variables)
        environment = Envi.get_environment(env_name)
        database_config = self.env_manager.get_database_config(environment)
        self.assertEqual(database_config['host'], '')

class TestEnvi(unittest.TestCase):

    def test_get_environments(self):
        environments = Envi.get_environments()
        self.assertEqual(len(environments), 0)

if __name__ == '__main__':
    unittest.main()