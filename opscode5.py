import subprocess
result = subprocess.run("git --version", shell=True, capture_output=True, text=True)
print(result.stdout)

result = subprocess.run("df -h", shell=True, capture_output=True, text=True)
print(result.stdout)
