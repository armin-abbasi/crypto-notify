# Read environment variables from .env file
def env(variable_name: str):
    env_file = open('.env')
    variables = env_file.readlines()

    for item in variables:
        key, value = item.split('=')
        if key == variable_name:
            return value