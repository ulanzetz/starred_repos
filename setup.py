from distutils.core import setup

setup(
    name='starred_repos',
    version='0.1',
    packages=['starred_repos'],
    url='https://github.com/ulanzetz/starred_repos',
    author='Ilya Ulanov',
    author_email='ulanzet@gmail.com',
    description='Simple utility to get github user starred repositories info',
    long_description=open('README.md').read(),
    install_requires=['requests']
)
