import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = """penelope.models
=============

for more details visit: http://getpenelope.github.com/"""

CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'Babel',
    'plone.i18n',
    'repoze.workflow',
    'setuptools',
    'SQLAlchemy',
    ]

tests_require = [
    'WebTest',
    'mock',
    'pyquery',
    'pytest',
    'pytest-cov',
    'pytest-pep8!=1.0.3',
    'pytest-xdist',
    'wsgi_intercept',
    'pyramid_robot'
    ]


setup(name='penelope.models',
      version='1.0dev0',
      description='Penelope main package',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        ],
      author='Penelope Team',
      author_email='penelopedev@redturtle.it',
      url='http://getpenelope.github.com',
      keywords='web wsgi bfg pylons pyramid',
      namespace_packages=['penelope'],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='penelope.models',
      install_requires = requires,
      tests_require=tests_require,
      entry_points = "",
      extras_require={
        'test': tests_require,}
      )
