class Ciphey < Formula
  desc "Automated decryption tool"
  homepage ""
  url "https://github.com/Ciphey/Ciphey/archive/4.2.0.tar.gz"
  sha256 "013c438cc1f1c34c314bb202209acb36d9da142d4febeb21e5d4a06fa7b4dd7c"


  def install
      bin.install "ciphey"
  end

end
