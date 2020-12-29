#!/usr/bin/env python

import os

from argparse import ArgumentParser
from configparser import ConfigParser
from pathlib import Path
from subprocess import run
from urllib.request import urlopen


DEFAULT_CONFIG_FILE = '/etc/coturn-dyn.conf'
COTURN_CONFIG = '/etc/turnserver/turnserver.conf'
EXTERNAL_IP_SERVICE = 'https://ipv4.icanhazip.com'
COTURN_SERVICE = 'turnserver.service'
SYSTEMCTL_BINARY = '/usr/bin/systemctl'


class ParserError(Exception):
    pass


def get_current_used_ips(coturn_config):
    ips = None
    with coturn_config.open() as fp:
        for line in fp:
            if line.startswith('external-ip'):
                ips = line.split('=')[1]
                break
    if ips is None:
        raise ParserError(f'No external-ip found in {str(coturn_config)}')
    if '/' in ips:
        return [ip.strip() for ip in ips.split('/')]
    else:
        return [ips.strip(), '']


def get_external_ip(service, stripchars=None):
    with urlopen(service) as sock:
        ip = sock.read().decode('ascii')
    if stripchars:
        return ip.strip(stripchars)
    return ip.strip()


def write_new_config(coturn_config, external_ip, internal_ip):
    new_config = coturn_config.parent / 'turnserver.conf.new'
    if internal_ip:
        internal_ip = f'/{internal_ip}'
    with coturn_config.open() as source, new_config.open('w') as dest:
        for line in source:
            if line.startswith('external-ip'):
                dest.write(f'external-ip={external_ip}{internal_ip}\n')
            else:
                dest.write(f'{line}')
    coturn_config.unlink()
    new_config.rename(coturn_config)


def get_config():
    parser = ArgumentParser(description='Check external IP and edit coturn '
                            'configuration if changed.')
    parser.add_argument('-c', '--config', default=DEFAULT_CONFIG_FILE,
                        help='Provide config file, default: %(default)s')
    args = parser.parse_args()
    config = dict(own_config=Path(args.config))
    cparser = ConfigParser()
    with config['own_config'].open() as fp:
        cparser.read_file(fp)
    config['external_ip_service'] = cparser.get(
        'global', 'external_ip_service', fallback=EXTERNAL_IP_SERVICE
    )
    config['coturn_service_file'] = cparser.get(
        'global', 'coturn_service_file', fallback=COTURN_SERVICE
    )
    config['coturn_config_file'] = Path(
        cparser.get('global', 'coturn_config_file', fallback=COTURN_CONFIG)
    )
    config['systemctl_binary'] = cparser.get(
        'global', 'systemctl_binary', fallback=SYSTEMCTL_BINARY
    )
    return config


def main():
    config = get_config()
    ips = get_current_used_ips(config['coturn_config_file'])
    external_ip = get_external_ip(config['external_ip_service'])
    if ips[0] == external_ip:
        print(f'IP not changed ({ips[0]})')
        return
    print('IP changed, new IP:', external_ip)
    write_new_config(config['coturn_config_file'], external_ip, ips[1])
    print('Changes written to', config['coturn_config_file'])
    cmd = [
        config['systemctl_binary'], 'restart', config['coturn_service_file']
    ]
    print('Restarting coturn, command:', ' '.join(cmd))
    run(cmd)


if __name__ == '__main__':
    main()
