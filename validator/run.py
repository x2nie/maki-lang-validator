import os
import subprocess

CURDIR = os.path.dirname(__file__)
os.chdir(CURDIR)
exe_dir = os.path.join(CURDIR, 'mc')


def compile(mfile):
    mfile = os.path.abspath(mfile)
    outdir = os.path.dirname(mfile)
    # os.chdir(outdir)

    # Perintah yang ingin dijalankan
    # command = f"wine {exe_dir}/mc.exe {mfile} /outpath {outdir} " 
    command = f"wine {exe_dir}/mc.exe {mfile}" 

    # Menjalankan perintah dan menangkap outputnya
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)

    # Menyimpan hasil eksekusi ke dalam file
    with open(os.path.join(outdir, "log.txt"), "w") as file:
        file.write(result.stdout or result.stderr)

    print("Hasil eksekusi telah disimpan ke dalam done-abc.txt")

if __name__ == '__main__':

    compile('mc/test.m')