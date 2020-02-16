# Maintainer: Thorsten Weimann <weimann.th@yahoo.com>
# Idea from: https://gitlab.com/r4dh4l/tachyon/-/blob/master/turn-server.md

pkgname=coturn-dyndns-git
pkgver=0.1
pkgrel=1
pkgdesc='Restart coturn if external IP changes'
arch=('any')
url='https://github.com/whitie/coturn-dyndns'
license=('MIT')
depends=('coturn' 'python')
optdepends=('miniupnpc: Get external IP from router')
source=('check_external_ip.timer' 'check_external_ip.service'
        'check_external_ip.py' 'external_ip_changed.path'
        'external_ip_changed.service' 'coturn-dyndns.service'
        'LICENSE' 'README.md')
sha256sums=('SKIP')

package() {
  install -Dm 755 check_external_ip.py "$pkgdir"/usr/bin/check_external_ip.py
  install -Dm 644 check_external_ip.timer "$pkgdir"/usr/lib/systemd/system/check_external_ip.timer
  install -Dm 644 check_external_ip.service "$pkgdir"/usr/lib/systemd/system/check_external_ip.service
  install -Dm 644 external_ip_changed.path "$pkgdir"/usr/lib/systemd/system/external_ip_changed.path
  install -Dm 644 external_ip_changed.service "$pkgdir"/usr/lib/systemd/system/external_ip_changed.service
  install -Dm 644 coturn-dyndns.service "$pkgdir"/usr/lib/systemd/system/coturn-dyndns.service
}
