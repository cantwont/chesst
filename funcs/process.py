import time
from funcs.get_reset import reset_hint
from funcs.get_profile import get_profile

def process_names(names, delay):
    print(f'Waiting {delay}s between each search')
    index = 0
    while index < len(names):
        time.sleep(delay)
        current_name = names[index]

        print(f'{current_name}: {reset_hint(current_name).get("email", "Email not found")} | {get_profile(current_name)}')

        index += 1