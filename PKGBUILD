# Contributor: @gsobell
# Maintainer:  @gsobell

pkgname=percentual
pkgver=0.0.1
pkgrel=1
pkgdesc='a nCurses progress tracker'
arch=('any')
url='https://github.com/gsobell/percentual'
license=('GPL')
provides=("$pkgname")
depends=('python')
source=("$url/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('')

package() {
    cd $pkgname-$pkgver
    install -Dm 755 $pkgname -t "$pkgdir/usr/bin"
    install -Dm 644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
