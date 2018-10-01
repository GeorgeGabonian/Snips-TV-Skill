from setuptools import setup

setup(
    name='snipsremote',
    version='1.0.0',
    description='Tv remote snips Skill',
    author='Snips Labs',
    url='',
    download_url='',
    license='MIT',
    install_requires=['smbus2', 'configparser','netaddr', ' pycryptodome'],
    test_suite="tests",
    keywords=['snips', 'tv', 'samsung'],
    packages=['snipsremote'],
    package_data={'snipsremote': ['Snipsspec']},
    include_package_data=True
)
