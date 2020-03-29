# Read environment variables from .env file
def env(variable_name: str) -> str:
    env_file = open('.env')
    variables = env_file.readlines()

    for item in variables:
        key, value = item.split('=')
        if key == str(variable_name).strip():
            return str(value).strip()


# Check if the given number passes threshold or not
def check_range(number: int, min: int, max: int) -> bool:
    if number < min or number > max:
        return True
    return False
