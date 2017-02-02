import commands
import argparse

LIST_FILE = 'list.txt'
FOLDER='apks'
DOWNLOAD_CMD = 'gplaycli -v -f ' + FOLDER + ' -d '
UPDATE_CMD = 'gplaycli -v -u ' + FOLDER

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
        status, result = commands.getstatusoutput(cmd)
        print result

def UpdateApks():
    status, result = commands.getstatusoutput(UPDATE_CMD)
    print result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download listed Apks from the google play.')
    parser.add_argument('-u', dest='update', action='store_true', default=False, help='update apk')
    args = parser.parse_args()

    if args.update:
        UpdateApks()
    else:
        DownloadApks()
