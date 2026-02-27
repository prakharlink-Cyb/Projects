import os
import shutil   

def read_directory():
    file = os.listdir("normal")
    print("Files found: ",file)

def MakeDirec():
    os.makedirs("Documents/Pythonfiles",exist_ok=True)
    os.makedirs("Documents/Webfiles",exist_ok=True)
    os.makedirs("Documents/Cppfiles",exist_ok=True)
    os.makedirs("Documents/Other",exist_ok=True)
    os.makedirs("Documents", exist_ok=True)


def Reading():
    files = os.listdir("normal")

    for file in files:
        source_path = os.path.join("normal",file)

        if os.path.isdir(source_path):
            continue

        name, ext = os.path.splitext(file)
        ext = ext.lower()  # ensures case-insensitive match

        if ext == ".pdf":
            shutil.move(f"normal/{file}", "Documents")
        elif ext == ".py":
            shutil.move(f"normal/{file}", "Documents/Pythonfiles")
        elif ext == ".html":
            shutil.move(f"normal/{file}", "Documents/Webfiles")
        elif ext == ".cpp":
            shutil.move(f"normal/{file}", "Documents/Cppfiles")
        else:
            shutil.move(f"normal/{file}", "Documents/Other")


read_directory()
MakeDirec()
Reading()

print("✅ Files organized successfully.")

