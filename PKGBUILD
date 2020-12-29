# Maintainer: Thorsten Weimann <weimann.th@yahoo.com>
# Idea from: https://gitlab.com/r4dh4l/tachyon/-/blob/master/turn-server.md

pkgname=coturn-dyndns-git
pkgver=0.2
pkgrel=1
pkgdesc='Restart coturn if external IP changes'
arch=('any')
url='https://github.com/whitie/coturn-dyndns'
license=('MIT')
depends=('coturn' 'curl')
source=('coturn-dyn-check-ip.timer' 'coturn-dyn-check-ip.service' 'coturn-dyn.conf'
        'coturn-dyn-check-ip.py' 'LICENSE' 'README.md')
md5sums=('6e2e946a06d4fe14f8bd521859bf3783'
         '634b5fa58a02a42b61012ea3ecc6be5b'
         'eb14e0cf4447e4222607ca8cbc5c525d'
         '1825899e21d86c84b1d1a2e164ab3a86'
         '683a216c6bcd595b7b4bbc281d5d37b1'
         '458e0ad5bb3da491a46ef11496e5c34f')

package() {
  install -Dm 755 coturn-dyn-check-ip.py "$pkgdir"/usr/bin/coturn-dyn-check-ip.py
  install -Dm 644 coturn-dyn-check-ip.timer "$pkgdir"/usr/lib/systemd/system/coturn-dyn-check-ip.timer
  install -Dm 644 coturn-dyn-check-ip.service "$pkgdir"/usr/lib/systemd/system/coturn-dyn-check-ip.service
  install -Dm 644 coturn-dyn.conf "$pkgdir"/etc/coturn-dyn.conf
}
