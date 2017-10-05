# apk-downloader
python script for downloading the apks from google play
based on [gplaycli](https://github.com/matlink/gplaycli)

# usage
python download_apks.py [-h] [-u]

Download listed Apks from the google play.

optional arguments:
* -h, --help  show this help message and exit
* -u          update apk

# Mac install
```shell
# install gplaycli and other requirements
pip install -r requirements.txt
```

then modify ssl cert file name from /usr/local/lib/python2.7/site-packages/ext_libs//googleplay_api/googleplay.py
```
#ssl_verify="/etc/ssl/certs/ca-certificates.crt"
ssl_verify="/etc/ssl/cert.pem"
```
