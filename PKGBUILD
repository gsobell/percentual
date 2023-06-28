# Contributor: @gsobell
# Maintainer:  @gsobell

pkgname=percentual
pkgver=0.1.0
pkgrel=1
pkgdesc='a nCurses progress tracker'
arch=('any')
url='https://github.com/gsobell/percentual'
license=('GPL')
provides=("$pkgname")
depends=('python')
source=("$url/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('55da50e13153335aa2083e6e543c98fe4ab723175178d2ac539d3ef42d4e09d3')

package() {
    cd $pkgname-$pkgver
    install -m 755 -TD "$pkgname.py" "$pkgdir/usr/bin/$pkgname"
    install -m 644 -TD "README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
    install -m 644 -TD "LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
