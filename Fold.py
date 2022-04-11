import os
def sor(p,fl,format):
    os.chdir(p)
    i=61
    files=os.listdir(p)
    with open (fl) as f:
        flist=f.read().split("\n")
    for file in files:
        if file not in flist:
            os.rename(file,file.capitalize())
        if os.path.splitext(file)[1]==format:
            os.rename(file,f"{i}{format}")
            i+=1
sor(r"C:\Users\ultim\OneDrive\Pictures\Wallpaper",r"C:\Codes\Folder Formatting\dont_change.txt",".jfif")
