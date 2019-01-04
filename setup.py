from setuptools import setup

setup(name='kubios',
      version='0.1',
      author='Pedro Gomes',
      author_email='pgomes92@gmail.com',
      license='BSD 3-Clause License',
      description="Python package to support KUBIOS file management.",
      long_description="Python package to export RRI data in KUBIOS readable format and to read/import KUBIOS results " \
				   "from KUBIOS reports.",
      url='https://github.com/PGomes92/kubios',
      package_dir={'': '.'},
      packages=['kubios',],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Topic :: Scientific/Engineering :: Medical Science Apps.',
          'License :: OSI Approved :: BSD 3-Clause License',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3'
      ],
      install_requires=[
          'six',
      ],)