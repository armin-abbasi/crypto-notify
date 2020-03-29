# Read environment variables from .env file
def env(variable_name: str) -> str:
    env_file = open('.env')
    variables = env_file.readlines()

    for item in variables:
        key, value = item.split('=')
        if key == str(variable_name).strip():
            return str(value).strip()