# Maintainer: Thorsten Weimann <weimann.th@yahoo.com>
# Idea from: https://gitlab.com/r4dh4l/tachyon/-/blob/master/turn-server.md

pkgname=coturn-dyndns
pkgver=0.1
pkgrel=1
pkgdesc='Restart coturn if external IP changes'
arch=('x86_64')
url=''
license=('MIT')
depends=('coturn' 'python')
optdepends=('miniupnpc: Get external IP from router')
source=('check_external_ip.timer' 'check_external_ip.service'
        'check_external_ip.py' 'external_ip_changed.path'
        'external_ip_changed.service' 'coturn-dyndns.service')

package() {
  install -Dm 755 check_external_ip.py "$pkgdir"/usr/bin/check_external_ip.py
  install -Dm 644 check_external_ip.timer "$pkgdir"/usr/lib/systemd/system/check_external_ip.timer
  install -Dm 644 check_external_ip.service "$pkgdir"/usr/lib/systemd/system/check_external_ip.service
  install -Dm 644 external_ip_changed.path "$pkgdir"/usr/lib/systemd/system/external_ip_changed.path
  install -Dm 644 external_ip_changed.service "$pkgdir"/usr/lib/systemd/system/external_ip_changed.service
  install -Dm 644 coturn-dyndns.service "$pkgdir"/usr/lib/systemd/system/coturn-dyndns.service
}

sha256sums=(
    '24f1bf8d52a3854e997dce52caf6de56294674fd07ec2a8ea6e485a2a98e2508' # LICENSE
    '92e6192b03cab2af698f05ac529a75336de2c48be3489f71a2c76aca386b61d0' # README.md
    'c85220a7606aed5c8268240d5688a0124a93bde47f3585487b451aa904c8e5b5' # check_external_ip.py
    '7514b7c46ba891ba722a7be3856d96a1cfc1c79391fd74c87703f6d0d3ec83ff' # check_external_ip.service
    '6f1722ebafdbd1c9e398c0b6bd7f11436d175a02cb77dcf934820f23f8440539' # check_external_ip.timer
    'e97405d66bbd35ee40715af533f7678b0e3591ef00ee93a027337f3c748461fa' # coturn-dyndns.service
    '06397609e5f2dd096b977cc84360b9690f203875d51d1e2cb9dac0fec87b202b' # external_ip_changed.path
    'de19223570f69ac19d487425a0097cba389cab77cf5569ea93f7f82c7d82a30b' # external_ip_changed.service
)
