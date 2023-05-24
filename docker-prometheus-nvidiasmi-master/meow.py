import subprocess

result1 = subprocess.run(["nvidia-smi", "-q", "-i", "0", "-x"], stdout=subprocess.PIPE).stdout.decode("utf-8")
meow = "\n".join(result1.split("\n")[:-2])
result2 = subprocess.run(["nvidia-smi", "-q", "-i", "1", "-x"], stdout=subprocess.PIPE).stdout.decode("utf-8")
meow2 = "\n".join(result2.split("\n")[7:])
print(meow+meow2, end="")