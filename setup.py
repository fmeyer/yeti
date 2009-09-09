from setuptools import setup, find_packages
import sys, os

version = '0.1'
README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(name='yeti',
      version=version,
      description="Writing unit examples in a readabler way",
      long_description=README,
      classifiers=[
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Topic :: Software Development :: Documentation',
          'Topic :: Software Development :: Testing',
          ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='bdd rspec spec',
      author='Fernando Meyer',
      author_email='fmcamargo@gmail.com',
      url='http://github.com/fmeyer/yeti',
      license='',
      package_dir={'yeti': 'src', 'yeti.specs': 'specs', 'yeti.examples': 'examples',},
      packages=['yeti', 'yeti.specs', 'yeti.examples',],
      package_data={'':['*.rst']},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'should-dsl',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
