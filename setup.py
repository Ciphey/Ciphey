from setuptools import setup

setup(
    name='Ciphey',
    version='3.0.5',
    packages=['app', 'app.Decryptor', 'app.Decryptor.Encoding', 'app.Decryptor.basicEncryption', 'app.neuralNetworkMod',
              'app.languageCheckerMod'],
    url='https://github.com/brandonskerritt/ciphey',
    license='MIT',
    author='Brandon Skerritt',
    author_email='brandon@skerritt.blog',
    description='Automated decryption tool using machine learning'
)
