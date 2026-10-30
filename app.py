import subprocess

def run_command(user_input):
    result = subprocess.run(
        user_input,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout
