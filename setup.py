try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

version = '0.1.20'

setup(
    name='hoverpy',
    install_requires=["requests"],
    packages=['hoverpy'],
    version=version,
    description='A python library for HoverFly',
    author='SpectoLabs',
    author_email='shyal@shyal.com',
    url='https://github.com/SpectoLabs/hoverpy',
    download_url='https://github.com/SpectoLabs/hoverpy/tarball/%s' % version,
    keywords=['testing', 'rest', 'caching', 'ci'],
    test_suite='hoverpy.tests.get_suite',
    classifiers=[],
    package_data={'hoverpy': ['cert.pem']}
)
