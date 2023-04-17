import os
import shutil


file_types = {
    "Images" : [".jpg", ".psd", ".xcf", ".ai", ".cdr", ".tif", ".tiff", ".bmp", ".jpeg", ".gif", ".png", ".eps", ".raw", ".cr2", ".nef", ".orf", ".sr2"],
    "Documents" : [".doc", ".docx", ".pdf", ".txt", ".odt", ".rtf", ".wpd", ".xml", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
    "Codes" : [".py", ".c", ".cpp", ".html", ".htm", ".js", ".h", ".cs", ".css", ".ipynb", ".php", ".java", ".swift", ".vb"],
    "Videos" : [".avi", ".mpg", ".mpeg", ".wmv", ".vob", ".flv", ".3gp"],
    "Audios" : [".mp3", ".wma", ".wpl", ".wav", ".mid", ".midi"],
    "Executables" : [".exe", ".apk", ".com", ".wsf", ".bin", ".bat"],
    "Folders" : [".zip", ".tar", ".zipx", ".rar", ".7z", ".gz", ".tgz", ".iso", ".img"],
    "Installers" : [".msp", ".mst", ".idt", ".msi", ".msm", ".cub", ".pcp"]
}


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_out(src_path, dest_path):
    root, dirs, files = next(os.walk(src_path))

    create_dir(src_path)

    if not dirs == []:
        out_path = dest_path + "Folders/"
        create_dir(out_path)
        for dir in dirs: 
            shutil.move(root + dir + '/', out_path)


    for file in files:
        ext = os.path.splitext(file)[-1]
        ftype = "Misc"
        for key, val in file_types.items():
            if ext in val:
                ftype = key
                break
        out_path = dest_path + ftype + "/"
        create_dir(out_path)
        fpath = os.path.join(root, file)
        shutil.move(fpath, out_path)



dl_path = "C:/Users/Ameer Hamza/Downloads/"
dest_path = "C:/Users/Ameer Hamza/Organized Downloads/"

move_out(dl_path, dest_path)
