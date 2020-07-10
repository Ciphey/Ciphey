# Maintainer: Ciphey <brandon@skerritt.blog> 
pkgname=Ciphey
pkgver='5.0.0rc2'
pkgrel=1
pkgdesc="Automated Description Tool"
arch=('any')
url="https://github.com/ciphey/ciphey"
license=('MIT')
depends=('python>=3.7')
makedepends=('python>=3.7')
install=
changelog=
#source=("$pkgname-$pkgver.tar.gz"
 #"$pkgname-$pkgver.patch")
noextract=()
md5sums=()
validpgpkeys=()

prepare() {
	python3 -m pip install --upgrade pip
}
package() {
	python3 -m pip install ciphey
}
