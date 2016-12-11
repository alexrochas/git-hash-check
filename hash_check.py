import getopt
import zipfile

import sys


def show_jar_classes(jar_file):
    zf = zipfile.ZipFile(jar_file, 'r')
    try:
        lst = zf.infolist()
        for zi in lst:
            fn = zi.filename
            if fn == 'git.properties':
                    print(zf.read(fn).decode('utf-8'))
    finally:
        zf.close()

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ha:", ["artifact="])
    except getopt.GetoptError:
        print('hash_check.py -a <artifact_path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('hash_check.py -a <artifact_path>')
            sys.exit()
        elif opt in ("-a", "--artifact"):
            artifact = arg
            show_jar_classes(artifact)
