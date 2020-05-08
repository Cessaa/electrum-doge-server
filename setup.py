from setuptools import setup

setup(
    name="electrum-doge-server",
    version="0.9",
    scripts=['run_electrum_doge_server','electrum-doge-server'],
    install_requires=['plyvel','jsonrpclib', 'irc==14.2.2'],
    package_dir={
        'electrumdogeserver':'src'
        },
    py_modules=[
        'electrumdogeserver.__init__',
        'electrumdogeserver.utils',
        'electrumdogeserver.storage',
        'electrumdogeserver.deserialize',
        'electrumdogeserver.networks',
        'electrumdogeserver.blockchain_processor',
        'electrumdogeserver.server_processor',
        'electrumdogeserver.processor',
        'electrumdogeserver.version',
        'electrumdogeserver.ircthread',
        'electrumdogeserver.stratum_tcp',
        'electrumdogeserver.stratum_http'
    ],
    description="Doge Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/electrumalt/electrum-doge-server/",
    long_description="""Server for the Electrum Lightweight Dogecoin Wallet"""
)


