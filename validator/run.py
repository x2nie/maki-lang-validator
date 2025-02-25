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

    #? move the compiled maki into the source-code's folder
    makifilepath = f'{mfile}aki' 
    makifilename = os.path.split( makifilepath )[1]
    here_makifile = os.path.join( CURDIR, makifilename )
    if os.path.exists(here_makifile):
        there_makifile = os.path.join(outdir, makifilename)
        if os.path.exists(there_makifile):
            os.remove(there_makifile)
        os.rename(here_makifile, there_makifile)

    # print("Done.")

if __name__ == '__main__':

    # compile('mc/test.m')
    # compile('res/assignment/star-eq.m')
    compile('res/misc/question.m')