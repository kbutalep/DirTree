import os


def dtg(cwd):
    for root, dirs, files in os.walk(cwd):
        print(os.path.basename(root))
        for f in files:
            print(f)


dtg('.')