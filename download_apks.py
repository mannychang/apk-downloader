import argparse
import os
import subprocess

LIST_FILE = 'list.txt'
FOLDER='apks'
DOWNLOAD_CMD = 'gplaycli -v -f ' + FOLDER + ' -d '
UPDATE_CMD = 'gplaycli -v -u ' + FOLDER

def CheckEnv():
    if not os.path.isdir(FOLDER):
        os.makedirs(FOLDER)

def DownloadApks():
    package_list = list()
    f = open(LIST_FILE)

    for line in f.readlines():
        line = line.strip()
        if not len(line) or line.startswith('#'):
            continue
        package_list.append(line)

    f.close()

    for pkg in package_list:
        cmd = DOWNLOAD_CMD + pkg
        print cmd
        subprocess.call(cmd.split())

def UpdateApks():
    subprocess.call(UPDATE_CMD.split())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download listed Apks from the google play.')
    parser.add_argument('-u', dest='update', action='store_true', default=False, help='update apk')
    args = parser.parse_args()

    CheckEnv()

    if args.update:
        UpdateApks()
    else:
        DownloadApks()
