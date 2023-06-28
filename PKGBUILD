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
sha256sums=('63071d33a62008c11345123e9e983524f2d4946c8b94d35dc4020b7313567da3')

package() {
    cd $pkgname-$pkgver
    install -m 755 -TD "$pkgname.py" "$pkgdir/usr/bin/$pkgname"
    install -m 644 -TD "README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
    install -m 644 -TD "LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
