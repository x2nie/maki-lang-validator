import os
import subprocess

os.chdir(os.path.dirname(__file__))

# Perintah yang ingin dijalankan
command = "ls *.py"

# Menjalankan perintah dan menangkap outputnya
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)

# Menyimpan hasil eksekusi ke dalam file
with open("done-abc.txt", "w") as file:
    file.write(result.stdout)

print("Hasil eksekusi telah disimpan ke dalam done-abc.txt")