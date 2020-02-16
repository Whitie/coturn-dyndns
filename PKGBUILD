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
md5sums=('8c7e4bbe9436bce8a036a751b2a3d1c5'
         'bffe92fb134d7e196ca30e965d84310f'
         '09a094854f986d1fa6212beeb8b1509c'
         'd23d5c0dc8f225bcbfbd23ef691b2697'
         '0dea87624e40064872efb980656e4479'
         '43809a1c03a76442d99b26f88bbf1af8'
         '683a216c6bcd595b7b4bbc281d5d37b1'
         '5f0255c6723d8064d82375edef62f32e')

package() {
  install -Dm 755 check_external_ip.py "$pkgdir"/usr/bin/check_external_ip.py
  install -Dm 644 check_external_ip.timer "$pkgdir"/usr/lib/systemd/system/check_external_ip.timer
  install -Dm 644 check_external_ip.service "$pkgdir"/usr/lib/systemd/system/check_external_ip.service
  install -Dm 644 external_ip_changed.path "$pkgdir"/usr/lib/systemd/system/external_ip_changed.path
  install -Dm 644 external_ip_changed.service "$pkgdir"/usr/lib/systemd/system/external_ip_changed.service
  install -Dm 644 coturn-dyndns.service "$pkgdir"/usr/lib/systemd/system/coturn-dyndns.service
}
