#!/usr/bin/env python3

import subprocess

def get_brightness():
    try:
        # Run the brightness.sh script and capture its output
        result = subprocess.run(['/bin/bash', '-c', '~/.config/qtile/scripts/brightness.sh'], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print(get_brightness())
