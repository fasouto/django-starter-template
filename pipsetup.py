import sys
import subprocess
import os

# default dependencies, 
def printPackage(package):
    print('----------------------------------------------------------------##')
    print("Installed Package: {}".format(package))
    print('----------------------------------------------------------------##')


def install(package, arg):

    if arg:
        subprocess.call([sys.executable, '-m', 'pip', 'install', package, arg])
    else:
        subprocess.call([sys.executable, '-m', 'pip', 'install', package])

    printPackage(package)


if __name__ == '__main__':
    packages = {
        'rcssmin ': '--install-option="--without-c-extensions"',
        'rjsmin ': '--install-option="--without-c-extensions"',
        # rcssmin and rjsmin have to be installed this way.
        'django~=2.0.0': '',
        'django-admin': '',
        'django-compressor': '--upgrade',
        'django[argon2]': '',
        'django-debug-toolbar': ''
    }

    for k, v in packages.items():
        install(k, v)

