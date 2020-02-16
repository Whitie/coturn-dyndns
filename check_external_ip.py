#!/usr/bin/python

import logging
import os
import sys

from subprocess import run, CalledProcessError
from urllib import request


URL = 'https://api.ipify.org'

logging.basicConfig(
    format='[%(asctime)s] %(filename)s/%(funcName)s %(message)s',
    datefmt='%Y-%m-%d',
    level=logging.INFO
)


class IPError(Exception):
    pass


def get_external_ip():
    try:
        logging.info('Trying to get external IP with script')
        process = run(['external-ip'], check=True, capture_output=True,
                      text=True)
        ip = process.stdout.strip()
        if ip:
            logging.info('IP: %s', ip)
            return ip
    except CalledProcessError:
        logging.error('Failed to get IP')
    try:
        logging.info('Trying to get external IP from %s using urllib', URL)
        out = request.urlopen(URL).read()
        ip = out.decode('utf-8').strip()
        if ip:
            logging.info('IP: %s', ip)
            return ip
    except:
        logging.error('Failed to get IP')
    raise IPError('Could not get external IP')


def get_ip_from_file(filepath):
    if not os.path.isfile(filepath):
        logging.info('File %s does not exist', filepath)
        return
    with open(filepath, 'r', encoding='ascii') as fp:
        data = fp.read().strip()
    return data.split('=')[1].strip()


def write_new_ip(ip, filepath):
    tmp = f'{filepath}.tmp'
    logging.info('Writing new IP to %s', tmp)
    with open(tmp, 'w', encoding='ascii') as fp:
        fp.write(f'EXTERNAL_IP={ip}')
    if os.path.exists(filepath):
        logging.info('Removing %s', filepath)
        os.remove(filepath)
    logging.info('Renaming %s to %s', tmp, filepath)
    os.rename(tmp, filepath)


def main(statefile='external_ip'):
    cache_dir = '/tmp'
    filepath = os.path.join(cache_dir, statefile)
    old_ip = get_ip_from_file(filepath)
    if old_ip:
        logging.info('Old IP: %s', old_ip)
    try:
        ip = get_external_ip()
    except IPError:
        sys.exit(1)
    if ip != old_ip:
        logging.info('New IP detected')
        write_new_ip(ip, filepath)
    else:
        logging.info('IP not changed')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(get_external_ip())
    else:
        main(sys.argv[1])
