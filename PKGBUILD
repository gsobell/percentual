# Contributor: @gsobell
# Maintainer:  @gsobell

pkgname=percentual
pkgver=0.1.1
pkgrel=1
pkgdesc='a nCurses progress tracker'
arch=('any')
url='https://github.com/gsobell/percentual'
license=('GPL')
provides=("$pkgname")
depends=('python')
source=("$url/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('6c4b5b0fc11ddabd7c042981255a83c7a396009c5a335ce1d2f2ff051f3bb27d')

package() {
    cd $pkgname-$pkgver
    install -m 755 -TD "$pkgname.py" "$pkgdir/usr/bin/$pkgname"
    install -m 644 -TD "README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
    install -m 644 -TD "LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
